
#include "repo.h"
#include "movie.h"
#include <vector>
#include <bits/stdc++.h>

void repo::add(movie &elem) {
    /**
     * just calls the predefined add from dynamic array
     */
    this->list.insert(list.end(),elem);
}

void repo::remove(const movie& elem) {
    /**
     * just calls the remove from dynamic array
     */
    int aux=-1;
    for (auto i:list){
        aux++;
        if(i.getLink()==elem.getLink()){
            break;
        }
    }
    auto it = list.begin()+aux;

    list.erase(it);

}

void repo::update(int index, std::string &title, std::string &genre, int year, int likes) {
    /**
     * updates the array at index "index" with the new fields passed as param
     */
    list[index].setTitle(title);
    list[index].setGenre(genre);
    list[index].setLikes(likes);
    list[index].setYear(year);
}

