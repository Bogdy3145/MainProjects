class Movie:

    def __init__(self,id,title,desc,genre):
        self.__id=id
        self.__title=title
        self.__desc=desc
        self.__genre=genre


    def __str__(self):
        return 'ID: ' + str(self.__id) + '   TITLE: ' + str(self.__title) + '   DESC: ' + str(self.__desc) + '   GENRE: ' +str(self.__genre)

    @property
    def get_id(self):
        return self.__id

    @property
    def get_title(self):
        return self.__title

    @property
    def get_description(self):
        return self.__desc

    @property
    def get_genre(self):
        return self.__genre


    def set_id(self,new_id):
        self.__id=new_id


    def set_title(self,new_title):
        self.__title=new_title


    def set_description(self,new_desc):
        self.__desc=new_desc


    def set_genre(self,new_genre):
        self.__genre=new_genre


class Client:

    def __init__(self,id,name,status):
        self.__id=id
        self.__name=name
        self.__blacklist=status

    def __str__(self):
        return 'ID: ' + str(self.__id) + '   NAME: ' + str(self.__name) + '   STATUS: ' + str(self.__blacklist)

    @property
    def get_id(self):
        return self.__id

    @property
    def get_name(self):
        return self.__name

    @property
    def get_blacklist(self):
        return self.__blacklist


    def set_id(self,new_id):
        self.__id=new_id

    def set_name(self,new_name):
        self.__name=new_name

    def set_blacklist(self,bool):
        self.__blacklist=bool

class Rental():

    def __init__(self,id,movieid,clientid,rendate,duedate,retdate):
        self.__id=id
        self.__movie_id=movieid
        self.__client_id=clientid
        self.__rented_date=rendate
        self.__due_date=duedate
        self.__return_date=retdate

    def __str__(self):
        return 'ID: ' + str(self.__id) + '   MOVIE ID: ' + str(self.__movie_id) + '   CLIENT ID: ' + str(self.__client_id) + '   RENT: ' + str(self.__rented_date) + '    DUE: ' + str(self.__due_date) + '   RETURN: ' + str(self.__return_date)

    @property
    def get_id(self):
        return self.__id

    @property
    def get_movie_id(self):
        return self.__movie_id

    @property
    def get_client_id(self):
        return self.__client_id

    @property
    def get_rented_date(self):
        return self.__rented_date

    @property
    def get_due_date(self):
        return self.__due_date

    @property
    def get_return_date(self):
        return self.__return_date

    def set_return_date(self,date):
        self.__return_date=date