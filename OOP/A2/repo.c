#include "repo.h"
#include "domain.h"
#include <stdlib.h>
#include <assert.h>
#include "dynamicArray.h"
#include <string.h>
#include <stdio.h>
#include <crtdbg.h>
#define _CRTDBG_MAP_ALLOC

Offer_Repo* Create_Repo(int cap){
    /*
     * creating the repo, allocating space for cap * sizeof(offers)
     */
    Offer_Repo* r = malloc(sizeof(Offer_Repo));

    if (r==NULL)
        return NULL;

    r->array = Create_Dynamic_Array(cap,&Delete_Offer);


    if (r->array == NULL) {
        free(r);
        return NULL;
        }

    return r;

}

void Destroy_Repo(Offer_Repo* r){
    /*
     * destroying the repo, freeing the memory, frist of the data inside, then the whole repo
     */
    if (r==NULL)
        return;

    if (r->array==NULL){
        free(r);
        return;
    }

    Destroy_Dynamic_Array(r->array);

    //free(r->array);
    free(r);

}

void Destroy_Repo_Without_Offers(Offer_Repo* r){
    /*
     * destroying only the repo, without the offers inside
     * this will help us when we want to use auxiliary repos
     */
    if (r==NULL)
        return;

    if (r->array==NULL){
        free(r);
        return;
    }

    free(r->array);
    free(r);

}




int Add_Offer(Offer_Repo* r, Offer* o){

    if(Add_Element_In_Array(r->array,o)==1)
        return 1;


    return 0;
}

int Remove_Offer(Offer_Repo* r, int pos){
    /*
    * removes the offer from the repository
    */
    int i;

    
    for (i=pos;i<r->array->size-1;i++){

       r->array->data[i]=r->array->data[i+1];
    }
    r->array->size--;
    return 1;

}


