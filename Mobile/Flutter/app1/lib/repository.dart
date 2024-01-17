// import 'sql/sql_helper.dart'; // Import your SQLHelper class
// import 'service.dart'; // Import the Service model
// import 'package:http/http.dart' as http;
// import 'dart:convert';


// class ServiceRepository {

//     final String baseUrl = 'http://192.168.1.196:5000'; // Replace with your server URL

//   // Method to fetch all services from the database

//   Future<List<Service>> getAllServices() async {
//     final response = await http.get(Uri.parse('$baseUrl/services'));
//     print(response);

//     if (response.statusCode == 200) {
//       final List<dynamic> serviceJson = json.decode(response.body);
//       return serviceJson.map((json) => Service.fromJson(json)).toList();
//     } else {
//       final List<Map<String, dynamic>> serviceData = await SQLHelper.getServices();
//       return serviceData.map((data) => Service(
//         id: data['id'],
//         name: data['name'],
//         provider: data['provider'],
//         location: data['location'],
//         radius: data['radius'],
//         phone: data['phone'],
//         price: data['price'],
//       )).toList();
    
//     }
//   }
//   // Future<List<Service>> getAllServices() async {
//   //   final List<Map<String, dynamic>> serviceData = await SQLHelper.getServices();
//   //   return serviceData.map((data) => Service(
//   //     id: data['id'],
//   //     name: data['name'],
//   //     provider: data['provider'],
//   //     location: data['location'],
//   //     radius: data['radius'],
//   //     phone: data['phone'],
//   //     price: data['price'],
//   //   )).toList();
//   // }

//   // Method to add a new service to the database
//   Future<int> addService(Service service) async {
//   final response = await http.post(
//     Uri.parse('$baseUrl/service'),
//     headers: <String, String>{
//       'Content-Type': 'application/json; charset=UTF-8',
//     },
//     body: jsonEncode(service.toJson()),
//   );

//   if (response.statusCode == 201) {
//     final responseData = json.decode(response.body);
//     if (responseData != null && responseData['id'] != null) {
//       return responseData['id'];
//     } else {
//       throw Exception('Failed to parse service ID from response');
//     }
//   } else {
//     throw Exception('Failed to add service, status code: ${response.statusCode}');
//   }
// }


//   // Future<int> addService(Service service) async {
//   //   return SQLHelper.createItem(
//   //     service.name,
//   //     service.provider,
//   //     service.location,
//   //     service.radius,
//   //     service.phone,
//   //     service.price,
//   //   );
//   // }


//    Future<int> updateService(Service service) async {
//     final response = await http.put(
//       Uri.parse('$baseUrl/service/${service.id}'),
//       headers: <String, String>{
//         'Content-Type': 'application/json; charset=UTF-8',
//       },
//       body: jsonEncode(service.toJson()), // Convert service object to JSON
//     );

//     if (response.statusCode == 200) {
//       return json.decode(response.body)['id']; // Or handle response as needed
//     } else {
//       print('Updating Service: $service'); 
//       return SQLHelper.updateService(
//         service.id,
//         service.name,
//         service.provider,
//         service.location,
//         service.radius.toString(),
//         service.phone,
//         service.price.toString(),
//     );
//     }
//   }

//   // Method to update an existing service in the database
//   // Future<int> updateService(Service service) async {
//   //   print('Updating Service: $service'); 
//   //   return SQLHelper.updateService(
//   //     service.id,
//   //     service.name,
//   //     service.provider,
//   //     service.location,
//   //     service.radius.toString(),
//   //     service.phone,
//   //     service.price.toString(),
//   //   );
//   // }

//   // Method to delete a service from the database
//   Future<void> deleteService(int id) async {
//     await SQLHelper.deleteService(id);
//   }
// }
