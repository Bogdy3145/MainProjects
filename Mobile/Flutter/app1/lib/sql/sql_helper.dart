import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart' as sql;
import 'package:sqflite/sqlite_api.dart';
import 'package:app1/service.dart';

class SQLHelper{

  SQLHelper._(); 
  static final SQLHelper instance = SQLHelper._();

  static sql.Database? _database;

  Future<sql.Database> get database async {
   if (_database != null) return _database!;
    _database = await db();
    return _database!;
  }


  Future<void> createTables(sql.Database database) async {
    await database.execute("""CREATE TABLE services(
      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      name TEXT,
      provider TEXT,
      location TEXT,
      radius INTEGER,
      phone TEXT,
      price INTEGER
    )""");
    print('Table "services" created successfully');

    await database.execute('''
            CREATE TABLE cached_requests(
              id INTEGER PRIMARY KEY,
              method TEXT,
              body TEXT,
              timestamp TEXT
            )
          ''').catchError((error) {
            // Log the error message to the console
            print('Error creating cached_requests table: $error');
          });
  }

  Future<sql.Database> db() async {

    try {
        final String path = join(await sql.getDatabasesPath(), 'bogdan.db');

    return await sql.openDatabase(
      path,
      version: 1,
      onCreate: (sql.Database database, int version) async{
        await createTables(database);
      }
    ); 
  }
  catch (e) {
    // Log the error message to the console
      print('Error initializing database: $e');
      rethrow;
  }
  }

  Future<void> insertServices(List<Service> services) async {
  for (var service in services) {
    try {
      await createItem(service.name, service.provider, service.location, service.radius, service.phone, service.price);
      print("Inserted service: ${service.id}");
    } catch (e) {
      if (e is DatabaseException && e.toString().contains('UNIQUE constraint failed')) {
        // Handle the unique constraint violation for this service
        print('Error inserting service (ID: ${service.id}): Unique constraint violation: Service.ID already exists in local DB');
      } else {
        // Log the error message to the console for other types of errors
        print('Error inserting service (ID: ${service.id}): $e');
      }
    }
  }
}

  Future<int> createItem(String name, String provider, String location, int radius, String phone, int price) async {
      try{
        final db = await database;

        final data = {'name':name, 'provider': provider, 'location': location, 'radius': radius, 'phone': phone, 'price': price};
        final id = await db.insert('services', data, conflictAlgorithm: sql.ConflictAlgorithm.replace);

        return id;
      }
      catch(e){
        // Log the error message to the console
      print('Error inserting service: $e');
      rethrow;
      }
  }

  Future<List<Map<String, dynamic>>> getServices() async{
    final db = await database;
    return await db.query('services', orderBy: "id");
  }

  Future<List<Map<String, dynamic>>> getItem(int id) async {
    final db = await database;
    return await db.query('services', where: "id = ?", whereArgs: [id], limit: 1);
  }

  Future<int> updateService(
    int id, String name, String provider, String location, String radius, String phone, String price) async{
        
        try{
        final db = await database;

        final data = {
          'name': name,
          'provider': provider,
          'location': location,
          'radius': radius,
          'phone': phone,
          'price': price
        };
        final result =
        await db.update('services', data, where: "id = ?", whereArgs: [id]);
        print('DATABASE Service: $data');
        return result;
    }
    catch (e){
      print('Error updating service: $e');
    
    rethrow; 
    }
    }
  
  Future<int> deleteService(int id) async{
    final db = await database;
    try{
      return await db.delete("services", where: "id = ?", whereArgs: [id]);
    }
    catch (e){
      debugPrint("Something went wrong with deleting the service: $e");
      rethrow;
    }
  }



    
  Future<void> clearLocalDatabase() async {
    try {
      final db = await database;
      await db.delete('services'); // Delete all records in the 'services' table
      print("Cleared local database");
    } catch (e) {
      // Log the error message to the console
      print('Error clearing local database: $e');
      rethrow;
    }
  }


 // Cache request when the device is offline
  Future<int> cacheRequest(String method, String body) async {
    try {
      final db = await database;
      final timestamp = DateTime.now().toUtc().toIso8601String();
      return await db.insert(
        'cached_requests',
        {'method': method,  'body': body, 'timestamp': timestamp},
      );
    } catch (e) {
      // Log the error message to the console
      print('Error caching request: $e');
      rethrow;
    }
  }

  // Get cached requests
  Future<List<Map<String, dynamic>>> getCachedRequests() async {
  try {
    final db = await database;

    // Check if the cached_requests table exists
    final isTableExists = await db
        .rawQuery('SELECT name FROM sqlite_master WHERE type="table" AND name="cached_requests"')
        .then((result) => result.isNotEmpty);

    if (!isTableExists) {
      print('The cached_requests table does not exist.');
      return [];
    }

    // Continue with the query if the table exists
    return await db.query('cached_requests');
  } catch (e) {
    // Log the error message to the console
    print('Error getting cached requests: $e');
    rethrow;
  }
}
  

  // Remove cached request after successfully sending to the server
  Future<int> removeCachedRequest(int id) async {
    try {
      final db = await database;
      return await db.delete(
        'cached_requests',
        where: 'id = ?',
        whereArgs: [id],
      );
    } catch (e) {
      // Log the error message to the console
      print('Error removing cached request: $e');
      rethrow;
    }
  }
  
}
