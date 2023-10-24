#include <exception>

#include "IndexedList.h"
//#include "ListIterator.h"
#include <iostream>

using namespace std;

struct IndexedList::DLLNode{
    TElem info;
    PNode next;
    PNode prev;
    DLLNode(TElem e, PNode n, PNode p);
};
//Theta(1)

IndexedList::DLLNode::DLLNode(TElem e, PNode n, PNode p) {
    info=e;
    next=n;
    prev=p;
}
//Theta(1)

IndexedList::IndexedList() {
    head= nullptr;
}
//Theta(1)

int IndexedList::size() const {
    int counter=0;
    PNode aux;
    aux=head;
    while (aux!= nullptr){
        aux=aux->next;
        counter++;
    }
    //cout << counter;
    return counter;

}
//Bestcase Theta(1)
//Worstcase Theta(length)
//Avgcase O(length)


bool IndexedList::isEmpty() const {
    if (head== nullptr)
        return true;
	return false;
}
//Theta(1)

TElem IndexedList::getElement(int pos) const {
    PNode aux;
    int counter=0;

    if (pos>=size())
        throw std::exception();
    aux=head;
    while (aux!= nullptr){
        if (counter==pos)
            return aux->info;
        aux=aux->next;
        counter++;
    }
    if (counter==pos)
        return aux->info;

    return NULL_TELEM;
}
//Bestcase Theta(1)
//Worstcase Theta(length)
//Avgcase O(length)

TElem IndexedList::setElement(int pos, TElem e) {
    PNode aux;
    int counter=0;
    aux=head;

    if (pos>=size() or pos <0)
        throw std::exception();

    while (aux!= nullptr){
        if (counter==pos){
            TElem oldInfo;
            oldInfo=aux->info;
            aux->info=e;
            return oldInfo;
        }
        aux=aux->next;
        counter++;
    }
    if (counter==pos){
        TElem oldInfo;
        oldInfo=aux->info;
        aux->info=e;
        return oldInfo;
    }

    return NULL_TELEM;
}
//Bestcase Theta(1)
//Worstcase Theta(length)
//Avgcase O(length)

void IndexedList::addToEnd(TElem e) {
    PNode aux,reminder;
    aux=head;

    if (aux== nullptr) {
        PNode newNode;
        newNode = new DLLNode(e, nullptr,aux);
        //newNode->next=head;
        head=newNode;

        return;
    }

    while (aux!= nullptr){
        reminder=aux;
        aux=aux->next;
    }

    PNode newNode;
    newNode = new DLLNode(e, nullptr,aux);

    reminder->next = newNode;
    newNode->prev=reminder;

}
//Avgcase Theta(length)

void IndexedList::addToPosition(int pos, TElem e) {
    PNode aux;
    aux=head;
    int counter=0;

    if (pos >= size())
        throw std::exception();

    if (aux == nullptr){
        PNode newNode;
        newNode = new DLLNode(e, nullptr,aux);
        //newNode->next=head;
        head=newNode;

        return;
    }

    while (aux->next != nullptr){
        if (counter==pos){
            PNode newNode;
            newNode = new DLLNode(e, nullptr,aux);
            newNode->next=aux;
            newNode->prev=aux->prev;
            if (aux->prev == nullptr){
                head=newNode;
                aux->prev=head;
            }
            else{
                aux->prev->next = newNode;
                aux->prev=newNode;
            }

            //aux->next=newNode;
        }
        aux=aux->next;
        counter++;
    }
    if (counter==pos){
        PNode newNode;
        newNode = new DLLNode(e, nullptr,aux);

        newNode->next=aux;
        newNode->prev=aux->prev;
        if (aux==head) {
            head = newNode;
            aux->prev=head;

        }
        else {
//        if (aux->next != nullptr)
//            aux->next->prev=newNode;
            aux->prev->next = newNode;
            aux->prev = newNode;
        }
    }
}
//Theta(length)

TElem IndexedList::remove(int pos) {
    PNode aux;
    aux=head;
    int counter=0;

    if (pos >= size())
        throw std::exception();

    while (aux->next != nullptr){
        if (counter==pos){
            TElem oldEl;
            oldEl=aux->info;
            if (aux->prev== nullptr) {
                head = aux->next;
                head->prev = nullptr;
            }
            else {
                aux->prev->next = aux->next;
                aux->next->prev=aux->prev;
            }
            return oldEl;
        }
        aux=aux->next;
        counter++;
    }
    if (counter==pos){
        TElem oldEl;
        oldEl=aux->info;
        if (aux->prev== nullptr) {
            head = aux->next;
            //head->prev = nullptr;
        }
        else {
            aux->prev->next = aux->next;
//            if (aux->next!= nullptr)
//                aux->next->prev=aux->prev;
        }
        return oldEl;
    }

	return NULL_TELEM;
}
//Bestcase Theta(1)
//Worstcase Theta(length)
//Avgcase O(length)

int IndexedList::search(TElem e) const{
    PNode aux;
    aux=head;
    int counter=0;

    while (aux != nullptr){
        if (aux->info==e){
            return counter;
        }
        aux=aux->next;
        counter++;
    }

    return -1;
}
//Bestcase Theta(1)
//Worstcase Theta(length)
//Avgcase O(length)

ListIterator IndexedList::iterator() const {
    return ListIterator(*this);        
}
//Theta(1)

IndexedList::~IndexedList() {
    while (head != nullptr) {
        PNode p = head;
        head = head->next;
        delete p;
    }
}
//Theta(length)


int IndexedList::lastIndexOf(TElem elem) const {
    PNode aux;
    aux=head;
    int reminder=-1,count=0;

    while (aux!= nullptr){
        if (aux->info==elem)
            reminder=count;
        count++;
        aux=aux->next;
    }
    return reminder;
}
//Theta(length)





ListIterator::ListIterator(const IndexedList& list) : list(list){
    currentElement=list.head;
}

void ListIterator::first(){
    currentElement=list.head;


}

void ListIterator::next(){
    if (currentElement == nullptr)
        throw std::exception();
    currentElement=currentElement->next;

}

bool ListIterator::valid() const{
    if (currentElement!= nullptr)
        return true;
    return false;
}

TElem ListIterator::getCurrent() const{
    if (currentElement == nullptr)
        throw std::exception();
    return currentElement->info;
    //return NULL_TELEM;
}