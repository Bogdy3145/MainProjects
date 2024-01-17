import 'dart:async';
import 'dart:convert';

import 'package:app/server/ApiRequests.dart';
import 'package:app/view/EditService.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:app/database/database_service.dart';
import 'package:app/model/Service.dart';
import 'package:app/view/AddService.dart';
import 'package:app/view/ServiceNotifier.dart';

Future<void> syncCachedRequests() async {
  try {
    final cachedRequests = await DatabaseService.instance.getCachedRequests();

    for (var cachedRequest in cachedRequests) {
       final method = cachedRequest['method'];
        final bodyString = cachedRequest['body'];

      // Parse the JSON string into a Dart map
        final body = json.decode(bodyString);
        
        print('Body for cached request is: $body');
        final id = body['id'];
    
      try {
        if (method.toLowerCase() == 'put') {
          print("Sending PUT request for cached service:$id");
          // If the method is PUT, assume it's an 'update' request
          await ApiRequests.putRequest('/update', body).timeout(
            Duration(seconds: 2),
            onTimeout: () {
              // Handle the timeout
              print('Timeout syncing cached request: $id');
            },
          );
        } else if (method.toLowerCase() == 'delete') {
          
          print("Sending DELETE request for cached service:$id");
          // If the method is DELETE, assume it's a 'delete' request
          await ApiRequests.deleteRequest('/delete/$id').timeout(
            Duration(seconds: 2),
            onTimeout: () {
              // Handle the timeout
              throw TimeoutException('The request to the server timed out');
            },
          );
        }

        // Remove the cached request as it was successfully sent to the server
        await DatabaseService.instance.removeCachedRequest(cachedRequest['id']);
      } catch (e) {
        // Log the error message to the console
        print('Error syncing cached request: $e');
      }
    }
  } catch (e) {
    // Log the error message to the console
    print('Error syncing cached requests: $e');
  }
}

Future<void> syncLocalServicesToServer(List<Service> localServices) async {

  // Post services that are fresh (negative ID)
  for (var service in localServices) {
    if (service.id < 0) {
      // Service has a negative ID, indicating it is not yet synced with the server
      try {
        // Post to server
        await ApiRequests.postRequest(
          '/add_service',
          service.toMap(),
        ).timeout(
          Duration(seconds: 2),
          onTimeout: () {
            // Handle the timeout
            print('Timeout syncing service to the server:${service.id}');
          },
        );

        
      } catch (e) {
        // Handle the error
        print('Error posting service ${service.id} to the server: $e');
      }
    }
  }

  // Make updates/ deletes on already existing services in server
   await syncCachedRequests();
}


void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  
  //  Check for an internet connection
  bool isInternetConnected = await ApiRequests.isInternetConnected();

  List<Service> services = [];

  //  If there is an internet connection, fetch data from the server
  if (isInternetConnected) {
    
    // Get local DB Services
      List<Service> localDbServices = await DatabaseService.instance.getServices();


      // Sync local services with negative IDs to the server
      await syncLocalServicesToServer(localDbServices);

      
    try {
      print("Trying to fetch data from server");

      // Use the timeout feature to set a 5-second timeout for the network request

      List<Service> serverServices = await ApiRequests.getServices().timeout(
      Duration(seconds: 10),
      onTimeout: () {
        // This callback is called if the network request times out
        throw TimeoutException('The request to the server timed out');
      },
    ).then((serviceMap) {
      return serviceMap.map((serviceMap) => Service.fromMap(serviceMap)).toList();
    });

      // Clear the local database after successfully syncing with the server
      await DatabaseService.instance.clearLocalDatabase();
  
      
      // Insert services received from serer
      await DatabaseService.instance.insertServices(serverServices); 

      services = serverServices;
    } catch (e) {
      print("Error fetching services from the server: $e");

      // If fetching from the server fails, fetch data from the local database
      services = await DatabaseService.instance.getServices();
    }
  } else {
    // If there is no internet connection, fetch data from the local database
    services = await DatabaseService.instance.getServices();
  }

  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context) => ServiceNotifier()..setServices(services)),
      ],
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    
    return MaterialApp(
      title: 'Cook Book',
      theme: ThemeData(
       
    
    
      ),
      home: const MyHomePage(title: 'Services Page'),
    );
  }
}

class MyHomePage extends StatelessWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
        backgroundColor: Color.fromARGB(255, 0, 195, 10),
      ),
      backgroundColor: Color.fromARGB(255, 0, 201, 191),
      body: Consumer<ServiceNotifier>(
        builder: (context, serviceNotifier, child) {
          final services = serviceNotifier.services;
          return ServiceList(services: services);
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async {
          final newService = await Navigator.of(context).push(
            MaterialPageRoute(
              builder: (context) => AddService(),
            ),
          );

          if (newService != null) {
            // Add the new service to the list
            context.read<ServiceNotifier>().addService(newService);
            final scaffoldMessenger = ScaffoldMessenger.of(context);
            scaffoldMessenger.showSnackBar(
              SnackBar(
                content: Text('New service added successfully'),
                duration: Duration(seconds: 2), 
              ),
            );
          }
        },
        tooltip: 'Add Service',
        backgroundColor: Color(0xFF023047),
        child: Icon(Icons.add),
      ),
    );
  }
}

class ServiceList extends StatelessWidget {
  final List<Service> services;

  const ServiceList({Key? key, required this.services}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: services.length,
      itemBuilder: (context, index) {
        final service = services[index];
        return GestureDetector(
          onTap: () async {
            
            final updatedService = await Navigator.of(context).push(
              MaterialPageRoute(
              
                builder: (context) => EditService(service: service),
              ),
            );
          
            if (updatedService != null) {
             if (updatedService is Service) {
                    // The service was updated, we returned a Service type
                    // Update the service in the UI
                    context.read<ServiceNotifier>().updateService(updatedService);
                    final scaffoldMessenger = ScaffoldMessenger.of(context);
                    scaffoldMessenger.showSnackBar(
                      SnackBar(
                        content: Text('Service updated successfully'),
                        duration: Duration(seconds: 2), 
                      ),
                    );
                  }
                  else
                      if(updatedService is int) {
                        
                        // The service was deleted, we returned an int - the ID of the deleted service
                        final scaffoldMessenger = ScaffoldMessenger.of(context);
                        scaffoldMessenger.showSnackBar(
                          SnackBar(
                            content: Text('Service deleted successfully'),
                            duration: Duration(seconds: 2), 
                          ),
                        );
                        
                        context.read<ServiceNotifier>().deleteService(updatedService);
                       
                      }
                }
          },
          child: ListTile(
  title: Text('${service.name}',  style: TextStyle(fontSize: 20,) ),
 
  subtitle: Padding(
    padding: const EdgeInsets.all(8.0), 
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('Provider: ${service.provider}', style: TextStyle(fontSize: 15),),
       
      ],
    ),
  ),
)
        );
      },
    );
  }
}
