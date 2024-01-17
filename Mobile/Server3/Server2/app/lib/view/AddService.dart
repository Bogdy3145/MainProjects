  import 'dart:async';

import 'package:app/database/database_service.dart';
  import 'package:app/model/Service.dart';
import 'package:app/server/ApiRequests.dart';
  import 'package:app/view/ServiceNotifier.dart';
  import 'package:flutter/material.dart';
  import 'package:provider/provider.dart';

  class AddService extends StatefulWidget {
    @override
    _AddServiceState createState() => _AddServiceState();
  }

  class _AddServiceState extends State<AddService> {
    final TextEditingController nameController = TextEditingController();
    final TextEditingController providerController = TextEditingController();
    final TextEditingController locationController = TextEditingController();
    final TextEditingController radiusController = TextEditingController();
    final TextEditingController phoneController = TextEditingController();
    final TextEditingController priceController = TextEditingController();


    @override
    Widget build(BuildContext context) {
      final serviceNotifier = Provider.of<ServiceNotifier>(context, listen: false);
      final nextId = serviceNotifier.findHighestId()+1;
      return Scaffold(
        backgroundColor: Color.fromARGB(255, 0, 201, 191),
        appBar: AppBar(
          title: Text('Add Service'),
          backgroundColor: Color.fromARGB(255, 0, 195, 10),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
        
          child: Column(
            children: <Widget>[
              
              TextFormField(
                controller: nameController,
                decoration: InputDecoration(labelText: 'Service Name'),
              ),
              TextFormField(
                controller: providerController,
                decoration: InputDecoration(labelText: 'Service Provider'),
              ),
              TextFormField(
                controller: locationController,
                decoration: InputDecoration(labelText: 'Location'),
              ),
              TextFormField(
                controller: radiusController,
                decoration: InputDecoration(labelText: 'Radius'),
              ),
              TextFormField(
                controller: phoneController,
                decoration: InputDecoration(labelText: 'Phone'),
              ),
              TextFormField(
                controller: priceController,
                decoration: InputDecoration(labelText: 'Price'),
              ),

  ElevatedButton(
    
    onPressed: () async {
      final newService = Service(
        id: nextId,
        name: nameController.text,
        provider: providerController.text,
        location: locationController.text,
        radius: int.tryParse(radiusController.text) ?? 9,
        phone: phoneController.text,
        price: int.tryParse(priceController.text) ?? 9
      );

    
    
      
      try {
          var result = 0;
          // Post to server
          try {
  
          await ApiRequests.postRequest(
            '/add_service',
          newService.toMap(),
          ).timeout(
            Duration(seconds: 2),
            onTimeout: () {
              // This callback is called if the network request times out
              throw TimeoutException('The request to the server timed out');
            },
          );
            result =  await DatabaseService.instance.insertService(newService);
             
            if(result == 999 && nextId !=999 && nextId != 998)
              result = -1;

             //result = await DatabaseService.instance.insertService(newService);
          } 
        catch (e) 
              {
            print("Error posting service to the server or timeout: $e");

            // Save service to local DB with negative ID to be synced at next connection with the server
              var negativeId = serviceNotifier.findLowestId();

              if(negativeId > 0 )
              {
                // If it is the first added offline, just negate the id
                newService.id = - newService.id;
              }
              else{
                // If multiple are added offline, we need to find the lowest id and subtract 1 from it 
                newService.id = negativeId -1;
              }

             result = await DatabaseService.instance.insertService(newService);
             if(result!=0)
              print("Successfully posted service to local DB");
              }

          
       

        if(result == -1)
          newService.id = 0;
        if (result != 0) {
        Navigator.pop(context, newService);} 
      else {
        // Alert dialog for error
        print("Error when trying to add new service in local database");
        showDialog(
          context: context,
          builder: (context) => AlertDialog(
            title: Text('Error'),
            content: Text('Failed to add a new service. Please try again.'),
            actions: <Widget>[
              TextButton(
                child: Text('OK'),
                onPressed: () {
                  Navigator.of(context).pop();
                },
              ),
            ],
          ),
        );
      }
  } catch (e) {
    // Log the error message 
    print("Error when trying to add new service: $e");

    // Show AlertDialog
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Error'),
        content: Text('Failed to add a new service. Please try again.'),
        actions: <Widget>[
          TextButton(
            child: Text('OK'),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      ),
    );
  }
      
    },
    style: ElevatedButton.styleFrom(backgroundColor:Color(0xFF023047),),
    child: Text('Add Service'),
    
  )


            ],
          ),
        ),
      );
    }
  }
