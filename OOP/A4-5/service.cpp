#include "service.h"
#include <exception>
#include <string>
#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>

using namespace std;

void service::add(std::string title, std::string genre, int year, int likes, std::string link) {
    year=int(year);
    if (year==0)
        throw std::exception();

    likes=int(likes);
    if (likes==0)
        throw std::exception();

    if (checkLink(link)!=-1)
        throw std::exception();


    movie m(title,genre,year,likes,link);
    this->r.add(m);

}

void service::removeMovie(std::string& str) {
    /**
     * gets the link as a parameter and removes it if it exists
     */

    for(auto& m : this->r.getList()){
        if (m.getLink()==str)
            this->r.remove(m);
    }

//    for (int i = 0; i < this->getSize(); i++)
//        if (this->getElement(i).getLink() == str)
//            this->r.remove(this->getElement(i));
}

int service::checkLink(const std::string& link) {
    int aux=-1;
    for (auto& m : this->r.getList()){
        aux++;
        if (m.getLink()==link)
            return aux;
    }

    return -1;

//    for  (int i = 0; i < this->getSize();i++)
//        if (this->getElement(i).getLink()==link)
//            return i;
//
//    return -1;
}

void service::updateMovieService(int index, std::string &title, std::string &genre, int year, int likes) {
    r.update(index,title,genre,year,likes);


}

void service::parseByGenreService(DynamicVector<int>& positions, std::string genre) {

    int i=0;

    if (genre=="-1"){
        for (auto &m:this->r.getList()){
            i++;
            positions.add(i);
        }
        return;
    }


//    if (genre=="-1") {
//        for (int i = 0; i < this->r.getSize(); i++) {
//            positions.add(i);
//        }
//        return;
//    }

    i = 0;

    for (auto& m:this->r.getList()){
        i++;
        if(m.getGenre()==genre){
            positions.add(i);
        }
    }

//
//    for (int i = 0; i < this->r.getSize(); i++){
//        if (this->r[i].getGenre()==genre){
//            positions.add(i);
//        }
//    }

}

void service::likeMovie(std::string &link) {


    for (auto& m : this->r.getList()){
        if (m.getLink()==link)
            m.setLikes((m.getLikes())+1);
    }

//    for (int i = 0; i < this->r.getSize(); i++){
//        if (this->r[i].getLink()==link)
//            r[i].setLikes(r[i].getLikes()+1);
//    }

}

void service::addToFile(string filename){
    ofstream file;
    file.open(filename);
    string str;
    for (auto& i: r.getList()) {
        //string str = to_string(i);
        file << i.getTitle();
        file << "\n";
        file << i.getGenre();
        file << "\n";
        file << i.getYear();
        file << "\n";
        file << i.getLikes();
        file << "\n";
        file << i.getLink();
        file << "\n";
        file << "\n";

    }
    file.close();

}

void service::addEntries() {
    /**
     * the entries for startup
     */
    movie m;
    m.setTitle("Title");
    m.setGenre("Genre");
    m.setYear(2010);
    m.setLikes(1000);
    m.setLink("www.youtube.com");
    r.add(m);

    movie m1;
    m1.setTitle("Title");
    m1.setGenre("Genre");
    m1.setYear(2012);
    m1.setLikes(2000);
    m1.setLink("www.youtube.com/something");
    r.add(m1);

    movie m2;
    m2.setTitle("The Illusionist");
    m2.setGenre("Action");
    m2.setYear(2012);
    m2.setLikes(1050);
    m2.setLink("https://www.youtube.com/watch?v=i0xO64icGSY&ab_channel=PIKtiva");
    r.add(m2);

    movie m3;
    m3.setTitle("Ford v Ferrari");
    m3.setGenre("Cars");
    m3.setYear(2019);
    m3.setLikes(100000);
    m3.setLink("https://www.youtube.com/watch?v=zyYgDtY2AMY&ab_channel=20thCenturyStudios");
    r.add(m3);

    movie m4;
    m4.setTitle("The Prestige");
    m4.setGenre("Great");
    m4.setYear(2008);
    m4.setLikes(20000);
    m4.setLink("https://www.youtube.com/watch?v=RLtaA9fFNXU");
    r.add(m4);

    movie m5;
    m5.setTitle("Snowpiercer");
    m5.setGenre("Action");
    m5.setYear(2020);
    m5.setLikes(1500);
    m5.setLink("https://www.youtube.com/watch?v=lGcJL6TG5cA");
    r.add(m5);

    movie m6;
    m6.setTitle("Rush");
    m6.setGenre("Niki");
    m6.setYear(2009);
    m6.setLikes(2000);
    m6.setLink("https://www.youtube.com/watch?v=4XA73ni9eVs");
    r.add(m6);

    movie m7;
    m7.setTitle("Mr. Nobody");
    m7.setGenre("Action");
    m7.setYear(2000);
    m7.setLikes(930);
    m7.setLink("https://www.youtube.com/watch?v=mpi0qsp3v_w&ab_channel=hollywoodstreams");
    r.add(m7);

    movie m8;
    m8.setTitle("Three billboards");
    m8.setGenre("Revenge");
    m8.setYear(2021);
    m8.setLikes(30000);
    m8.setLink("www.youtube.com/three");
    r.add(m8);

    movie m9;
    m9.setTitle("Alaska");
    m9.setGenre("Action");
    m9.setYear(2001);
    m9.setLikes(200);
    m9.setLink("www.youtube.com/alaska");
    r.add(m9);

}