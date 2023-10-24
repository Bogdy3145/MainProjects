package com.example.myapplication

import Service
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.RecyclerView

class ServiceAdapter (
    private var services: MutableList<Service>,
    private var itemClickListener: OnItemClickListener? = null

) :RecyclerView.Adapter<ServiceAdapter.ServiceViewHolder>() {

    class ServiceViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView){
        val titleTextView: TextView = itemView.findViewById(R.id.tvName)
        val location: TextView = itemView.findViewById(R.id.tvLocation)
        val price: TextView = itemView.findViewById(R.id.tvPrice)
        val provider: TextView = itemView.findViewById(R.id.tvProvider)

    }

    interface OnItemClickListener {
        fun onItemClick(service: Service)
    }

    fun setOnItemClickListener(listener: OnItemClickListener) {
        itemClickListener = listener
    }



    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ServiceViewHolder {
        return ServiceViewHolder(
            LayoutInflater.from(parent.context).inflate(
                R.layout.firstpage,
                parent,
                false
            )
        )
    }

    override fun getItemCount(): Int {
        return services.size
    }

    fun addService(service: Service) {
        services.add(service)
        notifyItemInserted(services.size -1)
    }


    override fun onBindViewHolder(holder: ServiceViewHolder, position: Int) {
        val curService = services[position]

        holder.itemView.apply {
            holder.titleTextView.text = curService.name
            holder.location.text = curService.location
            holder.price.text = curService.price.toString()
            holder.provider.text = curService.provider.toString()


        }
        holder.itemView.setOnClickListener {
            itemClickListener?.onItemClick(curService)
        }
    }

    fun setServices(newServices: MutableList<Service>) {
        services = newServices
        notifyDataSetChanged() // Notify the adapter of data change
    }


}