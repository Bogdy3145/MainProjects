import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../model/Service.dart';

class DatabaseService {
  DatabaseService._(); 
  static final DatabaseService instance = DatabaseService._();

  static Database? _database;

  Future<Database> get database async {
   
   if (_database != null) return _database!;
    _database = await initDatabase();
    return _database!;
  }

Future<void> resetDatabase() async {
  try {
    // Get the path to the database file
    final String path = join(await getDatabasesPath(), 'services.db');

    // Delete the existing database file
    await deleteDatabase(path);
    print("Database deleted successfully");

    // Reinitialize the database
    _database = null; // Reset the _database variable
    await initDatabase();
    print("Database reinitialized successfully");
  } catch (e) {
    // Log the error message to the console
    print('Error resetting database: $e');
    rethrow;
  }
}


  Future<void> deleteServicesTable() async {
    try {
      final db = await database;
      await db.execute('DROP TABLE IF EXISTS services');
      print("Services table deleted successfully");
    } catch (e) {
      print('Error deleting services table: $e');
      rethrow;
    }
  }


  Future<Database> initDatabase() async {
    try {

      final String path = join(await getDatabasesPath(), 'services.db');
      

      return await openDatabase(
        path,
        version: 1,
        onCreate: (db, version) async {
          await db.execute('''
          CREATE TABLE services(
            id INTEGER PRIMARY KEY,
            name TEXT,
            provider TEXT,
            location TEXT,
            radius INTEGER,
            phone TEXT,
            price INTEGER
          )
        ''').catchError((error){
          print('Error first : $error');
        });

        print("CREAETING");

          await db.execute('''
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
        },
      );
    } catch (e) {
      // Log the error message to the console
      print('Error initializing database: $e');
      rethrow;
    }
  }
  
Future<void> insertServices(List<Service> services) async {
  for (var service in services) {
    try {
      await insertService(service);
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

  Future<int> insertService(Service service) async {
  try {
    final db = await database;
    return await db.insert('services', service.toMap());

  } catch (e) {
  
    // Log the error message to the console
    print('Error inserting service: $e');
    return 999;
  }
}

  Future<List<Service>> getServices() async {
    final db = await database;
    final List<Map<String, dynamic>> maps = await db.query('services');
    return List.generate(maps.length, (i) {
      return Service.fromMap(maps[i]);
    });
  }

Future<bool> verifyAlreadyExisting(int id) async {
    try {
      final db = await database;
      final count = Sqflite.firstIntValue(await db.rawQuery('SELECT COUNT(*) FROM services WHERE id = ?', [id]));

    
      if(count !=null)
        {
          if(count > 0)
            return true;
          else
            return false;
          }
      else
        return false;
    } catch (e) {
     
      print('Error verifying existing recipe: $e');
      rethrow;
    }
  }

  Future<int> updateService(Service service) async {
  try {
    final db = await database;
    return await db.update(
      'services',
      service.toMap(),
      where: 'id = ?',
      whereArgs: [service.id],
    );
  } catch (e) {
    // Log the error message to the console
    print('Error updating service: $e');
    
    rethrow; 
  }
}
  

  Future<int> deleteService(int id) async {
  try {
    final db = await database;
    return await db.delete(
      'services',
      where: 'id = ?',
      whereArgs: [id],
    );
  } catch (e) {
    // Log the error message to the console
    print('Error deleting service: $e');
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
