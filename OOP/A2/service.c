#include "service.h"
#include "repo.h"
#include "domain.h"
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include "dynamicArray.h"
#include <crtdbg.h>
#define _CRTDBG_MAP_ALLOC
#include "ui.h"

Service* Create_Service(Offer_Repo* r, Dynamic_Array* u_s){
    /**
     * Creates a service, allocating space for it, then passing the repo to it, to set up our working space.
     */

    Service* s = malloc(sizeof(Service));

    if (s==NULL)
        return 0;

    s->repo=r;
    s->undo_stack = u_s;

    return s;
}

void Destroy_Service(Service* s){

    /**
     * Destroys the Service, deallocating all the space for it and also for the repository inside of it.
     */

    if (s==NULL)
        return;

    Destroy_Repo(s->repo);
    Destroy_Dynamic_Array_Undo(s->undo_stack);
    free(s);
}

int Add_Offer_Service(Service* s, Offer* o){
    /**
     * Checks for validity of the offer. If it is not valid, first it destroys it to deallocate the space, then it returns 0
     * If the offer is valid, it continues and adds it to the repo.
     */
    //Offer_Repo* r=s->repo;
    for (int i=0;i<s->repo->array->size;i++){
        if (strcmp(Get_Address(s->repo->array->data[i])->street_name,o->address->street_name)==0 && Get_Address(s->repo->array->data[i])->street_no==o->address->street_no) {
            Delete_Offer(o);
            return 0;
        }
    }

    
    Offer_Repo* nr = Create_Repo(20);
    Copy_Repo(nr, s->repo, s);
    Add_Element_In_Array(s->undo_stack, nr);

       

    s->undo_stack->reminder = 0;
    //s->undo_stack->max++;


    Add_Offer(s->repo,o);

    
    
    



    return 1;
}

int Add_Offer_Service_Startup(Service* s, Offer* o) {
    /**
     * Same as normal add but it is for startup so it doesnt mess the undo stack
     */
     //Offer_Repo* r=s->repo;
    for (int i = 0; i < s->repo->array->size; i++) {
        if (strcmp(Get_Address(s->repo->array->data[i])->street_name, o->address->street_name) == 0 && Get_Address(s->repo->array->data[i])->street_no == o->address->street_no) {
            Delete_Offer(o);
            return 0;
        }
    }


    Add_Offer(s->repo, o);



    return 1;
}

int Delete_Offer_Service(Service* s, Address* o){
    /**
     * Deleting the offer based on it's address
     */
    for (int i=0;i<s->repo->array->size;i++){
        if (strcmp(Get_Address(s->repo->array->data[i])->street_name,o->street_name)==0 && Get_Address(s->repo->array->data[i])->street_no==o->street_no) {


            Offer_Repo* nr = Create_Repo(20);
            Copy_Repo(nr, s->repo,s);
            Add_Element_In_Array(s->undo_stack, nr);

            s->undo_stack->reminder = 0;



            Delete_Offer(s->repo->array->data[i]);
           
            Remove_Offer(s->repo,i);


            return 1;
        }
    }
    return 0;
}

void Update_Offer_Service(Service* s, Address* o, char new_type[20], int new_price, int new_surface){
    /**
     * Updates the type, price and surface fields of the offer, based on it's address
     *
     */
    for (int i=0;i<s->repo->array->size;i++){
        if (strcmp(Get_Address(s->repo->array->data[i])->street_name,o->street_name)==0 && Get_Address(s->repo->array->data[i])->street_no==o->street_no) {


            Offer_Repo* nr = Create_Repo(20);
            Copy_Repo(nr, s->repo,s);
            Add_Element_In_Array(s->undo_stack, nr);

            s->undo_stack->reminder = 0;



            Set_Type(s->repo->array->data[i],new_type);
            Set_Price(s->repo->array->data[i],new_price);
            Set_Surface(s->repo->array->data[i],new_surface);
        }
    }

}

int Check_Offer_Availability(Service* s, Address* o){
    /**
     * Checks if there exists an offer at the given address
     */
    for (int i=0;i<s->repo->array->size;i++){
        if (strcmp(Get_Address(s->repo->array->data[i])->street_name,o->street_name)==0 && Get_Address(s->repo->array->data[i])->street_no==o->street_no) {
            return 1;
        }
    }
    return 0;
}

int Search_Matching_Offers(Service* s, char* string, int a[]){
    /**
     * Searches all the offers that contain the string given as parameter into the field street_name of the address
     * and puts all the positions in which the offer is matched into the array a[], that will be sent back to the caller
     */
    int i;
    int k=-1;
    int string_int_maybe=0;

    string_int_maybe=atoi(string);


    for (i=0;i<s->repo->array->size;i++){
        if (string_int_maybe==0){

            if (strstr(Get_Address(s->repo->array->data[i])->street_name,string)!=0) {
                k++;
                a[k] = i;


            }
        }
        else{

            char aux[10];
            sprintf(aux,"%d", Get_Address(s->repo->array->data[i])->street_no);

            if (strstr(aux,string)!=0){
                k++;
                a[k] = i;

            }

        }
    }
    return k;

}

void Sort_Ascending_Order(Offer_Repo* ir, int limit, int* criteria(Offer*, Offer*)){
    /**
     * sorts the offers in order based on the criteria, which is a pointer to a function, limit being the size of the
     * array that is being sorted.
     *
     */
    Offer* aux;
    int ok=0,i;

    do {
        ok=1;
        for(i=0;i<limit;i++)
            if (criteria(ir->array->data[i],ir->array->data[i+1])){
                aux=ir->array->data[i];
                ir->array->data[i]=ir->array->data[i+1];
                ir->array->data[i+1]=aux;
                ok=0;
            }
    } while (ok==0);
}

int ascending_price(Offer* a, Offer* b){
    /**
     * function to be used as criteria for sorting
     */
    if (a->price>b->price)
        return 1;
    return 0;
}

int ascending_type(Offer* a, Offer* b){
    /**
     * function to be used as criteria for sorting
     */
    if(strcmp(a->type,b->type)>0)
        return 1;
    return 0;
}

int Greater_Surface(Offer_Repo* r, int surf, int limit, int* new_array) {
    /*
    * makes an array with the position of all the offers that have the surface greater than a given value and returns through k the lenght of this array
    */
    int i, k = -1;
    for (i = 0; i <=r->array->size-1; i++) {
        if (Get_Surface(r->array->data[i]) > surf) {
            k++;
            new_array[k] = i;
        }
    }
    return k;
}

 int Search_Matching_Offers_Type(Service* s, char* string, int a[]){
    /**
     * Searches all the offers that contain the string given as parameter into the field street_name of the address
     * and puts all the positions in which the offer is matched into the array a[], that will be sent back to the caller
     */
    int i;
    int k=-1;
    int string_int_maybe=0;

    //string_int_maybe=atoi(string);


    for (i=0;i<s->repo->array->size;i++){
        if (string_int_maybe==0){

            if (strstr(Get_Type(s->repo->array->data[i]),string)!=0) {
                k++;
                a[k] = i;


            }
        }

    }
    return k;

}

 void Copy_Repo(Offer_Repo* r1, Offer_Repo* r2, Service* s) {
     /**
     * r1- repository in which we copy
     * r2- repository to be copied
     */
     for (int i = 0;i < r2->array->size;i++) {
         Address* a = Create_Address(Get_Address(r2->array->data[i])->street_name, Get_Address(r2->array->data[i])->street_no);
         Offer* o = Create_Offer(Get_Type(r2->array->data[i]), a, Get_Surface(r2->array->data[i]), Get_Price(r2->array->data[i]));
         Add_Offer(r1, o);

     }


 }

int Undo(Service* s) {
    /*
    * we create a new repo before the undo, to also have in memory the last "intact" copy of our current repository, we copy it into to new repository made and we add the copy to the stack
    * then, we decrease the size, because the size just went up with this addition of the copy
    * we increase the reminder, which is an index for the redo stack, to know how many times we can redo (same amount of times we undo in a row)
    * we destroy the current repo and we add the repo that was added before the last one (because the last one is basically the one we destroyed)
    * and we decrease the size of the stack again (WHICH IS JUST AN INDEX FOR US)
    */
    if (s->undo_stack->size == 0)
        return 0;

    

    
    Offer_Repo* nr = Create_Repo(20);
    Copy_Repo(nr, s->repo, s);
    Add_Element_In_Array(s->undo_stack, nr);
    s->undo_stack->size--;
    
   

    
    s->undo_stack->reminder++;


     Destroy_Repo(s->repo);
     s->repo = Create_Repo(20);
     
     
     Copy_Repo(s->repo, s->undo_stack->data[(s->undo_stack->size)-1],s);
     
     s->undo_stack->size--;


     

     return 1;

 }

int Redo(Service* s) {
    /*
    * basically specification from undo, but in the reverse order
    * we copy the repo which is at index + 1 of our current position, then we move to that index
    */
    
    //printf("%d, %d\n", s->undo_stack->size, s->undo_stack->reminder);

    if (s->undo_stack->reminder<=0)
        return 0;

    Destroy_Repo(s->repo);
    Offer_Repo* new_repo = Create_Repo(20);
    s->repo = new_repo;

   

    Copy_Repo(s->repo, s->undo_stack->data[(s->undo_stack->size)+1],s);
    s->undo_stack->size++;
    s->undo_stack->reminder--;
    return 1;
    
   

}