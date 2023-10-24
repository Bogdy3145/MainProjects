#pragma once
#ifndef A3_4_BOGDY3145_DOMAIN_H
#define A3_4_BOGDY3145_DOMAIN_H

#endif //A3_4_BOGDY3145_DOMAIN_H

typedef struct {

    char* street_name;
    int street_no;
} Address;

typedef struct {

    char* type;
    Address* address;
    int surface;
    int price;


} Offer;



Offer* Create_Offer(char* type, Address* add, int surf, int price);

void Delete_Offer(Offer* o);

Address* Create_Address(char* street_name, int street_no);

void Delete_Address(Address* p);


void toString(Offer* o, char str[]);
Address* Get_Address (Offer* o);

char* Get_Street_name(Offer* o);


int Get_Street_no(Offer* o);

void Set_Price(Offer* o, int new_price);
void Set_Surface(Offer* o, int new_surface);
void Set_Type(Offer* o, char* new_type);
int Get_Surface (Offer* o);
char* Get_Type (Offer* o);
int Get_Price(Offer* o);

