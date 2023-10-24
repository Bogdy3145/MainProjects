#include "domain.h"
#include "dynamicArray.h"
#include <stdlib.h>
#include <string.h>
#include <crtdbg.h>
#include <assert.h>
#include <stdio.h>
#define _CRTDBG_MAP_ALLOC

Offer* Create_Offer(char* type, Address* add, int surf, int price){

    /*
     * creating an offer and making sure of all the errors the program might encounter by freeing the allocated memory
     */

    if (type == NULL)
        return NULL;

    Offer* o =malloc(sizeof(Offer));

    if (o == NULL)
        return NULL;

    o->type = malloc(strlen(type)+1 * sizeof(char));

    if (o->type == NULL){
        free(o);
        return NULL;
        }

    strcpy(o->type,type);

    //o->address = malloc(sizeof(*add));
    
    o->address = add;

    if (o->address == NULL){
        free(o->type);
        free(o);
        return NULL;
    }

    o->address=add;

    o->surface = surf;

    o->price = price;

    return o;

}

void Delete_Offer(Offer* o){
    /*
     * Deleting the offer o, but first we deallocate the space used for the address and the type
     */

    if (o==NULL)
        return;
    Delete_Address(o->address);
    free(o->type);
    //free(o->address);
    free(o);
}

Address* Create_Address(char* street_name, int street_no){
    /*
     * Creating an Address with the given parameters and checking for errors
     */
    if (street_name == NULL)
        return NULL;

    Address* p = malloc(sizeof(Address));

    if (p==NULL)
        return NULL;

    p->street_name = malloc((strlen(street_name)+1)*sizeof(char));

    if (p->street_name == NULL){
        free(p);
        return NULL;
        }

    strcpy(p->street_name,street_name);

    p->street_no=street_no;

    return p;
}

void Delete_Address(Address* p){
    /*
     * Deleting the Address and freeing the space, first for the street_name, then for the whole address.
     */

    if (p==NULL)
        return;

    free(p->street_name);
    free(p);

}




void toString(Offer* o, char str[])
{
    if (o == NULL)
        return;

    sprintf(str, "This offer has a %s type, having a surface of %d sm and a price of %d euros, at address %s, %d \n"
            , o->type, o->surface, o->price, o->address->street_name, o->address->street_no);
}

Address* Get_Address (Offer* o){
    return o->address;
}

char* Get_Street_name(Offer* o) {
    return o->address->street_name;
}

int Get_Street_no(Offer* o) {
    return o->address->street_no;
}

int Get_Surface (Offer* o){
    return o->surface;
}

char* Get_Type (Offer* o){
    return o->type;
}

void Set_Type(Offer* o, char* new_type){
    strcpy(o->type,new_type);
}

void Set_Surface(Offer* o, int new_surface){
    o->surface=new_surface;
}

void Set_Price(Offer* o, int new_price){
    o->price=new_price;
}

int Get_Price(Offer* o) {
    return o->price;
}