#include <string>
#include "bills.h"
#include "dynamicArray.h"
#include "service.h"
#include "repo.h"
#include "tests.h"

using namespace std;

void remove(service& s){
    cout << "Enter the serial no. of the object you want to remove.\n";
    string serial;
    cin >> serial;

    if (s.remove(serial)==1)
        cout << "Bill successfully removed! \n";
    else
        cout << "Bill couldn't be removed! \n";

}

void addEntry(service& s){
    string serialNumber="1ABC";
    string company="DIGI";
    int day=15;
    int month=07;
    int year=2003;
    date d(day,month,year);
    int sum=100;
    bool isPaid=false;

    bill aux(serialNumber,company,d,sum,isPaid);

    s.add(aux);

    string serialNumber1="1ABCDE";
    string company1="ANTENA";
    int day1=15;
    int month1=07;
    int year1=2003;
    date d1(day,month,year);
    int sum1=100;
    bool isPaid1=false;

    bill aux1(serialNumber1,company1,d1,sum1,isPaid1);

    s.add(aux1);

    string serialNumber2="2ABC";
    string company2="Prima";
    int day2=10;
    int month2=8;
    int year2=2003;
    date d2(day,month,year);
    int sum2=500;
    bool isPaid2=true;

    bill aux2(serialNumber2,company2,d2,sum2,isPaid2);

    s.add(aux2);

    string serialNumber3="1ABCDEFGH1";
    string company3="NTT";
    int day3=15;
    int month3=07;
    int year3=2020;
    date d3(day,month,year);
    int sum3=50;
    bool isPaid3=false;

    bill aux3(serialNumber3,company3,d3,sum3,isPaid3);

    s.add(aux3);

    string serialNumber4="10";
    string company4="Porsche";
    int day4=10;
    int month4=10;
    int year4=200;
    date d4(day,month,year);
    int sum4=100;
    bool isPaid4=true;

    bill aux4(serialNumber4,company4,d4,sum4,isPaid4);

    s.add(aux4);


}

void calculateTotal(service& s){
    cout << s.calculateTotal();
}

void listAll(service& s){

    for (int i = 0; i < s.getSize();i++){
        string str=s.toString(s.getElem(i));
        cout << str << "\n";
    }
}

void sort(service& s){

}

void start(){
    repo r;
    service s(r);

    addEntry(s);

    string x;
    cout << "Press something else than 0 to start! \n";

    cin >> x;
    while (x!="0"){
        if (x=="remove")
            remove(s);
        if (x=="list")
            listAll(s);
        if (x=="total")
            calculateTotal(s);
        if (x=="sort")
            sort(s);
        cout << "Back to menu! \n";
        cin >> x;
    }
}

int main(){
    testAll();
    start();
    return 0;
}
