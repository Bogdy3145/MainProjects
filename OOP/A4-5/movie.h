#pragma once
#ifndef A5_6_BOGDY3145_MOVIE_H
#define A5_6_BOGDY3145_MOVIE_H

#endif //A5_6_BOGDY3145_MOVIE_H
#include <string>
#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

class movie{
private:
    std::string title;
    std::string genre;
    int year_of_release;
    int nr_of_likes;
    std::string link;
public:
    movie() :title{" "},genre{" "},year_of_release{0},nr_of_likes{0},link{" "}{};
    movie(std::string& title, std::string& genre, int year_of_release, int nr_of_likes,
          std::string& link);

    std::string getTitle() const {return this->title;}
    std::string getGenre() const {return this->genre;}
    std::string getLink() const {return this->link;}
    int getYear() const {return this->year_of_release;}
    int getLikes() const {return this->nr_of_likes;}

    void setTitle(const std::string& Title) {title=Title;}
    void setGenre(const std::string& Genre) {genre=Genre;}
    void setLink(const std::string& Link) {link=Link;}
    void setLikes(const int likes) {nr_of_likes=likes;}
    void setYear(const int year) {year_of_release=year;}

    istream& operator >> (istream& is) // Do not make customer const, you want to write to it!
    {
        string line;
        std::getline(is, line); // getline from <string>
        is >> this->genre;
        is >> this->year_of_release;
        is >> this->nr_of_likes;
        is >> this->link;

        is.ignore(1024, '\n'); // after reading the loanAmount, skip the trailing '\n'
        is.ignore(1024, '\n'); // after reading the loanAmount, skip the trailing '\n'
        return is;
    }





};
