#include "movie.h"

movie::movie(std::string &title, std::string &genre, const int year_of_release, const int nr_of_likes,
             std::string &link)
             :title{ title }, genre{genre}, year_of_release{year_of_release}, nr_of_likes{nr_of_likes},link{link}{}
