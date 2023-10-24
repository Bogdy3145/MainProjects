#include "user.h"
#include "dynamicArray.h"
#include "movie.h"

void user::add(movie& mov) {
    /**
     * checking to see if the movie already exists in our watchlist, and if it doesn't, it will add it
     */
    if (checkLink(mov.getLink())==0)
        this->watchlist.insert(watchlist.end(),mov);
    else
        throw exception();
}

int user::checkLink(std::string link) {
    /**
     * checks if the link given as a param is present our watchlist
     * if it is, it will return 1
     * if it isn't, it will return 0
     */

    for (auto& m:this->watchlist){
        if (m.getLink()==link)
            return 1;
    }
    return 0;

//
//    for (int i = 0; i < this->watchlist.getSize(); i++){
//        if (this->watchlist[i].getLink()==link)
//            return 1;
//    }
//    return 0;
}

int user::deleteMovieFromWatchlist(std::string &link) {
    /**
     * deleting the movie from the watchlist, the unique id being the link
     * if there is no movie with that link, it will throw an exception
     * if all is well, it will return 1
     */
    if (this->checkLink(link)==0)
        throw exception();

    int aux=-1;
    for (auto i:watchlist){
        aux++;
        if(i.getLink()==link){
            break;
        }
    }
    auto it = watchlist.begin()+aux;

    watchlist.erase(it);


//    for (int i = 0; i < this->getSize(); i++){
//        if (this->watchlist[i].getLink()==link)
//            this->watchlist.remove(this->watchlist[i]);
//    }
    return 1;


}
