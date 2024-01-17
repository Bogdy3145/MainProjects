import asyncio
import json
import threading

import websockets as websockets
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'  # SQLite database file
db = SQLAlchemy(app)
connected_clients = []


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

    data['id'] = new_service.id
    json_data = json.dumps(data)

    # Broadcast the updated request data to the WebSocket server
    asyncio.run(broadcast_request("ADD#" + json_data))
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

        asyncio.run(broadcast_request("UPDATE#" + str(request.data, "UTF-8")))

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
        asyncio.run(broadcast_request("DELETE#" + str(service_id)))
        return jsonify({'message': 'Service deleted successfully'})
    else:
        return jsonify({'message': 'Service not found'}), 404




async def send_request(websocket, message):
    # Send message to one client
    try:
        await websocket.send(message)
    except websockets.ConnectionClosed:
        connected_clients.remove(websocket)


async def broadcast_request(message):
    # Send new request to all connected clients
    print("Broadcasting new request to all connected clients: "+message)
    for socket in connected_clients:
        asyncio.create_task(send_request(socket, message))


async def handle_clients(websocket):
    # Add/ remove new connections
    connected_clients.append(websocket)
    print("New client connected" + str(websocket))
    try:
        await websocket.wait_closed()
    finally:
        connected_clients.remove(websocket)



async def start_websocket():
    # Start websocket
    async with websockets.serve(handle_clients, "192.168.3.123", 8765, ssl=None):
        await asyncio.Future()


def websocket_thread():
    asyncio.run(start_websocket(),debug=False)


def server_requests_thread():
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables before running the app
    thread_web = threading.Thread(target=server_requests_thread)
    thread_server = threading.Thread(target=websocket_thread)
    # Start server requests and websocket on separate threads
    thread_server.start()
    thread_web.start()