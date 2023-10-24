#pragma once

#ifndef A3_4_BOGDY3145_DYNAMICARRAY_H
#define A3_4_BOGDY3145_DYNAMICARRAY_H

#endif //A3_4_BOGDY3145_DYNAMICARRAY_H


typedef struct {
    int size;
    int capacity;
    int reminder;
    int max;
    void** data;
    void (*Destroy_Function)(void*);
} Dynamic_Array;


Dynamic_Array* Create_Dynamic_Array(int capacity, void(*Destroy_Function)(void*));

void Destroy_Dynamic_Array(Dynamic_Array* a);
void Destroy_Dynamic_Array_Undo(Dynamic_Array* a);

int Add_Element_In_Array(Dynamic_Array* a, void* elem);

