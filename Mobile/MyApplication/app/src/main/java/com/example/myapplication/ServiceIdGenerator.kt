package com.example.myapplication

class ServiceIdGenerator {
    private var currentId: Long = 3

    fun generateUniqueId(): Long {
        return ++currentId
    }
}
