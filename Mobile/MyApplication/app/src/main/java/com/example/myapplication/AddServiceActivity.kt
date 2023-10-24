package com.example.myapplication

import Service
import ServiceViewModel
import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.result.ActivityResult
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider

class AddServiceActivity : ComponentActivity() {
    private lateinit var serviceViewModel: ServiceViewModel

    val idGenerator = ServiceIdGenerator()

    // Creating a new Service with an auto-incremented ID


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.addpage)

        serviceViewModel = ViewModelProvider(this).get(ServiceViewModel::class.java)




        val btnSubmit = findViewById<Button>(R.id.btnSubmit)

        btnSubmit.setOnClickListener {
            // Retrieve data from EditText fields
            val name = findViewById<EditText>(R.id.etName).text.toString()
            val provider = findViewById<EditText>(R.id.etProvider).text.toString()
            val location = findViewById<EditText>(R.id.etLocation).text.toString()
            val radius = findViewById<EditText>(R.id.etRadius).text.toString()
            val phone = findViewById<EditText>(R.id.etPhone).text.toString()
            val price = findViewById<EditText>(R.id.etPrice).text.toString()

            if (name.isEmpty() || provider.isEmpty() || location.isEmpty() || radius.isEmpty() || phone.isEmpty() || price.isEmpty()) {
                // Show an error message with a Toast
                Toast.makeText(this, "Please fill in all fields", Toast.LENGTH_SHORT).show()
            }
            else {

                // Create a new Service object
                val newService = Service(
                    idGenerator.generateUniqueId(),
                    name,
                    provider,
                    location,
                    radius.toInt(),
                    phone,
                    price.toInt(),
                    //R.drawable.reb
                );

                Log.d("AddServiceActivity", "New Service: $newService")


                // Add the new Service to your RecyclerView through your ViewModel
                //serviceViewModel.addService(newService)

                // Optionally, clear the EditText fields after submission
                clearEditTextFields()

                val intent = Intent()
                intent.putExtra("newService", newService)
                setResult(Activity.RESULT_OK, intent)
                finish()
            }
        }
    }

    private fun clearEditTextFields() {
        val editTextIds = arrayOf(R.id.etName, R.id.etProvider, R.id.etLocation, R.id.etRadius, R.id.etPhone, R.id.etPrice)
        for (editTextId in editTextIds) {
            findViewById<EditText>(editTextId).text.clear()
        }
    }

}
