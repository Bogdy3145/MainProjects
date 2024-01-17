import asyncio
import json
#import threading
from threading import Thread
from flask_cors import CORS
import websockets
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'  # SQLite database file
db = SQLAlchemy(app)
connected_clients = set()


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    provider = db.Column(db.String(255), nullable=False)
    location = db.Column(db.Text, nullable=False)
    radius = db.Column(db.Integer, default=0)
    phone = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'provider': self.provider,
            'location': self.location,
            'radius' : self.radius,
            'phone' : self.phone,
            'price': self.price,
        }

@app.route('/')
def home():
    return render_template('index.html', message='Hello')

@app.route('/add_service', methods=['POST'])
def add_service():
    # Print the current thread ID
    print(f"Handling request in thread {threading.current_thread().ident}")

    data = request.get_json()
    new_service = Service(
        name=data['name'],
        provider=data['provider'],
        location=data['location'],
        radius=data['radius'],
        phone=data['phone'],
        price=data['price'],
    )

    db.session.add(new_service)
    db.session.commit()
    print("Service added successfully")
    return jsonify({'message': 'Service added successfully'})

@app.route('/update', methods=['PUT'])
def update_service():
    # Print the current thread ID
    print(f"Handling request in thread {threading.current_thread().ident}")

    data = request.get_json()
    service_id = data.get('id')
    service = Service.query.get(service_id)

    if service:
        # Update the recipe with the data received in the request
        service.name = data['name']
        service.provider = data['provider']
        service.location = data['location']
        service.radius = data['radius']
        service.phone = data['phone']
        service.price = data['price']

        db.session.commit()
        print("Service updated successfully")
        return jsonify({'message': 'Service updated successfully'})
    else:
        return jsonify({'message': 'Service not found'}), 404

@app.route('/services', methods=['GET'])
def get_all_services():

    # Print the current thread ID
    print(f"Handling request in thread {threading.current_thread().ident}")

    services = Service.query.all()
    services_list = [service.to_dict() for service in services]
    return jsonify({'services': services_list})

@app.route('/delete/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = Service.query.get(service_id)

    # Print the current thread ID
    print(f"Handling request in thread {threading.current_thread().ident}")

    if service:
        db.session.delete(service)
        db.session.commit()
        print("Service deleted successfully")
        return jsonify({'message': 'Service deleted successfully'})
    else:
        return jsonify({'message': 'Service not found'}), 404

async def send(websocket, message):
    try:
        await websocket.send(message)
    except websockets.ConnectionClosed:
        CLIENTS.remove(websocket)
        pass


async def broadcast(message):
    for websocket in CLIENTS:
        asyncio.create_task(send(websocket, message))


async def echo(websocket):
    CLIENTS.append(websocket)
    try:
        # data = await websocket.recv()
        # print(data)

        await websocket.wait_closed()
    finally:
        CLIENTS.remove(websocket)


async def main_sockets():
    async with websockets.serve(echo, "0.0.0.0", 8765, ssl=None):
        await asyncio.Future()


def routine1():
    asyncio.run(main_sockets(), debug=False)


def routine2():
    app.run(host="0.0.0.0", debug=False, threaded=True)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables before running the app


    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    # Flash has built-in with the "threaded = True" option:
    # implementation using the SocketServer.ThreadingMixIn class
