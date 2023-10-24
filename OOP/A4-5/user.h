#pragma once
#include "dynamicArray.h"
#include "ui.h"
#include "service.h"
#include "repo.h"
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

class user{
private:
    vector<movie> watchlist;
public:
    void add(movie& mov);
    int checkLink(std::string link);
    int getSize(){return watchlist.size();}

    int deleteMovieFromWatchlist(std::string& link);


    TElem& operator[](const int index) {return watchlist[index];}
};
