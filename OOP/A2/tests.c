//
// Created by Bogdan on 3/14/2022.
//
#include <stdio.h>
#include "ui.h"
#include <stdlib.h>
#include "domain.h"
#include "repo.h"
#include "service.h"
#include <crtdbg.h>
#include <string.h>
#include "dynamicArray.h"
#include "tests.h"
#include <crtdbg.h>
#define _CRTDBG_MAP_ALLOC

void Test_Offer(){

    Address* a = Create_Address("mamata",12);

    Offer* o = Create_Offer("hostel",a,15,20);

    assert (o!=NULL);

    Delete_Offer(o);


}

void Test_Address(){

    Address* a = Create_Address("mamata",12);

    assert (a!=NULL);

    Delete_Address(a);

    //assert (a==NULL);
}

void Test_Dynamic_Array(){
    Dynamic_Array* arr = Create_Dynamic_Array(20,&Delete_Offer);
    char a_string[100];
    assert(arr!=NULL);
    Address* a = Create_Address("mama",1);
    Offer* o = Create_Offer("tip",a,10,20);

    Add_Element_In_Array(arr,o);

    
    Destroy_Dynamic_Array(arr);



}
void Test_Repo(){

    Offer_Repo* r = Create_Repo(10);

    assert(r!=NULL);

    Address* a = Create_Address("mama", 1);
    Offer* o = Create_Offer("tip", a, 10, 20);

    Add_Offer(r, o);

    assert(r->array->size == 1);

    Delete_Offer(o);
    Remove_Offer(r, 1);
    
    assert(r->array->size == 0);

    

    Destroy_Repo(r);

}

void Test_Service() {   

    Offer_Repo* r = Create_Repo(20);
    Dynamic_Array* u_s = Create_Dynamic_Array(20, &Destroy_Repo);

    Service* s = Create_Service(r,u_s);

    assert(s != NULL);

    Address* a = Create_Address("mama", 1);
    Offer* o = Create_Offer("tip", a, 10, 20);

    Add_Offer_Service(s, o);

    assert(s->repo->array->size == 1);

    Update_Offer_Service(s, Get_Address(s->repo->array->data[0]), "new", 20, 30);

    assert(Get_Price(s->repo->array->data[0]) == 20);
    assert(Get_Surface(s->repo->array->data[0]) == 30);

    assert(Check_Offer_Availability(s, Get_Address(s->repo->array->data[0])), 1);

    int k[5];
    assert(Search_Matching_Offers(s, "alalal", k), 1);

    
    
    Delete_Offer_Service(s, Get_Address(s->repo->array->data[0]));
    assert(s->repo->array->size == 0);

    



    Destroy_Service(s);

}

