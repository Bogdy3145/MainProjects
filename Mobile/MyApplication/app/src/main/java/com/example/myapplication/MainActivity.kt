package com.example.myapplication

import Service
import ServiceViewModel
import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.result.ActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.myapplication.ui.theme.MyApplicationTheme

class MainActivity : ComponentActivity() {
    private lateinit var serviceViewModel: ServiceViewModel
    private lateinit var serviceAdapter: ServiceAdapter


    private val addServiceLauncher =
        registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result: ActivityResult ->
            if (result.resultCode == Activity.RESULT_OK) {
                val data: Intent? = result.data
                val newService = data?.getParcelableExtra<Service>("newService")
                if (newService != null) {
                    serviceViewModel.addService(newService)
                }
            }
        }

    private val editServiceLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result: ActivityResult ->
        if (result.data != null) {
            val data = result.data

            // Check if the result contains a Parcelable (Service)
            val updatedService = data?.getParcelableExtra<Service>("updatedService")
            if (updatedService != null) {
                // Handle the Service
                serviceViewModel.updateService(updatedService)
            } else {
                // Check if the result contains a number (ID)
                val deletedServiceId = data?.getLongExtra("deletedServiceId", -1)
                if (deletedServiceId?.toInt() != -1) {
                    // Handle the number (ID)
                    if (deletedServiceId != null) {
                        serviceViewModel.deleteService(deletedServiceId)
                    }

                    // Update the LiveData with the modified list
                }
            }
        }
    }






    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Initialize ViewModel
        serviceViewModel = ViewModelProvider(this).get(ServiceViewModel::class.java)

        //btn
        //val btnAdd = findViewById<Button>(R.id.btnAdd)
        val btnAdd = findViewById<ImageView>(R.id.ivImage)

        // Simulate data loading or add your actual data
        val initialServiceList = mutableListOf(
            Service(1,"1lol", "test", "cugir", 50, "0723", 30),
            Service(2,"test", "test", "cugir", 50, "0723", 30),
            Service(3,"rebo", "test", "cugir", 50, "0723", 30)
        )

        // Initialize RecyclerView and Adapter
        val rvServices = findViewById<RecyclerView>(R.id.rvServices)
        serviceAdapter = ServiceAdapter(initialServiceList)

        rvServices.adapter = serviceAdapter
        rvServices.layoutManager = LinearLayoutManager(this)

        // Observe the LiveData from the ViewModel
        serviceViewModel.getServices().observe(this, Observer { newServices ->
            serviceAdapter.setServices(newServices as MutableList<Service>)
            //Log.d("MainActivity", "Updated service list: $newServices")
        })

        serviceViewModel.updateServices(initialServiceList)

        btnAdd.setOnClickListener {
            // Handle the button click, e.g., navigate to another activity
            addServiceLauncher.launch(Intent(this, AddServiceActivity::class.java))
        }


        serviceAdapter.setOnItemClickListener(object : ServiceAdapter.OnItemClickListener {
            override fun onItemClick(service: Service) {
                // Create an intent to open EditServiceActivity
                val intent = Intent(this@MainActivity, EditServiceActivity::class.java)
                intent.putExtra("selectedService", service)
                editServiceLauncher.launch(intent)
            }
        })
    }
}

