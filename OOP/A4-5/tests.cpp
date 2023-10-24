#include "tests.h"
#include "repo.h"
#include "service.h"
#include "movie.h"
#include "dynamicArray.h"
#include <assert.h>

void testDynamicArray(){
    DynamicVector<int> arr(1);
    DynamicVector<int> arr2(1);


    arr.add(10);
    arr2=arr;


    assert(arr.getSize()==1);
    assert(arr2.getSize()==1);
    assert(&(arr=arr)==&arr);
    assert(arr[0]==10);

    arr.add(20);
    assert(arr[1]==20);

    movie m;
    std::string title = "tit";
    std::string genre = "gen";
    std:: string link = "c";
    int year=1,likes=10;
    movie m2(title,genre,year,likes,link);

    DynamicVector<movie> arr3;
    arr3.add(m);
    arr3.add(m2);
    arr3.remove(m);
    assert(arr3.getSize()==1
    );

    //GETTERS
    //arr3.add(m);
    arr3[0].setLink("LINK");
    assert(arr3[0].getLink()=="LINK");
    arr3[0].setTitle("TITLE");
    assert(arr3[0].getTitle()=="TITLE");
    arr3[0].setGenre("GEN");
    assert(arr3[0].getGenre()=="GEN");
    arr3[0].setYear(10);
    assert(arr3[0].getYear()==10);
    arr3[0].setLikes(20);
    assert(arr3[0].getLikes()==20);


}

void testRepo(){
    repo r;

    std::string title = "tit";
    std::string genre = "gen";
    std:: string link = "c";
    int year=1,likes=10;
    movie m2(title,genre,year,likes,link);

    r.add(m2);
    assert(r.getSize()==1);
    std::string new_tit="new";
    std::string new_gen="gen";
    r.update(0,new_tit,new_gen,year,likes);
    assert(r[0].getTitle()=="new");
    r.remove(m2);
    assert(r.getSize()==0);


}

void testService(){
    repo r;
    service s(r);

    assert(s.getSize()==0);

    std::string title = "tit";
    std::string genre = "gen";
    std:: string link = "c";
    int year=1,likes=10;

    s.add(title,genre,year,likes,link);
    assert(s.getElement(0).getTitle()=="tit");

    std::string str = s.to_string(s.getElement(0));
    assert(str=="TITLE: tit    GENRE: gen    YEAR: 1    LIKES: 10     LINK: c");

    std::string new_tit = "new";
    s.updateMovieService(0,new_tit,genre,year,likes);
    assert(s.getElement(0).getTitle()=="new");

    int exLikes=s.getElement(0).getLikes();
    s.likeMovie(link);
    assert(exLikes+1==s.getElement(0).getLikes());

    year=0;
    bool exceptionThrown=false;
    try{
        s.add(title,genre,year,likes,link);
    }
    catch(std::exception){
        exceptionThrown=true;
    }
    assert(exceptionThrown==true);

    likes=0;
    year=1;
    exceptionThrown=false;
    try{
        s.add(title,genre,year,likes,link);
    }
    catch(std::exception){
        exceptionThrown=true;
    }
    assert(exceptionThrown==true);

    likes=1;
    exceptionThrown=false;
    try {
        s.add(title, genre, year, likes, link);
    }
    catch (std::exception){
        exceptionThrown=true;
    }
    assert(exceptionThrown==true);



    std::string str1="c";
    s.checkLink(str1);
    s.removeMovie(str1);
    assert(s.getSize()==0);



    DynamicVector<int> positions;
    DynamicVector<int> positions2;

    title = "tit";
    genre = "gen";
    link = "a";
    year=1,likes=10;

    s.add(title,genre,year,likes,link);

    title = "tit";
    genre = "genre";
    link = "b";
    year=1,likes=10;

    s.add(title,genre,year,likes,link);

    title = "tit";
    genre = "gen";
    link = "d";
    year=1,likes=10;

    s.add(title,genre,year,likes,link);

    s.parseByGenreService(positions,genre);
    assert(positions.getSize()==2);

    genre="-1";
    s.parseByGenreService(positions2,genre);
    assert(positions2.getSize()==3);
}

void testOperation(){
    DynamicVector<int> arr(1);
    arr = arr + 1;

    assert(arr.getSize()==1);

    arr = 1 + arr;

    assert(arr.getSize()==2);
}

void testUser(){
    repo r;
    service s(r);
    user u;

    assert(u.getSize()==0);

    movie m;
    u.add(m);
    assert(u.getSize()==1);

    bool exceptionThrown=false;


    std::string title = "tit";
    std::string genre = "gen";
    std:: string link = "c";
    int year=1,likes=10;

    movie m2(title,genre,year,likes,link);

    u.add(m2);
    assert(u.checkLink(link)==1);
    assert(u[1].getTitle()=="tit");

    try{
        u.add(m2);
    }
    catch (exception){
        exceptionThrown=true;
    }
    assert(exceptionThrown==true);

    exceptionThrown=false;

    assert(u.deleteMovieFromWatchlist(link)==1);

    try{
        u.deleteMovieFromWatchlist(link);
    }
    catch (exception){
        exceptionThrown=true;
    }

    assert(exceptionThrown==true);

}

void testAll(){
    testDynamicArray();
    testRepo();
    testService();
    testOperation();
    testUser();
}