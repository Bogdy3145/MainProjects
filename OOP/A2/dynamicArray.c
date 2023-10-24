#include "dynamicArray.h"
#include <stdio.h>
#include <stdlib.h>
#include "domain.h"
#include <assert.h>
#include <crtdbg.h>
#define _CRTDBG_MAP_ALLOC


Dynamic_Array* Create_Dynamic_Array(int capacity, void(*Destroy_Function)(void*)){
    /*
    * Constructor for the dynamic array, checking for errors and if all is fine, allocating space for the array
    */

    Dynamic_Array* a = malloc(sizeof (Dynamic_Array));

    if (a==NULL)
        return NULL;

    a->size=0;
    a->reminder = 0;
    a->max = 0;

    a->capacity=capacity;
    a->Destroy_Function=Destroy_Function;

    a->data=malloc(sizeof(void*)*a->capacity);

    if (a->data == NULL) {
        free(a);
        return NULL;
    }

    return a;

}

void Resize(Dynamic_Array* arr){
    /*
    * resize the array using realloc
    */
    if (arr==NULL)
        return;

    arr->capacity*=2;

    void** aux = realloc(arr->data, arr->capacity * sizeof(void));

    if (aux==NULL)
        return;

    arr->data=aux;

}

void Destroy_Dynamic_Array(Dynamic_Array* a){
    /*
    * freeing the space that was allocated before for the array
    */
    if (a==NULL)
        return;

    if (a->data == NULL) {
        free(a);
        return;
    }
    printf("%d, %d\n", a->max, a->size);

    

    for (int i = 0; i < a->size; i++) {
        if (a->data[i]!=NULL)
            a->Destroy_Function(a->data[i]);
    }
    free(a->data);
    free(a);
}

void Destroy_Dynamic_Array_Undo(Dynamic_Array* a) {
    /*
    * freeing the space that was allocated before for the array
    */
    if (a == NULL)
        return;

    if (a->data == NULL) {
        free(a);
        return;
    }
    printf("%d, %d\n", a->max, a->size);



    for (int i = 0; i < a->max; i++) {
        if (a->data[i] != NULL)
            a->Destroy_Function(a->data[i]);
    }
    free(a->data);
    free(a);
}

int Add_Element_In_Array(Dynamic_Array* a, void* elem){
    /*
    * Adding an element into the array, also checking for maximum size of the array for a particular case
    */
    if (a==NULL || elem== NULL)
        return 0;

    if (a->size==a->capacity)
        Resize(a);

    a->data[a->size]=elem;
    a->size++;
    if (a->size > a->max)
        a->max = a->size;

    return 1;

}


