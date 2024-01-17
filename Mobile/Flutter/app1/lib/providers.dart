// import 'package:flutter/material.dart';
// import 'package:provider/provider.dart';
// import 'service.dart'; // Import the Service model
// import 'repository.dart'; // Import your ServiceRepository


// class ServiceProvider with ChangeNotifier {
//   List<Service> _services = [];

//   List<Service> get services => _services;

//   Future<void> loadServices() async {
//     // Load services from your repository here
//     // Replace this with your actual service loading logic
//     _services = await ServiceRepository().getAllServices();
//     notifyListeners();
//   }

//   Future<void> addService(Service newService) async {
//     // Add a service using your repository
//     await ServiceRepository().addService(newService);
//     await loadServices(); // Refresh the service list
//   }

//   Future<void> updateService(Service updatedService) async {
//     // Update a service using your repository
//     await ServiceRepository().updateService(updatedService);
//     await loadServices(); // Refresh the service list
//   }

//   Future<void> deleteService(int id) async {
//     // Delete a service using your repository
//     await ServiceRepository().deleteService(id);
//     await loadServices(); // Refresh the service list
//   }
// }
