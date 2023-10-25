import unittest
import random
import string
import datetime
from domain import Movie,Client,Rental
import pickle

import services

class MovieException(Exception):
    pass

class MovieRepo:

    def __init__(self):
        self.__movie_data=[]

    def movie_random(self,random,random_movie,random_description,random_genre):
        m=Movie(random,random_movie,random_description,random_genre)
        self.__movie_data.append(m)

    def get_movie_list(self):
        return self.__movie_data

    def set_movie_list(self,new_list):
        self.__movie_data=new_list

    def list_movie(self):
        return self.__movie_data

    def add_movie(self,id,title,desc,genre):
        """
        id: the new movie's id
        title: the title of the new movie
        desc: the description of the new movie
        genre: the genre of the new movie
        """
        id=str(id)

        if not id.isnumeric():
            raise MovieException ("ID must be a numeric value!")

        for x in self.__movie_data:
            if str(x.get_id)==str(id):
                raise MovieException ("You can't have 2 movies with the same ID!")

        aux=Movie(id,title,desc,genre)
        self.__movie_data.append(aux)

    def remove_movie(self, id):
        """
        id: id of the movie we're to remove
        """
        aux=0
        for x in self.__movie_data:
            if str(x.get_id) == str(id):
                self.__movie_data.remove(x)
                aux=1

        if aux==0:
            raise Exception ("The movie with the given ID does not exist!")

    def update_movie(self,id,title,desc,genre):
        """
        id: id of the movie we'll update
        title: the new title we'll give to the movie
        desc: the new description we'll give to the movie
        genre: the new genre we'll give to the movie
        """
        aux = 0
        for i in range(len(self.__movie_data)):
            if str(self.__movie_data[i].get_id) == str(id):
                self.__movie_data[i].set_title(title)
                self.__movie_data[i].set_description(desc)
                self.__movie_data[i].set_genre(genre)
                aux = 1

        if aux==0:
            raise Exception ("The movie with the given ID does not exist!")

    def get_movie_pos(self, pos):
        return self.__movie_data[pos]

    def search_movie_id(self,word):
        for x in self.__movie_data:
            if str(x.get_id)==str(word):
                return x

        raise Exception ("There are no movies with the given id.")

    def search_movie_name(self,aux):
        for x in self.__movie_data:
            if x==aux:
                return x.get_title

    def search_movie_description(self,aux):
        for x in self.__movie_data:
            if x==aux:
                return x.get_description

    def search_movie_genre(self,aux):
        for x in self.__movie_data:
            if x == aux:
                return x.get_genre

    def get_movie_by_id(self,id):
        for x in self.__movie_data:
            if int(x.get_id)==int(id):
                return x

class ClientRepo:

    def __init__(self):
        self.__client_data=[]

    def client_random(self,randomid,name):

        m = Client(randomid, name)
        self.__client_data.append(m)

    def get_client_list(self):
        return self.__client_data

    def set_client_list(self,new_list):
        self.__client_data=new_list

    def get_client(self, pos):
        return self.__client_data[pos]

    def list_client(self):
        return self.__client_data

    def add_client(self,id,name,status):
        """
        id: the new client's id
        name: the name of the new client
        *note: his status will be automatically set to false
        """
        for x in self.__client_data:
            if str(x.get_id)==str(id):
                raise Exception ("You can't have 2 clients with the same ID!")

        aux = Client(id, name, status)
        self.__client_data.append(aux)

    def remove_client(self,id):
        """
        id: id of the client we're to remove
        """
        aux=0
        for x in self.__client_data:
            if str(x.get_id) == str(id):
                self.__client_data.remove(x)
                aux=1

        if aux==0:
            raise Exception ("The client with the given ID does not exist!")

    def update_client(self,id,name,status):
        """
        id: id of the client
        name: the new name we'll give to the client
        status: the new status we'll give to the client ( whether he's blacklisted or not )
        """
        aux = 0
        for i in range(len(self.__client_data)):
            if str(self.__client_data[i].get_id) == str(id):
                self.__client_data[i].set_name(name)
                if str(status).lower()=="true":
                    self.__client_data[i].set_blacklist(True)
                elif str(status).lower()=="false":
                    self.__client_data[i].set_blacklist(False)

                aux=1

        if aux==0:
            raise Exception ("The client with the given ID does not exist!")

    def search_client_id(self,word):
        """
        word=id

        we return the object of the class with the given id
        """

        for x in self.__client_data:
            if str(x.get_id) == str(word):
                return x

        raise Exception ("There are no clients with that ID")

    def search_client_name(self,word_lis):
        """
        word: the name we're searching for

        return: a list of client objects with the name similar to the given words
        """
        list_of_clients=[]
        fname_lname_list=[]
        for x in self.__client_data:
            aux=x.get_name.lower()
            fname_lname_list=aux.split(' ')          #in fname_lname_list we have the names from the class and in
                                                            # lis we have the names by which we are searching
            ok=True                                         #ok is a boolean to know if we are already returning an instance from the class
            for i in range(len(word_lis)):
                for j in range(len(fname_lname_list)):
                    if fname_lname_list[j]==word_lis[i]:
                        for l in list_of_clients:
                            if l==x:
                                ok=False
                        if ok==True:
                            list_of_clients.append(x)

        if list_of_clients==[]:
           raise Exception ("There are no clients with such name.")

        return list_of_clients

    def search_client_status(self,status):
        """
        status: the status we're searching for

        return: a list of all the clients that have the same status as the one given
        """
        lis=[]
        for x in self.__client_data:
            if str(x.get_blacklist).lower()==status:
                lis.append(x)

        if lis==[]:
            raise Exception ("There are no clients with the given status.")

        return lis

    def get_client_by_id(self,id):
        """
        id: an ID

        return: the client object with that given ID
        """
        for x in self.__client_data:
            if int(x.get_id)==int(id):
                return x

class Repo:

    def __init__(self):
        self.__rental_data=[]

    def rental_random(self,rent,movid,clid,rented_date,duedate,return_date):
        m=Rental(rent,movid,clid,rented_date,duedate,return_date)
        self.__rental_data.append(m)

    def list_rent(self):
        return self.__rental_data

    def set_rental_list(self,new_list):
        self.__rental_data=new_list

    def rent_movie(self,id,client_id,movie_id,rent_date,due_time,return_date):
        """
        id: id of the rental
        client_id: id of the client that rents
        movie_id: id of the movie that is being rented
        rent_date: date in which the rent takes place
        due_date: date in which the movie is supposed to be returned
        return_date: for the moment it's 0, but it will be changed when the movie will be returned

        """

        #client_data=client_obj.get_client_list()
        #movie_data=movie_obj.get_movie_list()
        #print(client_data)

        for x in self.__rental_data:
            if str(x.get_id)==str(id):
                raise Exception ("This ID for the rental is already in use")

        aux=Rental(id,movie_id,client_id,rent_date,due_time,return_date)
        self.__rental_data.append(aux)

        for x in self.__rental_data:
            print(x)

    def remove_rental(self,item):
        self.__rental_data.remove(item)

    def return_movie(self,id,today_date,movie_obj,client_obj):
        """
        id: id of the movie to return
        today_date: the date in which the return takes place, to know if the customer was late in delivering the movie
                    this will take place of the argument return_date in the rental class
        """

        movie_data=movie_obj.get_movie_list()
        client_data=client_obj.get_client_list()

        exist=0
        for x in self.__rental_data:
            if str(x.get_id)==str(id):
                exist=1

                if str(x.get_return_date)=='0':

                    aux=x.get_due_date
                    day=aux.day
                    month=aux.month
                    year=aux.year
                    #day,month,year=aux.day,aux.month,aux,year

                    aux2=today_date
                    return_day=aux2.day
                    return_month=aux2.month
                    return_year=aux2.year
                    #return_day,return_month,return_year=aux2.split('/')

                    client_id=x.get_client_id

                    for y in client_data:
                        if str(y.get_id)==str(client_id):
                            client=y

                    if return_year>year:
                        client.set_blacklist(True)
                        #print("you've been blacklisted")
                    elif return_month>month:
                        client.set_blacklist(True)
                        #print("you've been blacklisted")
                    elif return_day>day:
                        client.set_blacklist(True)
                        #print("you've been blacklisted")

                        #print("good")

                    x.set_return_date(today_date)
                else:
                    raise Exception ("There must be a mistake, this movie appears to be with us already")
                    #print("deja sa returnat bos")
        if exist==0:
            raise Exception ("This ID doens't exist")

    def set_return_movie(self, id, today_date, movie_obj, client_obj):
        """
        id: id of the movie to return
        today_date: the date in which the return takes place, to know if the customer was late in delivering the movie
                    this will take place of the argument return_date in the rental class
        """

        movie_data = movie_obj.get_movie_list()
        client_data = client_obj.get_client_list()
        for x in self.__rental_data:
            #x.set_return_date=0
            if str(x.get_id) == str(id):
                x.set_return_date(today_date)
                client=x.get_client_id

        for x in client_data:
            if str(x.get_id)==str(client):
                x.set_blacklist(False)



    def calculate_rental_days(self,item):
        """
        item: a rental object

        return:
        """
        today=datetime.date.today()

        if item.get_return_date==0:
            days=today-item.get_rented_date
        else:
            days=item.get_return_date-item.get_rented_date

        return days.days

    def calculate_late_days(self,item):
        """
        item: a rental object

        return: the number of days that rental is late
        """
        today=datetime.date.today()

        if str(item.get_return_date)==str(0) and item.get_due_date<today:
            days=today-item.get_due_date
        else:
            return 0

        print (days.days)
        if days.days<0:
            return 0

        return days.days

    def get_rental(self,pos):
        return self.__rental_data[pos]

    def get_rental_data(self):
        return self.__rental_data


class MovieTextFileRepository(MovieRepo):

    def __init__(self,name):
        super().__init__()

        self.file_name = name
        self.load_file()

    def load_file(self):

        with open(self.file_name, "r") as f:
            for line in f.readlines():
                line.strip()
                line.strip('\n')
                print(len(self.get_movie_list()))
                if line != '\n':
                    if len(line)>1:
                        id,title,description,genre,nothing=line.split(maxsplit=4,sep=', ')
                        self.add_movie(id,title,description,genre)

    def save_file(self):

        with open(self.file_name,"w") as f:
            for movie in self.get_movie_list():
                print(str(movie.get_id))
                f.write(str(movie.get_id) + ', ' + movie.get_title + ', ' + movie.get_description + ', ' + movie.get_genre + ', \n')

    def add_movie(self,id,title,description,genre):
        super(MovieTextFileRepository,self).add_movie(id,title,description,genre)

        self.save_file()

    def remove_movie(self, id):
        super(MovieTextFileRepository,self).remove_movie(id)

        self.save_file()

    def update_movie(self,id,title,desc,genre):
        super(MovieTextFileRepository,self).update_movie(id,title,desc,genre)

        self.save_file()


class MovieBinFileRepository(MovieRepo):
    def __init__(self,name):
        super().__init__()
        #self.__data = []
        self.file_name = name
        self.load_file()


    def load_file(self):
        with open(self.file_name,"rb") as f:
            try:

                self.__data=pickle.load(f)
                self.set_movie_list(self.__data)
                #print(self.__data)

            except EOFError:
                self.__data=[]
                pass

    def save_file(self):
        with open(self.file_name,"wb") as f:
            print(self.__data)
            pickle.dump(self.__data,f,pickle.HIGHEST_PROTOCOL)

    def add_movie(self,id,title,description,genre):
        super(MovieBinFileRepository,self).add_movie(id,title,description,genre)

        self.__data=self.get_movie_list()

        self.save_file()

    def remove_movie(self, id):
        super(MovieBinFileRepository,self).remove_movie(id)

        self.__data = self.get_movie_list()
        self.save_file()

    def update_movie(self,id,title,desc,genre):
        super(MovieBinFileRepository,self).update_movie(id,title,desc,genre)

        self.__data = self.get_movie_list()
        self.save_file()


class ClientTextFileRepository(ClientRepo):

    def __init__(self,name):
        super().__init__()

        self.file_name=name
        self.load_file()

    def load_file(self):

        with open (self.file_name,"r") as f:
            for line in f.readlines():
                line.strip()
                if len(line)>1:
                    id,name,status,nothing=line.split(maxsplit=3,sep=', ')
                    self.add_client(id,name,status)

    def save_file(self):

        with open (self.file_name,"w") as f:
            for client in self.get_client_list():
                f.write(str(client.get_id) + ', ' + client.get_name + ', ' + str(client.get_blacklist) + ', \n')

    def add_client(self,id,name,status):
        super(ClientTextFileRepository,self).add_client(id,name,status)

        self.save_file()

    def remove_client(self,id):
        super(ClientTextFileRepository,self).remove_client(id)

        self.save_file()

    def update_client(self,id,name,status):
        super(ClientTextFileRepository,self).update_client(id,name,status)

        self.save_file()


class ClientBinFileRepository(ClientRepo):

    def __init__(self,name):
        super().__init__()

        self.file_name=name
        self.load_file()

    def load_file(self):
        with open(self.file_name, "rb") as f:
            try:

                self.__data = pickle.load(f)
                self.set_client_list(self.__data)


            except EOFError:
                self.__data = []
                pass

    def save_file(self):

        self.__data=self.get_client_list()

        with open(self.file_name, "wb") as f:
            print(self.__data)
            pickle.dump(self.__data, f, pickle.HIGHEST_PROTOCOL)

    def add_client(self,id,name,status):
        super(ClientBinFileRepository,self).add_client(id,name,status)

        self.save_file()

    def remove_client(self,id):
        super(ClientBinFileRepository,self).remove_client(id)

        self.save_file()

    def update_client(self,id,name,status):
        super(ClientBinFileRepository,self).update_client(id,name,status)

        self.save_file()


class RentalTextFileRepository(Repo):

    def __init__(self,movie_repo,client_repo,name):
        super().__init__()

        self.file_name=name
        self.load_file()
        self.__movie_repo=movie_repo
        self.__client_repo=client_repo

    def load_file(self):

        with open (self.file_name,"r") as f:
            for line in f.readlines():
                line.strip()
                if len(line)>2:
                    id,movie_id,client_id,rent_date,due_date,return_date,endline=line.split(maxsplit=6,sep=', ')

                    year,month,day=rent_date.split('-')
                    day=int(day)
                    month=int(month)
                    year=int(year)
                    rent_date=datetime.date(year=year,month=month,day=day)

                    year, month, day = due_date.split('-')
                    day = int(day)
                    month = int(month)
                    year = int(year)
                    due_date=datetime.date(year=year,month=month,day=day)

                    if str(return_date)!='0':
                        year, month, day = return_date.split('-')
                        day = int(day)
                        month = int(month)
                        year = int(year)
                        return_date=datetime.date(year=year,month=month,day=day)


                    self.rent_movie(id,client_id,movie_id,rent_date,due_date,return_date)

    def save_file(self):

        with open (self.file_name, "w") as f:
            for rental in self.get_rental_data():
                f.write(str(rental.get_id) + ', ' + str(rental.get_movie_id) + ', ' + str(rental.get_client_id) + ', '
                        + str(rental.get_rented_date) + ', ' + str(rental.get_due_date) + ', '
                        + str(rental.get_return_date) + ', \n')

    def rent_movie(self,id,client_id,movie_id,rent_date,due_time,return_date):

        super(RentalTextFileRepository,self).rent_movie(id,client_id,movie_id,rent_date,due_time,return_date)

        self.save_file()

    def return_movie(self,id,today_date,movie_obj,client_obj):
        super(RentalTextFileRepository,self).return_movie(id,today_date,movie_obj,client_obj)

        self.save_file()

    def remove_rental(self,item):
        super(RentalTextFileRepository,self).remove_rental(item)

        self.save_file()

    def set_return_movie(self, id, today_date, movie_obj, client_obj):
        super(RentalTextFileRepository,self).set_return_movie(id,today_date,movie_obj,client_obj)

        self.save_file()

class RentalBinFileRepository(Repo):

    def __init__(self,name):
        super().__init__()

        self.file_name=name
        self.load_file()

    def load_file(self):

        with open(self.file_name,"rb") as f:
            try:
                self.__data=pickle.load(f)
                self.set_rental_list(self.__data)

            except EOFError:
                self.__data=[]

    def save_file(self):

        self.__data=self.get_rental_data()

        with open(self.file_name, "wb") as f:
            print(self.__data)
            pickle.dump(self.__data, f, pickle.HIGHEST_PROTOCOL)

    def rent_movie(self,id,client_id,movie_id,rent_date,due_time,return_date):

        super(RentalBinFileRepository,self).rent_movie(id,client_id,movie_id,rent_date,due_time,return_date)

        self.save_file()

    def return_movie(self,id,today_date,movie_obj,client_obj):
        super(RentalBinFileRepository,self).return_movie(id,today_date,movie_obj,client_obj)

        self.save_file()

    def remove_rental(self,item):
        super(RentalBinFileRepository,self).remove_rental(item)

        self.save_file()

    def set_return_movie(self, id, today_date, movie_obj, client_obj):
        super(RentalBinFileRepository,self).set_return_movie(id,today_date,movie_obj,client_obj)

        self.save_file()