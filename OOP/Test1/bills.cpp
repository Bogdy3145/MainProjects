
#include "bills.h"
#include <string>

bill::bill(string &serialNumber, string &company, date &date, double sum, bool isPaid) {
    this->serialNumber=serialNumber;
    this->company=company;
    this->dueDate=date;
    this->sum=sum;
    this->isPaid=isPaid;
}

date::date(int day, int month, int year) {
    this->day=day;
    this->month=month;
    this->year=year;

}
