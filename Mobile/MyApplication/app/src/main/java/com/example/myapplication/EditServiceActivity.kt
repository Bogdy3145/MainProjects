package com.example.myapplication

import Service
import ServiceViewModel
import android.app.AlertDialog
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.activity.ComponentActivity
import androidx.activity.result.contract.ActivityResultContracts
import androidx.lifecycle.ViewModelProvider
import android.util.Log
import android.content.Intent
import android.widget.ImageView
import androidx.activity.result.ActivityResult
import androidx.activity.result.ActivityResultLauncher

class EditServiceActivity : ComponentActivity() {
    private lateinit var serviceViewModel: ServiceViewModel
    private lateinit var editServiceLauncher: ActivityResultLauncher<Intent>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.updatepage)

        val requestCodeDelete = 123
        val requestCodeEdit = 456

        serviceViewModel = ViewModelProvider(this).get(ServiceViewModel::class.java)

        // Initialize views
        val etId = findViewById<EditText>(R.id.etId)
        val etName = findViewById<EditText>(R.id.etName)
        val etProvider = findViewById<EditText>(R.id.etProvider)
        val etLocation = findViewById<EditText>(R.id.etLocation)
        val etRadius = findViewById<EditText>(R.id.etRadius)
        val etPhone = findViewById<EditText>(R.id.etPhone)
        val etPrice = findViewById<EditText>(R.id.etPrice)

        val btnSubmitChanges = findViewById<ImageView>(R.id.ivImageSave)

        // Receive selected item's details from the previous activity
        val selectedService = intent.getParcelableExtra<Service>("selectedService")

        // Populate the EditText views with the details
        etId.setText(selectedService?.id.toString())
        etName.setText(selectedService?.name)
        etProvider.setText(selectedService?.provider)
        etLocation.setText(selectedService?.location)
        etRadius.setText(selectedService?.radius.toString())
        etPhone.setText(selectedService?.phone)
        etPrice.setText(selectedService?.price.toString())

        // Initialize the Activity Result Launcher for updating the item
        editServiceLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result: ActivityResult ->
            if (result.resultCode == RESULT_OK) {
                // Handle the result if needed
                val data: Intent? = result.data
                // Extract any data you need from the result
            }
        }

        // Handle the "Submit Changes" button click
        btnSubmitChanges.setOnClickListener {
            // Create a new Service object with the updated details
            val updatedService = Service(
                etId.text.toString().toLong(),
                etName.text.toString(),
                etProvider.text.toString(),
                etLocation.text.toString(),
                etRadius.text.toString().toInt(),
                etPhone.text.toString(),
                etPrice.text.toString().toInt(),
                //selectedService?.imageResId ?: R.drawable.corgi
            )


            // Pass the updated Service object to the previous activity
            val intent = Intent()
            intent.putExtra("updatedService", updatedService)
            setResult(RESULT_OK, intent)
            finish()
        }

        val btnDelete = findViewById<ImageView>(R.id.ivImageDelete)

        btnDelete.setOnClickListener {
            // Show a confirmation dialog
            val dialogBuilder = AlertDialog.Builder(this)
            dialogBuilder.setMessage("Are you sure you want to delete this service?")
                .setCancelable(false)
                .setPositiveButton("Yes") { _, _ ->
                    // Delete the service from your data source (e.g., ViewModel)
                    val intent = Intent()
                    intent.putExtra("deletedServiceId", etId.text.toString().toLong())
                    setResult(RESULT_OK, intent)
                    finish()
                    // Navigate back to the previous screen (e.g., MainActivity)

                }
                .setNegativeButton("No") { dialog, _ ->
                    dialog.dismiss()
                }

            val alertDialog = dialogBuilder.create()
            alertDialog.show()
        }


    }
}
