#include "SetIterator.h"
#include "Set.h"
#include <exception>

using namespace std;

SetIterator::SetIterator(const Set& m) : set(m)
{
    this->current=0;
}
//Theta(1)


void SetIterator::first() {
    this->current=0;
}
//Theta(1)


void SetIterator::next() {
    if (this->current == this->set.length)
        throw exception();
    this->current++;
}
//Theta(1)

void SetIterator::previous() {
    if (this->current == -1)
        throw exception();
    this->current--;
}
//Theta(1)

TElem SetIterator::getCurrent()
{
    if (this->current == this->set.length or this->current == -1)
        throw exception();
    return this->set.elems[this->current];

}
//Theta(1)

bool SetIterator::valid() const {

    if (this->current < this->set.length and this->current > -1)
        return true;
    return false;
}
//Theta(1)





