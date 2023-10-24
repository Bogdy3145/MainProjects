#pragma once
#ifndef A5_6_BOGDY3145_SERVICE_H
#define A5_6_BOGDY3145_SERVICE_H

#endif //A5_6_BOGDY3145_SERVICE_H

#include "repo.h"
#include "movie.h"
#include "user.h"

class service{
private: repo& r;
public:
    explicit service(repo& rep):r{rep}{};
    void add(std::string title, std::string genre, int year, int likes, std::string link);
    int getSize(){
        return r.getSize();
    }
    movie& getElement(int i){
        return r[i];

    }

    std::string to_string(movie m){
        std::string str = "TITLE: " + m.getTitle() + "    GENRE: " + m.getGenre() + "    YEAR: " + std::to_string(m.getYear()) + "    LIKES: " +
                std::to_string(m.getLikes()) + "     LINK: " + m.getLink();
        return str;
    }

    void removeMovie(std::string& str);

    int checkLink(const std::string& link);

    void updateMovieService(int index, std::string& title, std::string& genre, int year, int likes);

    void addEntries();

    void parseByGenreService(DynamicVector<int>& positions, std::string genre);

    void likeMovie(std::string& link);
    void addToFile(string filename);


    };