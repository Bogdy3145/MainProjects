import domain
from repository import Repo, RentalTextFileRepository, RentalBinFileRepository
from repository import MovieRepo,MovieTextFileRepository,MovieBinFileRepository
from repository import ClientRepo,ClientTextFileRepository, ClientBinFileRepository
from services import Functions
from UndoService import UndoService,Operation,CascadedOperation
import datetime

class UI:

    def __init__(self,func):
        self.__functions=func


    @staticmethod
    def show_menu():
        print("     1. Manage movies")
        print("     2. Manage clients")
        print("     3. Manage rentals")
        print("     4. Search for a client")
        print("     5. Search for a movie")
        print("     6. Statistics")
        print("     7. Undo/Redo")
        #print("     8. Undo/Redo")

    @staticmethod
    def show_movie_menu():
        print("     1. Add movie")
        print("     2. Remove movie")
        print("     3. Update movie")
        print("     4. List movies")
        print("     9. Return to the main menu")

    @staticmethod
    def show_client_menu():
        print("     1. Add client")
        print("     2. Remove client")
        print("     3. Update client")
        print("     4. List client")
        print("     9. Return to the main menu")

    @staticmethod
    def print_rent_menu():
        print("     1. Rent a movie: ")
        print("     2. Return a movie: ")
        print("     3. List the rent log")
        print("     9. Return to the main menu")



    @staticmethod
    def print_search_client():
        print("     1. Search by ID")
        print("     2. Search by Name")
        print("     3. Search by Status")
        print("     9. Return to the main menu")

    @staticmethod
    def print_search_movie():
        print("     1. Search by ID")
        print("     2. Search by Title")
        print("     3. Search by Description")
        print("     4. Search by Genre")
        print("     9. Return to the main menu")

    @staticmethod
    def print_statistics():
        print("     1. Most rented movies")
        print("     2. Most active clients")
        print("     3. Late rentals")

    def print_client_list(self):
        for x in self.__functions.list_client():
            print(x)

    def print_movie_list(self):
        for x in self.__functions.list_movie():
            print(x)

    def print_rent_list(self):
        for x in self.__functions.list_rent():
            print(x)





    def add_movie_details(self):
        id=input("ID to add: ")
        title=input("Title: ")
        desc=input("Description: ")
        genre=input("Genre: ")

        try:
            self.__functions.add_movie(id,title,desc,genre)
        except Exception as ex:
            print(str(ex))

    def add_client_details(self):
        id=input("ID to add: ")
        name=input("Name: ")
        status=False

        try:
            self.__functions.add_client(id,name,status)
        except Exception as ex:
            print(str(ex))

    def remove_movie_detais(self):
        id=input("ID to remove: ")
        try:
            self.__functions.remove_movie(id)
        except Exception as ex:
            print(str(ex))

    def remove_client_details(self):
        id=input("ID to remove: ")
        try:
            self.__functions.remove_client(id)
        except Exception as ex:
            print(str(ex))

    def update_movie_details(self):
        id=input("ID to search for: ")
        title=input("Title to update: ")
        desc=input("Description to update: ")
        genre=input("Genre to update: ")
        try:
            self.__functions.update_movie(id,title,desc,genre)
        except Exception as ex:
            print(str(ex))

    def update_client_details(self):
        id=input("ID to search for: ")
        name=input("Name to update: ")
        status=input("Status to update (True or False): ")
        try:
            self.__functions.update_client(id,name,status)
        except Exception as ex:
            print(str(ex))

    def rent_movie_details(self):
        id=input("ID of the new rental: ")
        client_id=input("ID of the client: ")
        movie_id=input("ID of the movie: ")
        year=int(input("Year of the rent: "))
        month=int(input("Month of the rent: "))
        day=int(input("Day of the rent: "))
        rent_date=datetime.date(year,month,day)
        #rent_date=input("Date of the rent (in format dd/mm/yyyy): ")
        year=int(input("Year of the supposed return: "))
        month=int(input("Month of the supposed return: "))
        day=int(input("Day of the supposed return: "))
        due_date=datetime.date(year,month,day)
        #due_date=input("Date of the supposed return (in format dd/mm/yyyy): ")
        return_date=0
        try:
            self.__functions.rent_movie(id,client_id,movie_id,rent_date,due_date,return_date)
        except Exception as ex:
            print(str(ex))

    def return_movie_details(self):
        id=input("ID you got when you rented the movie: ")
        year=int(input("Current year: "))
        month=int(input("Current month: "))
        day=int(input("Current day: "))
        today_date=datetime.date(year,month,day)
        #today_date=input("Today's date (in format dd/mm/yyyy): ")

        try:
            self.__functions.return_movie(id,today_date)
        except Exception as ex:
            print(str(ex))

    def search_client_id(self):
        word=input("Enter the ID you wish to search for: ")
        print(self.__functions.search_client_id(word))

    def search_client_name(self):
        word=input("Enter the name you wish to search for: ")
        lis=[]
        lis=(self.__functions.search_client_name(word))

        for x in lis:
            print(x)

    def search_client_status(self):
        word=input("Input the status you wish to search for (True/False): ")
        lis=(self.__functions.search_client_status(word))

        for x in lis:
            print(x)

    def search_movie_id(self):
        word=input("Enter the ID you wish to search for: ")
        print(self.__functions.search_movie_id(word))

    def search_movie_name(self):
        word=input("Enter the name of the movie you wish to search for: ")
        lis=self.__functions.search_movie_name(word)

        for x in lis:
            print(x)

    def search_movie_description(self):
        word=input("Enter the description of the movie you wish to search for: ")
        lis=self.__functions.search_movie_description(word)

        for x in lis:
            print(x)

    def search_movie_genre(self):
        word=input("Enter the genre of the movie you wish to search for: ")
        lis=self.__functions.search_movie_genre(word)

        for x in lis:
            print(x)

    def rented_movies_statistics(self):
        list_of_ids,list_of_days=self.__functions.most_rented_movies()

        for x in range(len(list_of_ids)):
            print('DAYS: ' + str(list_of_days[x]) + '   ' + str(self.__functions.get_movie_by_id(list_of_ids[x])))

    def active_clients_statistics(self):
        list_of_ids, list_of_days = self.__functions.most_active_clients()

        for x in range(len(list_of_ids)):
            print('DAYS: ' + str(list_of_days[x]) + '   ' + str(self.__functions.get_client_by_id(list_of_ids[x])))


    def late_rentals_statistics(self):
        list_of_ids, list_of_days = self.__functions.late_rentals()

        for x in range(len(list_of_ids)):
            print('DAYS: ' + str(list_of_days[x]) + '   ' + str(self.__functions.get_movie_by_id(list_of_ids[x])))


    def start(self):

        #self.show_menu()

        while True:
            self.show_menu()
            x=input('>>> ')
            try:
                x=int(x)
            except:
                print("Please introduce a available number")
            if x==0:
                return

            elif x==1:
                self.show_movie_menu()

                while(True):
                    x=input("/>>> ")
                    try:
                        x=int(x)
                    except:
                        print("Please introduce an available number!")

                    if (x==9):
                        break

                    elif x==1:
                        self.add_movie_details()

                    elif x==2:
                        self.remove_movie_detais()

                    elif x==3:
                        self.update_movie_details()

                    elif x==4:
                        self.print_movie_list()

            elif x==2:
                self.show_client_menu()

                while True:
                    x = input("/>>> ")
                    try:
                        x = int(x)
                    except:
                        print("Please introduce an available number!")

                    if (x == 9):
                        break

                    elif x == 1:
                        self.add_client_details()

                    elif x == 2:
                        self.remove_client_details()

                    elif x == 3:
                        self.update_client_details()

                    elif x == 4:
                        self.print_client_list()

            elif x==3:
                self.print_rent_menu()
                while True:
                    x = input("/>>> ")
                    try:
                        x = int(x)
                    except:
                        print("Please introduce an available number!")

                    if (x == 9):
                        break

                    elif x == 1:
                        self.rent_movie_details()

                    elif x == 2:
                        self.return_movie_details()

                    elif x == 3:
                        self.print_rent_list()

            elif x==4:
                self.print_search_client()
                while True:
                    x = input("/>>> ")
                    try:
                        x = int(x)
                    except:
                        print("Please introduce an available number!")

                    if x == 1:
                        try:
                            self.search_client_id()
                        except Exception as ex:
                            print(str(ex))

                    elif x == 2:
                        try:
                            self.search_client_name()
                        except Exception as ex:
                            print(str(ex))

                    elif x == 3:
                        try:
                            self.search_client_status()
                        except Exception as ex:
                            print(str(ex))

                    elif x == 9:
                        break

            elif x==5:
                self.print_search_movie()
                while True:
                    x = input("/>>> ")
                    try:
                        x = int(x)
                    except:
                        print("Please introduce an available number!")

                    if x == 1:
                        try:
                            self.search_movie_id()
                        except Exception as ex:
                            print(str(ex))

                    elif x == 2:
                        try:
                            self.search_movie_name()
                        except Exception as ex:
                            print(str(ex))

                    elif x == 3:
                        try:
                            self.search_movie_description()
                        except Exception as ex:
                            print(str(ex))

                    elif x == 4:
                        try:
                            self.search_movie_genre()
                        except Exception as ex:
                            print(str(ex))

                    elif x == 9:
                        break

            elif x==6:
                self.print_statistics()
                while True:
                    x = input("/>>> ")
                    try:
                        x = int(x)
                    except:
                        print("Please introduce an available number!")

                    if x == 1:
                        try:
                            self.rented_movies_statistics()
                        except Exception as ex:
                            print(str(ex))

                    elif x == 2:
                        try:
                            self.active_clients_statistics()
                        except Exception as ex:
                            print(str(ex))

                    elif x == 3:
                        try:
                            self.late_rentals_statistics()
                        except Exception as ex:
                            print(str(ex))

                    elif x == 9:
                        break


            elif x==7:
                try:
                    self.__functions.undo()
                except Exception as ex:
                    print(str(ex))

            elif x==8:
                try:
                    self.__functions.redo()
                except Exception as ex:
                    print(str(ex))

            else:
                print("Please choose an available command")

def open_settings():

    file_name="settings.properties"

    with open(file_name,"r") as f:
        line=f.readline()
        line = line.strip('\n')

        repo,type=line.split("=")

        print(type)
        if type == "inmemory":
            movie_repo=MovieRepo()
            client_repo=ClientRepo()
            data_repo=Repo()
            #print("xd")

        elif type == "binary":
            for line in f.readlines():
                line=line.strip()
                line=line.strip('\n')

                repo,name=line.split("=")

                if repo=="movie_repo":
                    movie_repo=MovieBinFileRepository(name)
                if repo=="client_repo":
                    client_repo=ClientBinFileRepository(name)
                if repo=="rental_repo":
                    data_repo=RentalBinFileRepository(name)

        elif type == "text":
            for line in f.readlines():
                line=line.strip()
                line=line.strip('\n')

                repo,name=line.split("=")
                if repo=="movie_repo":
                    movie_repo=MovieTextFileRepository(name)
                if repo=="client_repo":
                    client_repo=ClientTextFileRepository(name)
                if repo=="rental_repo":
                    data_repo=RentalTextFileRepository(movie_repo,client_repo,name)

    return movie_repo,client_repo,data_repo

# movie_repo=MovieBinFileReposiory()
#
# client_repo=ClientBinFileRepository()
#
# data_repo=RentalTextFileRepository(movie_repo,client_repo)

movie_repo,client_repo,data_repo=open_settings()

#open_settings(movie_repo,client_repo,data_repo)

undo_service=UndoService()
#data_repo.rental_random(movie_repo,client_repo)

functions=Functions(movie_repo,client_repo,data_repo,undo_service)
#functions.rental_random_generator(movie_repo,client_repo)


ui=UI(functions)

ui.start()

