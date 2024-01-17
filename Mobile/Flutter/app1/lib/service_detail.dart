import 'dart:async';
import 'dart:convert';

import 'package:app1/sql/sql_helper.dart';
import 'package:flutter/material.dart';
import 'ApiRequests.dart';
import 'repository.dart';
import 'service.dart';

class ServiceDetailPage extends StatefulWidget {
  final Service service;
  // final Function(Service) onUpdate; // Add this line
  // final void Function(int) onDelete; // Add this line
  
ServiceDetailPage({
    required this.service,
    // required this.onUpdate,
    // required this.onDelete,
  });
  @override
  _ServiceDetailPageState createState() => _ServiceDetailPageState();
}

class _ServiceDetailPageState extends State<ServiceDetailPage> {
  final _formKey = GlobalKey<FormState>();
  final TextEditingController locationController = TextEditingController();
  final TextEditingController nameController = TextEditingController();
  final TextEditingController providerController = TextEditingController();
  final TextEditingController radiusController = TextEditingController();
  final TextEditingController phoneController = TextEditingController();
  final TextEditingController priceController = TextEditingController();
  
  @override
  void initState() {
    super.initState();
    providerController.text = widget.service.provider;
    nameController.text = widget.service.name;
    locationController.text = widget.service.location.toString();
    radiusController.text = widget.service.radius as String;
    phoneController.text = widget.service.phone;
    priceController.text = widget.service.price as String;
  }

  

  Future<void> deleteServiceOnServer(int serviceId) async {
   
  }



  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF8ecae6),
      appBar: AppBar(
        automaticallyImplyLeading: false,
        backgroundColor: Color(0xFFFFB8500),
        title: Text('Edit Service'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            children: <Widget>[
              TextFormField(
                controller: providerController,
                decoration: InputDecoration(labelText: 'Provider'),
              ),
              TextFormField(
                controller: nameController,
                decoration: InputDecoration(labelText: 'Service Name'),
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
              ),TextFormField(
                controller: priceController,
                decoration: InputDecoration(labelText: 'Price'),
              ),
              ElevatedButton(
                onPressed: () async {
                  final editedService = Service(
                    id: widget.service.id,
                    provider: providerController.text,
                    name: nameController.text,
                    location: locationController.text,
                    radius: int.tryParse(radiusController.text) ?? 0,
                    phone: phoneController.text,
                    price: int.tryParse(priceController.text) ?? 0,
                  );

                  var result = 0;

                  try {
                      await ApiRequests.putRequest(
                        '/update',  
                        editedService.toMap(),  
                      ).timeout(
                        Duration(seconds: 2),
                        onTimeout: () {
                          // This callback is called if the network request times out
                          throw TimeoutException('The request to the server timed out');
                        },
                      );

                     result = await SQLHelper.instance.updateService(editedService.id, editedService.name, editedService.provider, editedService.location, editedService.radius as String, editedService.phone, editedService.price as String);
                     final uId = editedService.id;
                    print("Updated service id :$uId");
                    

                    } catch (e) {
                        print("Error when trying to update service on the server or timeout: $e");

                        result = await SQLHelper.instance.updateService(editedService.id, editedService.name, editedService.provider, editedService.location, editedService.radius as String, editedService.phone, editedService.price as String);
                        final uId = editedService.id;
                        if(result!=0)
                          {
                            print("Successfully updated service locally:$uId");

                            // Convert the updated service to a map
                            Map<String, dynamic> editedServiceMap = editedService.toMap();

                            // Convert the map to a JSON string
                            String body = jsonEncode(editedServiceMap);

                            // Cache the update request
                            await SQLHelper.instance.cacheRequest('put', body);
                            print("Successfully cached update request for service id :$uId");
                            
                          }

                       
                       }
                 
                     if (result != 0) {
                          Navigator.pop(context, editedService);
                        } else {
                          print("Error when trying to update service locally");
                        
                        }


                  final scaffoldMessenger = ScaffoldMessenger.of(context);
                  scaffoldMessenger.showSnackBar(
                    SnackBar(
                      content: Text('Service updated successfully'),
                      duration: Duration(seconds: 2),
                    ),
                  );
                },
                style: ElevatedButton.styleFrom(backgroundColor: Color(0xFF023047)),
                child: Text('Save Changes'),
              ),

              ElevatedButton(
                onPressed: () async {
                  showDialog(
                    context: context,
                    builder: (context) => AlertDialog(
                      title: Text('Delete Service'),
                      content: Text('Are you sure you want to delete this service? This action cannot be undone!'),
                      actions: <Widget>[
                        TextButton(
                          child: Text('Cancel'),
                          onPressed: () {
                            Navigator.of(context).pop();
                          },
                        ),
                        TextButton(
                          child: Text('Delete'),
                          onPressed: () async {
                           
                          
                             
                              final idToDelete = widget.service.id;
                              var result = 0;

                              
                           try {

                            await ApiRequests.deleteRequest(
                              '/delete/$idToDelete',  
                            ).timeout(
                              Duration(seconds: 2),
                              onTimeout: () {
                                // This callback is called if the network request times out
                                throw TimeoutException('The request to the server timed out');
                              },
                            );

                            // Delete service from SQLite
                             result = await SQLHelper.instance.deleteService(widget.service.id);
                            print("Deleted service: $idToDelete");
                            
                          } catch (e) {
                            print("Error when trying to delete service on the server or timeout: $e");
                              // Delete service from SQLite
                                result = await SQLHelper.instance.deleteService(widget.service.id);
                            
                                if(result!=0)
                                  { 
                                    print("Successfully deleted service locally with id:$idToDelete");

                                     await SQLHelper.instance.cacheRequest('delete', jsonEncode({'id': idToDelete}));
                                     
                                    print("Successfully cached delete request for service id :$idToDelete");
                                  }
                       
                          }
                         
                            
                            if (result != 0) {
                              Navigator.pop(context, widget.service.id);
                              Navigator.pop(context, widget.service.id);
                            } else {
                              print("Error when trying to delete service");
                              showDialog(
                                context: context,
                                builder: (context) => AlertDialog(
                                  title: Text('Error'),
                                  content: Text('Failed to delete the service. Please try again.'),
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
                        ),
                      ],
                    ),
                  );
                },
                style: ElevatedButton.styleFrom(backgroundColor: Color(0xFF023047)),
                child: Text('Delete Service'),
              ),

              
            ],
          ),
        ),
      ),
    );
  }
}