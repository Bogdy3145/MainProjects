//
// Created by Bogdan on 3/2/2022.
//
#define _CRTDBG_MAP_ALLOC
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





void menu(){

    printf("%s","\n");
    printf("%s","\n");
    printf("%s","\n");

    printf("%s", "1. Add a real estate. \n");
    printf("%s", "2. Delete a real estate. \n");
    printf("%s", "3. Update a real estate. \n");
    printf("%s", "4. Display all real estates. \n");
    printf("%s", "5. Display all real estates that match your criteria. \n");
    printf("%s", "6. Display all real estates of a given type, having the surface greater than a given number. \n");
    printf("%s", "7. Display all real estates sorted ascending based on their type. \n");

    printf("%s", "0. Exit \n");


}

void Print_All_Offers(Service* s){

    int i;

    for (i = 0; i < s->repo->array->size; i++){
        char a_string[200];

        toString(s->repo->array->data[i],a_string);
        printf("%s",a_string);
    }

}

void print_custom_offers(Service* s, void* criteria){

    int i,limit=s->repo->array->size;
    int array_of_positions[50];

    if (criteria== ascending_price){
        char searching_string[10];
        printf("%s\n","Enter the street name or street no.");
        gets(searching_string);

        if (strcmp(searching_string,"-1")==0){
            limit = Search_Matching_Offers(s, "", array_of_positions);

        }
        else {
            limit = Search_Matching_Offers(s, searching_string, array_of_positions);

            if (limit == -1) {
                printf("%s\n", "There are no offers that match your search...");
                return;
            }
        }
    }
    else {

        limit = Search_Matching_Offers(s, "", array_of_positions);
    }

    Offer_Repo* ir = Create_Repo(20);



    for (i=0;i<=limit;i++){

        Address* a = Create_Address(Get_Street_name(s->repo->array->data[array_of_positions[i]]), Get_Street_no(s->repo->array->data[array_of_positions[i]]));
        Offer* o = Create_Offer(Get_Type(s->repo->array->data[array_of_positions[i]]), a, Get_Surface(s->repo->array->data[array_of_positions[i]]), Get_Price(s->repo->array->data[array_of_positions[i]]));
        Add_Offer(ir, o);
        

    }


    Sort_Ascending_Order(ir, limit, (int *(*)(Offer *, Offer *)) criteria);

    for (i=0;i<=limit;i++){
        char a_string[200];

        toString(ir->array->data[i],a_string);
        printf("%s",a_string);
    }

    Destroy_Repo(ir);

}

void print_given_type_with_surface(Service* s){
    printf("%s\n","Enter the type of the estate:");

    char type[20];
    gets(type);

    char surface[10];
    int surface_int;
    printf("%s\n","Enter the searched surface: ");

    scanf("%s",surface);
    surface_int=atoi(surface);

    if (surface_int==0){
        printf("%s\n","Something went wrong, you must enter a positive integer as surface!");
        return;
    }

    Offer_Repo* ir = Create_Repo(20);


    int array_of_positions[30],limit,i;

    limit = Search_Matching_Offers_Type(s,type,array_of_positions);

    for (i=0;i<=limit;i++){

        Address* a = Create_Address(Get_Street_name(s->repo->array->data[array_of_positions[i]]), Get_Street_no(s->repo->array->data[array_of_positions[i]]));
        Offer* o = Create_Offer(Get_Type(s->repo->array->data[array_of_positions[i]]), a, Get_Surface(s->repo->array->data[array_of_positions[i]]), Get_Price(s->repo->array->data[array_of_positions[i]]));
        Add_Offer(ir, o);
    }


    int new_limit = Greater_Surface(ir,surface_int,limit,array_of_positions);

    Destroy_Repo(ir);
    Offer_Repo* another_repo = Create_Repo(20);

    for (i=0;i<=new_limit;i++){
        Address* a = Create_Address(Get_Street_name(s->repo->array->data[array_of_positions[i]]), Get_Street_no(s->repo->array->data[array_of_positions[i]]));
        Offer* o = Create_Offer(Get_Type(s->repo->array->data[array_of_positions[i]]), a, Get_Surface(s->repo->array->data[array_of_positions[i]]), Get_Price(s->repo->array->data[array_of_positions[i]]));
        Add_Offer(ir, o);
    }

    for (i=0;i<=new_limit;i++){
        char a_string[200];

        toString(another_repo->array->data[i],a_string);
        printf("%s\n",a_string);
    }

    Destroy_Repo(another_repo);



}

void add_an_estate(Service* s){
    printf("%s\n","Enter the type of the estate:");

    char type[20];
    gets(type);
    printf("%s\n","Enter the street name: ");

    char street_name[100];

    scanf("%[a-z,A-Z,0-9,' ']",street_name);


    char street_no[10];
    int street_no_int;

    printf("%s\n","Enter the street number: ");
    char aux[2];
    gets(aux);
    scanf("%s",street_no);
    street_no_int=atoi(street_no);

    if (street_no_int==0){
        printf("%s\n","Something went wrong, you must enter a positive integer as street number!");
        return;
    }


    char surface[10],price[10];
    int surface_int,price_int;
    printf("%s\n","Enter the surface: ");

    scanf("%s",surface);
    surface_int=atoi(surface);

    if (surface_int==0){
        printf("%s\n","Something went wrong, you must enter a positive integer as surface!");
        return;
    }

    printf("%s\n","Enter the price: ");
    scanf("%s",price);
    price_int=atoi(price);

    if (price_int==0){
        printf("%s\n","Something went wrong, you must enter a positive integer as price!");
        return;
    }

    Address* a =Create_Address(street_name,street_no_int);
    Offer* o=Create_Offer(type,a,surface_int,price_int);

    if (Add_Offer_Service(s,o)==1)
        printf("%s\n","Offer successfully added!");
    else {
        printf("%s\n", "Failed to add this offer! Can't have 2 estates at the same address");
        //Delete_Offer(o);
    }
}

void delete_an_estate(Service* s){
    printf("%s\n","Enter the street name of the estate: ");
    char street_name[30];
    gets(street_name);

    printf("%s\n","Enter the street no. of the estate: ");
    char street_no[10];
    int street_no_int;

    scanf("%s",street_no);
    street_no_int=atoi(street_no);

    if (street_no_int==0){
        printf("%s\n","Something went wrong, you must enter a positive integer as street number!");
        return;
    }

    Address* a = Create_Address(street_name,street_no_int);

    int res=Delete_Offer_Service(s,a);
    if (res==0){
        printf("%s","Something went wrong, the address given does not exist among our estates!");
    }
    else{
        printf("%s","Offer successfully removed!");
    }

    Delete_Address(a);



}

void update_an_estate(Service* s){
    printf("%s\n","Enter the street name of the estate: ");
    char street_name[30];
    gets(street_name);

    printf("%s\n","Enter the street no. of the estate: ");
    char street_no[10];
    int street_no_int;

    scanf("%s",street_no);
    street_no_int=atoi(street_no);

    if (street_no_int==0){
        printf("%s\n","Something went wrong, you must enter a positive integer as street number!");
        return;
    }

    Address* a = Create_Address(street_name,street_no_int);

    int res=Check_Offer_Availability(s,a);

    if (res==0){
        printf("%s","Something went wrong, the address given does not exist among our estates!");
        Delete_Address(a);
        return;
    }



    char aux[2];
    gets(aux);

    printf("%s\n","Enter the new type of the estate:");

    char type[20];
    gets(type);

    char surface[10],price[10];
    int surface_int,price_int;
    printf("%s\n","Enter the new surface: ");

    scanf("%s",surface);
    surface_int=atoi(surface);

    if (surface_int==0){
        printf("%s\n","Something went wrong, you must enter a positive integer as surface!");
        return;
    }

    printf("%s\n","Enter the new price: ");
    scanf("%s",price);
    price_int=atoi(price);

    if (price_int==0){
        printf("%s\n","Something went wrong, you must enter a positive integer as price!");
        return;
    }

    Update_Offer_Service(s,a,type,price_int,surface_int);

    printf("%s\n","Offer updated successfully!");


}

void add_stuff(Service* s) {

    Address* a = Create_Address("victoriei", 1);
    Offer* o = Create_Offer("hotel", a, 10, 20);

    Add_Offer_Service_Startup(s, o);

    Address* a1 = Create_Address("arivabenne", 1);
    Offer* o1 = Create_Offer("tip", a1, 15, 23);

    Add_Offer_Service_Startup(s, o1);

    Address* a2 = Create_Address("paulista", 10);
    Offer* o2 = Create_Offer("hotel", a2, 15, 23);

    Add_Offer_Service_Startup(s, o2);

    Address* a3 = Create_Address("rozelor", 1);
    Offer* o3 = Create_Offer("tip", a3, 115, 230);

    Add_Offer_Service_Startup(s, o3);

    Address* a4 = Create_Address("victoriei", 2);
    Offer* o4 = Create_Offer("hotel", a4, 234, 12);

    Add_Offer_Service_Startup(s, o4);

    Address* a5 = Create_Address("canalului", 1);
    Offer* o5 = Create_Offer("pensiune", a5, 15, 23);

    Add_Offer_Service_Startup(s, o5);

    Address* a6 = Create_Address("rozelor", 25);
    Offer* o6 = Create_Offer("pensiune", a6, 105, 223);

    Add_Offer_Service_Startup(s, o6);

    Address* a7 = Create_Address("principala", 1);
    Offer* o7 = Create_Offer("hotel", a7, 195, 923);

    Add_Offer_Service_Startup(s, o7);

    Address* a8 = Create_Address("rozelor", 123);
    Offer* o8 = Create_Offer("tip", a8, 155, 253);

    Add_Offer_Service_Startup(s, o8);

    Address* a9 = Create_Address("xd", 1);
    Offer* o9 = Create_Offer("alo", a9, 15, 23);

    Add_Offer_Service_Startup(s, o9);

    Address* a10 = Create_Address("canalului", 1234);
    Offer* o10 = Create_Offer("tip", a10, 15, 23);

    Add_Offer_Service_Startup(s, o10);




}

void start(){

    int option=-1;

    Offer_Repo* r = Create_Repo(20);
    Dynamic_Array* u_s = Create_Dynamic_Array(20, &Destroy_Repo);
    Service* s = Create_Service(r,u_s);

    add_stuff(s);
   
    

    while (option!=0){
        menu();
        char aux[10];
        scanf("%d",&option);
        gets(aux);


        if (option==1){
            add_an_estate(s);
        }
        else if (option==2){
            delete_an_estate(s);
            }
        else if (option==3){
            update_an_estate(s);
        }
        else if (option==4){
            Print_All_Offers(s);
        }
        else if (option==5){
            print_custom_offers(s, ascending_price);
        }
        else if (option==6){
            print_given_type_with_surface(s);
        }
        else if (option==7){
            print_custom_offers(s, ascending_type);
        }
        else if (option == 8) {

            if (Undo(s) == 0)
                printf("%s\n", "Can't undo from here.");
        }
        else if (option == 9) {
            if (Redo(s) == 0)
                printf("%s\n", "Can't redo from here.");
        }

    }
    Destroy_Service(s);
    
    
    
}

int main(){
    
    Test_Dynamic_Array();
    Test_Address();
    Test_Offer();
    Test_Repo();
    Test_Service();

    


    start();
    _CrtDumpMemoryLeaks();



}

