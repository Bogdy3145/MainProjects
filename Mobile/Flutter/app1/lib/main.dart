
import 'dart:async';
import 'dart:convert';

import 'package:app1/ServiceNotifier.dart';
import 'package:app1/sql/sql_helper.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'ApiRequests.dart';
import 'repository.dart';
import 'service.dart';
import 'service_detail.dart';
import 'service_add.dart';


Future<void> syncCachedRequests() async {
  try {
    final cachedRequests = await SQLHelper.instance.getCachedRequests();

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
        await SQLHelper.instance.removeCachedRequest(cachedRequest['id']);
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
          '/service',
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

void main() async{

    WidgetsFlutterBinding.ensureInitialized();

   bool isInternetConnected = await ApiRequests.isInternetConnected();

  List<Service> services = [];

  if (isInternetConnected) {
    
    // Get local DB Services
      List<Service> localDbServices = (await SQLHelper.instance.getServices()).cast<Service>();


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
      await SQLHelper.instance.clearLocalDatabase();
  
      
      // Insert services received from serer
      await SQLHelper.instance.insertServices(serverServices); 

      services = serverServices;
    } catch (e) {
      print("Error fetching services from the server: $e");

      // If fetching from the server fails, fetch data from the local database
      services = (await SQLHelper.instance.getServices()).cast<Service>();
    }
  } else {
    // If there is no internet connection, fetch data from the local database
    services = (await SQLHelper.instance.getServices()).cast<Service>();
  }

  runApp(
    MultiProvider(providers: [ChangeNotifierProvider(create: (context) => ServiceNotifier()..setServices(services)),], child:  MainPage(),),);
    
}

class MainPage extends StatefulWidget {
  @override
  _MainPageState createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  //final ServiceRepository _serviceRepository = ServiceRepository();
  List<Service> _services = [];

  @override
  void initState() {
    super.initState();
  }

  

 void _addService() async {
  // Navigate to the page for adding a new service and receive the result
  final newServiceAdded = await Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => ServiceAddPage(),
    ),
  );

  if (newServiceAdded == true) {
    // Reload services if a new service was added successfully
    
  }
}



  


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Service List'),
      ),
      body: Consumer<ServiceNotifier>(
        builder: (context, serviceNotifier, child){
          final services = serviceNotifier.services;
          return ServiceList(services: services);
        }
      ),
      floatingActionButton: FloatingActionButton(onPressed: () async{
        final newService = await Navigator.of(context).push(MaterialPageRoute(builder:(context) => ServiceAddPage(),),);
      
      if (newService != null){
        context.read<ServiceNotifier>().addService(newService);
        final scaffoldMessenger = ScaffoldMessenger.of(context);
        scaffoldMessenger.showSnackBar(
          SnackBar(content: Text('New service added'),
          duration: Duration(seconds: 2),
          )
        );

      }
      },
      tooltip: 'Add service',
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
              
                builder: (context) => ServiceDetailPage(service: service),
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
        Text('Description: ${service.location}', style: TextStyle(fontSize: 15),),
       
      ],
    ),
  ),
)
        );
      },
    );
  }
}
