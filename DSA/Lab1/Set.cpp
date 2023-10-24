#include "Set.h"
#include "SetIterator.h"
#include <exception>

using namespace std;

Set::Set() {
    this->capacity=1;
    this->length=0;
    this->elems= new TElem[capacity];
}
//Theta(1)

bool Set::add(TElem elem) {

    if (this->length == this->capacity)
        resize();

    for (int i = 0; i < this->length; i++)
        if (this->elems[i]==elem)
            return false;

    this->elems[length]=elem;
    this->length++;

	return true;
}
//Best case: Theta(1)
// Worst case: Theta(this->length)
//Total complexity: O(this->length)

bool Set::remove(TElem elem) {



    for (int i = 0; i < this->length; i++){
        if (this->elems[i] == elem) {
            this->elems[i] = this->elems[this->length - 1];
            this->length--;
            return true;
        }
    }

    return false;

}
//Best case: Theta(1)
//Worst case: Theta(this->length)
//Total: O(n)

bool Set::search(TElem elem) const {

    for (int i = 0; i < this->length; i++){
        if (this->elems[i] == elem)
            return true;
    }

	return false;
}

//Best case: Theta(1)
//Worst case: Theta(n)
//


int Set::size() const {
	return this->length;

}
//Theta(1)


bool Set::isEmpty() const {
	if (this->length==0) return true;
	return false;
}
//Theta(1)

Set::~Set() {
    delete[] this->elems;
}
//Theta(1)

SetIterator Set::iterator() const {
	return SetIterator(*this);
}
//Theta(1)


void Set::resize(){
    int oldcap = this->capacity;
    this->capacity = this->capacity * 2;

    TElem* temp = new TElem[this->capacity];

    for (int i = 0; i < this->length; i++)
        temp[i]=this->elems[i];

    delete[] this->elems;

    this->elems=temp;
}
//Theta(this->length)



