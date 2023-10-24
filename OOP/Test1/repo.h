#pragma once
#include "bills.h"
#include "dynamicArray.h"
class repo{
private:
    DynamicVector<bill> repo;
public:
    void add(TElem& elem);
    void remove(TElem& elem);


    bill& getElem(int pos){
        return repo[pos];
    }



    int getSize(){return repo.getSize();}
    TElem& operator[](int index) {return repo[index];}

};