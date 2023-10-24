#pragma once
#include "repo.h"
#include "dynamicArray.h"
#include "bills.h"

class service{
private: repo& r;
public:
    service(repo& rep):r{rep}{};

    void add(TElem& elem);

    int remove(string& serial);

    bill& getElem(int pos){
        return r[pos];
    }

    int getSize(){
        return r.getSize();
    }

    int calculateTotal();



    string toString(bill& aux){
        string isPaidStr;
        if (aux.getIsPaid())
            isPaidStr="true";
        else
            isPaidStr="false";
        string str = "Serial NO: " + aux.getSerialNumber() + "   Company: " + aux.getCompany() + "   DueDate: " +
                to_string(aux.getDate().getDay()) + "." + to_string(aux.getDate().getMonth()) + "."
                + to_string(aux.getDate().getYear()) + "   Sum: " + to_string(aux.getSum()) + "   Paid: " + isPaidStr;

        return str;
    }
};
