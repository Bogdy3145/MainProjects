#pragma once
#ifndef A3_4_BOGDY3145_REPO_H
#define A3_4_BOGDY3145_REPO_H

#endif //A3_4_BOGDY3145_REPO_H

#include "domain.h"
#include "dynamicArray.h"

typedef struct {
    Dynamic_Array* array;
} Offer_Repo;


Offer_Repo* Create_Repo(int cap);

void Destroy_Repo(Offer_Repo* r);


int Add_Offer(Offer_Repo* repo, Offer* offer);
int Remove_Offer(Offer_Repo* r, int pos);
void Destroy_Repo_Without_Offers(Offer_Repo* r);



