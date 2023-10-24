//
// Created by Bogdan on 4/6/2022.
//

#include "service.h"

void service::add(TElem &elem) {
    r.add(elem);
}

int service::remove(string& serial) {
    /**
     * to remove a bill, we get the serial from the UI, we check if the serial exists between our bills and if it does,
     * we call the repo to remove it.
     * If it was successfully removed, we return 1. If it wasn't, we return 0.
     */
    bill aux;
    bool ok=false;
    for (int i = 0; i < r.getSize(); i++)
        if (r.getElem(i).getSerialNumber()==serial)
            {
            aux=r.getElem(i);
            ok=true;
            }
    if (ok==true) {
        r.remove(aux);
        return 1;
    }
    else return 0;
}

int service::calculateTotal() {
    /**
     * goes through all the elements  and with getSum(), takes the sum field of each object and adds it to the local sum
     * then it returns the local sum
     */
    int sum=0;
    for (int i = 0; i < this->getSize();i++){
        sum+=r.getElem(i).getSum();
    }
    return sum;

}