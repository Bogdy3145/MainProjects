class Service {
   int id; // You can set this when adding to a database
  final String name; 
  final String provider; 
  final String location; 
  int radius; 
  final String phone; 
  int price;
  

  Service({
    required this.id,
    required this.name,
    required this.provider,
    required this.location,
    required this.radius,
    required this.phone,
    required this.price,
  });

  Map<String, dynamic> toMap() {
  return {
    'id': id,
    'name': name,
    'provider': provider,
    'location': location,
    'radius': radius,
    'phone': phone,
    'price': price,
  };
}

factory Service.fromMap(Map<String, dynamic> map) {
  return Service(
    id: map['id'],
    name: map['name'],
    provider: map['provider'],
    location: map['location'],
    radius: map['radius'],
    phone: map['phone'],
    price: map['price'],
  );
}
 int getId() {
    return id;
  }

  


}

