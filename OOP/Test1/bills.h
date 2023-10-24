#pragma once
#include <string>
#include <iostream>

using namespace std;

class date{
private:
    int day;
    int month;
    int year;
public:
    date(int day, int month, int year);

    date():day{0},month{0},year{0}{};

    int getDay(){return day;}
    int getMonth(){return month;}
    int getYear(){return year;}
};

class bill{
private:
    string serialNumber;
    string company;
    date dueDate;
    double sum;
    bool isPaid;
public:

    bill():serialNumber{""},company{""}, dueDate(), sum{0},isPaid{false}{};
    bill(string& serialNumber, string& company, date& date, double sum, bool isPaid);

    string& getSerialNumber(){return this->serialNumber;}
    string& getCompany(){return this->company;}
    date& getDate(){return this->dueDate;}
    double getSum(){return this->sum;}
    bool getIsPaid(){return this->isPaid;}

};

