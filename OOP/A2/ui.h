#include "repo.h"
#include "service.h"
#pragma once
#ifndef A3_4_BOGDY3145_UI_H
#define A3_4_BOGDY3145_UI_H

#endif //A3_4_BOGDY3145_UI_H

void menu();
void start();
void Print_All_Offers(Service* s);
void add_an_estate(Service* s);
void delete_an_estate(Service* s);
void update_an_estate(Service* s);
void print_custom_offers(Service* s, void* criteria);
void print_given_type_with_surface(Service* s);
void add_stuff(Service* s);

