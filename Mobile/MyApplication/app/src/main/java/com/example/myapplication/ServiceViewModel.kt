import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import Service

class ServiceViewModel : ViewModel() {
    private val serviceList: MutableLiveData<MutableList<Service>> = MutableLiveData(mutableListOf()) // Initialize with an empty list

    // Public method to access the LiveData
    fun getServices(): LiveData<MutableList<Service>> {
        return serviceList
    }

//    init {
//        // Initialize the list with an empty MutableList
//        serviceList.value = mutableListOf()
//    }

    fun addService(service: Service) {
        Log.d("ServiceViewModel", "FIRST service list: ${serviceList.value}")

        val currentServices = serviceList.value ?: mutableListOf()
        currentServices.add(service)
        serviceList.postValue(currentServices)
        Log.d("ServiceViewModel", "Updated service list: ${currentServices}")
    }


    // Public method to update the service list
    fun updateServices(newServices: MutableList<Service>) {

        serviceList.value = newServices


    }

    fun updateService(updatedService: Service) {
        // Get the current list of services
        val currentServices = serviceList.value ?: mutableListOf()

        Log.d("EDIT", "servs: $currentServices")
        // Find the position of the service to update (you may need a unique identifier in your Service class)
        val serviceToUpdate = currentServices.indexOfFirst { it.id == updatedService.id }
        Log.d("EDIT", "New Service: $serviceToUpdate")

        if (serviceToUpdate != -1) {
            Log.d("EDIT", "TEST: $serviceToUpdate")

            // Update the service in the list
            currentServices[serviceToUpdate] = updatedService

            // Update the LiveData to notify observers of the change
            serviceList.value = currentServices
        }
    }

    fun deleteService(etId: Long) {
        val currentServices = serviceList.value ?: mutableListOf()
        Log.d("test","test,${serviceList.value}")

        // Find the position of the service to update (you may need a unique identifier in your Service class)
        val serviceToDeleteIndex = currentServices.indexOfFirst { it.id == etId }
        Log.d("DELETE", "index: $etId")
        Log.d("ALL", "index: $currentServices")

        if (serviceToDeleteIndex != -1) {
            // Remove the service from the list
            currentServices.removeAt(serviceToDeleteIndex)

            // Update the LiveData with the modified list
            serviceList.postValue(currentServices)
            Log.d("DELETE", "all: $serviceList")
        }
    }

}
