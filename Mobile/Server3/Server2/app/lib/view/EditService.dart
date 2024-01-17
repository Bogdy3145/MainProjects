
import 'dart:async';
import 'dart:convert';

import 'package:app/server/ApiRequests.dart';
import 'package:flutter/material.dart';
import 'package:app/database/database_service.dart';
import 'package:app/model/Service.dart';


class EditService extends StatefulWidget {
  final Service service;

  EditService({required this.service});

  @override
  _EditServiceState createState() => _EditServiceState();
}

class _EditServiceState extends State<EditService> {
  final TextEditingController nameController = TextEditingController();
    final TextEditingController providerController = TextEditingController();
    final TextEditingController locationController = TextEditingController();
    final TextEditingController radiusController = TextEditingController();
    final TextEditingController phoneController = TextEditingController();
    final TextEditingController priceController = TextEditingController();

  @override
  void initState() {
    super.initState();
    nameController.text = widget.service.name;
    providerController.text = widget.service.provider;
    locationController.text = widget.service.location;
    radiusController.text = widget.service.radius.toString();
    phoneController.text = widget.service.phone;
    priceController.text = widget.service.price.toString();
  }


  Future<void> deleteServiceOnServer(int serviceId) async {
   
  }



  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color.fromARGB(255, 0, 201, 191),
      appBar: AppBar(
        automaticallyImplyLeading: false,
        backgroundColor: Color.fromARGB(255, 0, 195, 10),
        title: Text('Edit Service'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            children: <Widget>[
              TextFormField(
                controller: nameController,
                decoration: InputDecoration(labelText: 'Name'),
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
                  final editedService = Service(
                    id: widget.service.id,
                    name: nameController.text,
                    provider: providerController.text,
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

                     result = await DatabaseService.instance.updateService(editedService);
                     final uId = editedService.id;
                    print("Updated service id :$uId");
                    

                    } catch (e) {
                        print("Error when trying to update service on the server or timeout: $e");

                        result = await DatabaseService.instance.updateService(editedService);
                        final uId = editedService.id;
                        if(result!=0)
                          {
                            print("Successfully updated service locally:$uId");

                            // Convert the updated service to a map
                            Map<String, dynamic> editedServiceMap = editedService.toMap();

                            // Convert the map to a JSON string
                            String body = jsonEncode(editedServiceMap);

                            // Cache the update request
                            await DatabaseService.instance.cacheRequest('put', body);
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
                             result = await DatabaseService.instance.deleteService(widget.service.id);
                            print("Deleted service: $idToDelete");
                            
                          } catch (e) {
                            print("Error when trying to delete service on the server or timeout: $e");
                              // Delete service from SQLite
                                result = await DatabaseService.instance.deleteService(widget.service.id);
                            
                                if(result!=0)
                                  { 
                                    print("Successfully deleted service locally with id:$idToDelete");

                                     await DatabaseService.instance.cacheRequest('delete', jsonEncode({'id': idToDelete}));
                                     
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

              // Padding(
              //   padding: EdgeInsets.only(top: 20.0),
              //   child: Row(
              //     mainAxisAlignment: MainAxisAlignment.center,
              //     children: [
              //       Text(
              //         'Likes: $likes',
              //         style: TextStyle(fontSize: 16),
              //       ),
              //       IconButton(
              //         icon: Icon(Icons.thumb_up, size: 28),
              //         onPressed: () {
              //           setState(() {
              //             likes++;
              //             widget.service.setLikes(likes);
              //           });
              //         },
              //       ),
              //     ],
              //   ),
              // ),
            ],
          ),
        ),
      ),
    );
  }
}
