#pragma once
#include <typeinfo>
#include <iomanip>
#include "movie.h"
#include <iostream>
#include <string>
#include "dynamicArray.h"
#ifndef A5_6_BOGDY3145_DYNAMICARRAY_H
#define A5_6_BOGDY3145_DYNAMICARRAY_H

#endif //A5_6_BOGDY3145_DYNAMICARRAY_H

typedef movie TElem;
using namespace std;

template <typename TElem> class DynamicVector {
private:
    TElem *elems;
    int size, capacity;

public:
    explicit DynamicVector(int Capacity=1){capacity=Capacity , size=0, elems=new TElem[capacity];}

    DynamicVector& operator=(const DynamicVector& v){
        if (this==&v)
            return *this;

        size=v.size;
        capacity=v.capacity;

        delete[] elems;
        elems = new TElem[capacity];
        for (int i = 0; i < size; i++){
            elems[i]=v.elems[i];
        }
        return *this;

    }
    TElem& operator[](const int index) {return elems[index];}


    void add(const TElem& elem){
        if(size==capacity)
            resize();
        elems[size++]=elem;
    }
    void resize(){
        capacity*=2;
        TElem* newElements = new TElem[capacity];

        for (int i = 0; i < size; i++)
            newElements[i]=elems[i];

        delete[] elems;
        elems=newElements;
    };

    void remove(const TElem& elem){
        bool ok=false;
        int i = 0;

        while(ok==false and size > 1 and i < size-1) {

            if (elems[i].getLink() == elem.getLink()) {
                if (size>1)
                    for (int j = i; j < size - 1; j++) {

                        elems[j] = elems[j + 1];
                        ok = true;
                    }

                }

            i++;
        }

        size--;
    }

    int getSize() const {return size;}
    ~DynamicVector(){delete[] elems;}
};


template <typename TElem>
DynamicVector<TElem>& operator+(DynamicVector<TElem>& list,const TElem& elem) {
    list.add(elem);
    return list;
}

template <typename TElem>
DynamicVector<TElem>& operator+(const TElem& elem, DynamicVector<TElem>& list) {
    list.add(elem);
    return list;
}
