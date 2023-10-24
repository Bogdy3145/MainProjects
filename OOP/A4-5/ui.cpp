
#include "dynamicArray.h"
#include "ui.h"
#include "service.h"
#include "repo.h"
#include <iomanip>
#include <iostream>
#include <string>
#include "tests.h"
#include "user.h"
#include <windows.h>
#include <shellapi.h>


using namespace std;

bool is_number(const std::string& s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}

void printAdminMenu(){
    cout << "\n";
    cout << "1. Add a movie \n";
    cout << "2. Remove a movie \n";
    cout << "3. Update a movie \n";
    cout << "4. List all movies \n";
    cout << "0. Go back \n";

}

void printUserMenu(){
    cout << "\n";
    cout << "1. Filter by genre \n";
    cout << "2. See your watchlist \n";
    cout << "3. Delete a movie from watchlist \n";
    cout << "0. Go back \n";

}

void addMovie(service& s){
    string year,likes;
    string title,link,genre;
    cin.get();
    cout << "Enter the title: ";
    std::getline(std::cin,title);
    cout << "Enter the genre: ";
    std::getline(cin,genre);
    cout << "Enter the year: ";
    cin >> year;
    if (is_number(year)==0){
        cout << "Year must be an integer.";
        return;
    }

    cout << "Enter the likes: ";
    cin >> likes;

    if (is_number(likes)==0){
        cout << "Likes must be an integer.";
        return;
    }


    cout << "Enter the link: ";
    cin >> link;
    int year_int,likes_int;
    year_int=stoi(year);
    likes_int=stoi(likes);
    try {
        s.add(title, genre, year_int, likes_int, link);
    }
    catch(exception){
        cout << "Something went wrong!";
    }

}

void printAllMovies(service& s){
    for (int i = 0; i <s.getSize(); i++) {
        string str = s.to_string(s.getElement(i));
        cout << str << "\n";
    }
}

void removeMovie(service& s){
    string link;
    cout << "Link to the trailer: ";
    cin >> link;
    s.removeMovie(link);
}

void updateMovie(service& s){

    string link;
    cout << "Link to the movie that is to be updated: ";
    cin >> link;
    int index=s.checkLink(link);
    if (index==-1) {
        cout << "This movie doesn't exist!";
        return;
    }
    string title, genre;
    string year, likes;
    cout << "New title: ";
    cin >> title;
    cout << "New genre: ";
    cin >> genre;
    cout << "New year: ";
    cin >> year;
    if (is_number(year)==0){
        cout << "Year must be an integer.";
        return;
    }

    cout << "Enter the likes: ";
    cin >> likes;

    if (is_number(likes)==0){
        cout << "Likes must be an integer.";
        return;
    }

    int year_int,likes_int;
    year_int=stoi(year);
    likes_int=stoi(likes);

    s.updateMovieService(index,title,genre,year_int,likes_int);
    cout << "Movie successfully updated!\n";


}
void like(service& s,std::string& link){
    cout << "1. Like \n";
    cout << "2. Nothing \n";
    string aux;
    int aux_int;
    cin >> aux;
    if (aux=="1")
        s.likeMovie(link);


}

bool addToWatchlist(){
    cout << "Press 1 if you wish to add to watchlist. \n";
    string aux;
    cin >> aux;
    if (aux=="1")
        return true;
    return false;
}

bool next(){
    cout << "1. You wish to continue? \n";
    cout << "2. You wish to stop here. \n";
    string aux;
    cin >> aux;
    if (aux=="1")
        return true;
    return false;
}

bool retakeList(){
    cout << "You've come to the end of the list! \n \n";
    cout << "1. You want to retake the list. \n";
    cout << "2. You want to stop here. \n";

    string aux;
    cin >> aux;
    if (aux=="1")
        return true;
    return false;
}

void parseByGenre(service& s, user& u){
    cout << "Enter the genre by which you wish to filter: ";
    string genre;
    cin >> genre;

    DynamicVector<int> arrayOfPositions;

    s.parseByGenreService(arrayOfPositions,genre);

    int aux;
    string str;
    movie aux_movie;
    cout << "\n";

    do {
        for (int i = 0; i < arrayOfPositions.getSize(); i++) {
            aux = arrayOfPositions[i];
            str = s.to_string(s.getElement(aux));
            cout << str << endl;
            ShellExecuteA(NULL,NULL,"chrome.exe", s.getElement(aux).getLink().c_str(),NULL,SW_SHOWMAXIMIZED);
            if (addToWatchlist()) {
                try {
                    u.add(s.getElement(aux));
                }
                catch (exception) {
                    cout << "Can't add this movie twice! \n";
                }
            }
            if (!next())
                return;

        }
    }while (retakeList());
}

void deleteMovieFromWatchlist(service& s, user& u){
    cout << "Enter the link of the movie you want to delete: ";
    string aux;
    cin >> aux;

    try{
        if (u.deleteMovieFromWatchlist(aux)==1)
            cout << "Movie deleted succesfully! \n";
        like(s,aux);
    }
    catch (exception){
        cout << "This movie isn't in your watchlist! \n";
    }
}

void printWatchlist(service& s, user& u){
    string str;
    for (int i = 0; i < u.getSize(); i++){
        str=s.to_string(u[i]);
        cout << str << " \n";
    }
}

void intoFile(service& s){
    s.addToFile("database.txt");
}

int main() {

    //testAll();

    repo r;
    service s(r);
    s.addEntries();
    user u;



    cout << "1. Admin mode. \n2. User mode. \n";
    string x;
    cin >> x;
    while (x!="0") {
        if (x == "1") {
            printAdminMenu();
            cin >> x;
            while (x != "0") {
                if (x == "1")
                    addMovie(s);
                else if (x == "2")
                    removeMovie(s);
                else if (x == "3")
                    updateMovie(s);
                else if (x == "4")
                    printAllMovies(s);
                else if (x == "5")
                    intoFile(s);
                else if (x == "9")
                    break;
                printAdminMenu();
                cin >> x;
            }
        } else if (x == "2") {
            printUserMenu();
            while (x != "0") {
                if (x == "1")
                    parseByGenre(s,u);
                else if (x == "2")
                    printWatchlist(s,u);
                else if (x == "3")
                    deleteMovieFromWatchlist(s,u);
                printUserMenu();
                cin >> x;
            }

        }
        cout << "1. Admin mode. \n2. User mode. \n";
        cin >> x;
    }

}

