#pragma once
#include "repo.h"
#include "domain.h"
#include <stdlib.h>
#include <assert.h>

#ifndef A3_4_BOGDY3145_SERVICE_H
#define A3_4_BOGDY3145_SERVICE_H

#endif //A3_4_BOGDY3145_SERVICE_H

typedef struct {
    Offer_Repo* repo;
    Dynamic_Array* undo_stack;
} Service;

Service* Create_Service(Offer_Repo* r, Dynamic_Array* u_s);

void Destroy_Service(Service* s);


int Add_Offer_Service(Service* s, Offer* o);
int Add_Offer_Service_Startup(Service* s, Offer* o);
int Delete_Offer_Service(Service* s, Address* o);
void Update_Offer_Service(Service* s, Address* o, char new_type[20], int new_price, int new_surface);

int Check_Offer_Availability(Service* s, Address* o);
int Search_Matching_Offers(Service* s, char* string, int a[]);
void Sort_Ascending_Order(Offer_Repo* ir, int limit, int* criteria(Offer*, Offer*));
int ascending_price(Offer* a, Offer* b);
int ascending_type(Offer* a, Offer* b);
int Greater_Surface(Offer_Repo* r, int surf, int limit, int* new_array);
int Search_Matching_Offers_Type(Service* s, char* string, int a[]);
void Copy_Repo(Offer_Repo* r1, Offer_Repo* r2, Service* s);


int Undo(Service* s);
int Redo(Service* s);










