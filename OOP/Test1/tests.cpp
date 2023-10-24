#include "tests.h"
#include <string>
#include "bills.h"
#include "dynamicArray.h"
#include "service.h"
#include "repo.h"
#include <assert.h>
void testRemove(){
    repo r;
    service s(r);
    bill aux;
    s.add(aux);
    assert(s.getSize()==1);

    assert(s.remove(s.getElem(0).getSerialNumber())==1);
    assert(s.getSize()==0);
    assert(s.remove(s.getElem(0).getSerialNumber())==0);
}

void testSum(){
    repo r;
    service s(r);

    assert(s.calculateTotal()==0);

    string serialNumber2="2ABC";
    string company2="Prima";
    int day2=10;
    int month2=8;
    int year2=2003;
    date d2(day2,month2,year2);
    int sum2=500;
    bool isPaid2=true;

    bill aux2(serialNumber2,company2,d2,sum2,isPaid2);

    s.add(aux2);

    string serialNumber3="1ABCDEFGH1";
    string company3="NTT";
    int day3=15;
    int month3=07;
    int year3=2020;
    date d3(day3,month3,year3);
    int sum3=50;
    bool isPaid3=false;

    bill aux3(serialNumber3,company3,d3,sum3,isPaid3);

    s.add(aux3);

    assert(s.calculateTotal()==550);
}

void testAll(){
    testRemove();
    testSum();
}