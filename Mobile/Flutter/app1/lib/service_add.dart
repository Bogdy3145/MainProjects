import 'dart:async';

import 'package:app1/ServiceNotifier.dart';
import 'package:app1/sql/sql_helper.dart';
import 'package:flutter/material.dart';
import 'ApiRequests.dart';
import 'repository.dart'; // Import your ServiceRepository
import 'service.dart'; // Import the Service model
import 'package:provider/provider.dart';


class ServiceAddPage extends StatefulWidget {
  @override
  _ServiceAddPageState createState() => _ServiceAddPageState();
}

class _ServiceAddPageState extends State<ServiceAddPage> {

  // Create a Service object to store the form data
  Service _newService = Service(
    id: 0,
    name: '',
    provider: '',
    location: '',
    radius: 0,
    phone: '',
    price: 0,
  );

  final _formKey = GlobalKey<FormState>();

  

  @override
  Widget build(BuildContext context) {
    final serviceNotifier = Provider.of<ServiceNotifier>(context, listen: false);
    final nextId = serviceNotifier.findHighestId()+1;
    return Scaffold(
      appBar: AppBar(
        title: Text('Add Service'),
      ),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: EdgeInsets.all(16.0),
          children: <Widget>[
            TextFormField(
              decoration: InputDecoration(labelText: 'Name'),
              onChanged: (value) {
                setState(() {
                  _newService.name = value!;
                });
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a name';
                }
                return null;
              },
            ),
            TextFormField(
              decoration: InputDecoration(labelText: 'Provider'),
              onChanged: (value) {
                _newService.provider = value!;
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a provider';
                }
                return null;
              },
            ),
            TextFormField(
              decoration: InputDecoration(labelText: 'Location'),
              onChanged: (value) {
                _newService.location = value!;
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a location';
                }
                return null;
              },
            ),
            TextFormField(
              decoration: InputDecoration(labelText: 'Radius'),
              onChanged: (value) {
                _newService.radius = int.parse(value!);
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a radius';
                }
                return null;
              },
              keyboardType: TextInputType.number,
            ),
            TextFormField(
              decoration: InputDecoration(labelText: 'Phone'),
              onChanged: (value) {
                _newService.phone = value!;
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a phone number';
                }
                return null;
              },
            ),
            TextFormField(
              decoration: InputDecoration(labelText: 'Price'),
              onChanged: (value) {
                _newService.price = int.parse(value!);
              },
              validator: (value) {
          if (value == null || value.isEmpty) {
                  return 'Please enter a price';
                }
                return null;
              },
              keyboardType: TextInputType.number,
            ),
            ElevatedButton(

              onPressed: () async{

          try{
                var result = 0;
                try{
                      await ApiRequests.postRequest(
                        '/service',
                      _newService.toMap(),
                      ).timeout(
                        Duration(seconds: 2),
                        onTimeout: () {
                          // This callback is called if the network request times out
                          throw TimeoutException('The request to the server timed out');
                        },
                      );

                        // Insert new recipe in SQLite
                        result = await SQLHelper.instance.createItem(_newService.name,_newService.provider, _newService.location, _newService.radius, _newService.phone, _newService.price);
                      } 
                catch(e){ 
                        print("Error posting recipe to the server or timeout: $e");

                        // Save recipe to local DB with negative ID to be synced at next connection with the server
                          var negativeId = serviceNotifier.findLowestId();

                          if(negativeId > 0 )
                          {
                            // If it is the first added offline, just negate the id
                            _newService.id = - _newService.id;
                          }
                          else{
                            // If multiple are added offline, we need to find the lowest id and subtract 1 from it 
                            _newService.id = negativeId -1;
                          }

                        result = await SQLHelper.instance.createItem(_newService.name,_newService.provider, _newService.location, _newService.radius, _newService.phone, _newService.price);
                        if(result!=0)
                          print("Successfully posted recipe to local DB");}

                        if (result != 0) {
                    Navigator.pop(context, _newService);} 
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
              child: Text('Submit'),
            ),
          ],
        ),
      ),
    );
  }
}
