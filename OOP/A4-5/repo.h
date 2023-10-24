#pragma once
#ifndef A5_6_BOGDY3145_REPO_H
#define A5_6_BOGDY3145_REPO_H

#endif //A5_6_BOGDY3145_REPO_H

#include "dynamicArray.h"
#include "movie.h"
#include <vector>

class repo{
private:
    vector<movie> list;

public:
    void add(movie& elem);
    void remove(const movie& elem);
    void update(int index, std::string& title, std::string& genre, int year, int likes);
    int getSize(){
        return list.size();
    }
    vector<movie>& getList(){
        return list;
    }

    TElem& operator[](int index) {return list[index];}



};
