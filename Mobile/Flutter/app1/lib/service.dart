class Service {
  int id;
  String name;
  String provider;
  String location;
  int radius;
  String phone;
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

  factory Service.fromJson(Map<String, dynamic> json) {
    return Service(
      id: json['id'] as int,
      name: json['name'] as String,
      provider: json['provider'] as String,
      location: json['location'] as String,
      radius: json['radius'] as int,
      phone: json['phone'] as String,
      price: json['price'] as int,
    );
  }

  Map<String, dynamic> toJson() {
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

  Service copyWith({
    int? id,
    String? name,
    String? provider,
    String? location,
    int? radius,
    String? phone,
    int? price,
  }) {
    return Service(
      id: id ?? this.id,
      name: name ?? this.name,
      provider: provider ?? this.provider,
      location: location ?? this.location,
      radius: radius ?? this.radius,
      phone: phone ?? this.phone,
      price: price ?? this.price,
    );
  }

  Map<String, dynamic> toMap() {
  return {
    'id': id,
    'name': name,
    'provider': provider,
    'location': location,
    'radius': radius,
    'phone': phone,
    'price': price
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

  @override
  String toString() {
    return 'Service(id: $id, name: $name, provider: $provider, location: $location, radius: $radius, phone: $phone, price: $price)';
  }

  int getId() {
    return id;
  }
}
