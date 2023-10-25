import random
import datetime
import data_structure

from UndoService import Operation,FunctionCall,CascadedOperation

class Functions:

    def __init__(self,movierep,clientrep,repository,undo_service):
        self.__movie_repo=movierep
        self.__client_repo=clientrep
        self.__rental_repo=repository
        self._undo_service=undo_service

    def movie_random_generator(self):
        """
                Generating the first 20 inputs for the class Movie
                """

        random_movie_list = ["The Prestige", "Nightcrawler", "Mr. Bean", "Ford v Ferrari", "Rush", "Black Mirror",
                             "Time",
                             "Once Upon a Time in America", "Once Upon a Time in Hollywood", "The Irishman", "Hugo",
                             "BoJack Horseman", "Mr. Robot", "I Origins", "Dune", "Star Wars", "Begin Again", "Luca",
                             "Gravity",
                             "8 Mile", "The Illusionist", "Blow", "Judas and the Black Messiah"]

        random.shuffle(random_movie_list)

        randomList = random.sample(range(10, 100), 20)

        random_description_list = ["A nice description", "A bad description", "Idk any more descriptions",
                                   "Description",
                                   "Another bad description", "10/10 on IMDB", "Who is this guy",
                                   "Christopher Nolan rules",
                                   "Christopher Nolan Sucks", "Best direct ever", "I dont like this movie", "BEST",
                                   "What",
                                   "I'm confused", "What did I just watch", "I'm Bored", "Why did I watch this?",
                                   "Should've watched Hugo..", "Quentin Tarantino senpai",
                                   "Generating 20 random stuff=boring",
                                   "Great movie again", "Tbh I like all those movies"]

        random.shuffle(random_description_list)

        random_genre_list = ["Action", "Thriller", "Horror", "Sci-Fi", "Drama"]

        for i in range(20):
            self.__movie_repo.movie_random(randomList[i],random_movie_list[i],random_description_list[i],random_genre_list[random.randint(0,4)])

    def client_random_generator(self):
        """
                Generating the first 20 inputs for the class Client
                """

        randomList = random.sample(range(10, 100), 20)

        randomFname = ["Alex", "Bogdan", "Mircea", "Victor", "Deian", "Messi", "Haaland", "Veratti", "Florin",
                       "Gheorghe", "Ionut", "Eduard", "Neymar", "Banel", "Mitrut", "Mirel", "Mihai", "EDG", "Faker",
                       "Showmaker"]
        random.shuffle(randomFname)
        randomLname = ["Ion", "Aioanei", "Mariusel", "Cretu", "Miguel", "Martini", "Ololosh", "Rapunzel", "Janu",
                       "Salam", "Khan", "Bjergsen", "Doublelift", "Tyler", "BoxBox", "Leclerc", "Norris", "Meiko",
                       "YellowStar",
                       "Hashinshin"]

        random.shuffle((randomLname))

        for i in range(20):
            name = randomFname[i] + ' ' + randomLname[i]
            self.__client_repo.client_random(randomList[i],name)

    def rental_random_generator(self,movie_obj,client_obj):
        """
                Generating the first 20 inputs for the class Rental
                """
        self.movie_random_generator()
        movie_data = movie_obj.get_movie_list()

        self.client_random_generator()
        client_data = client_obj.get_client_list()

        # self.__client.client_random()

        randomList = random.sample(range(10, 100), 20)

        random_day1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        random_day2 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

        random_month1 = [1, 2, 3, 4, 5, 6]
        random_month2 = [8, 9, 10, 11, 12]

        random.shuffle(random_day1)
        random.shuffle(random_month1)

        random.shuffle(random_day2)
        random.shuffle(random_month2)

        duedate = []
        rented_date = []
        return_date = []

        for i in range(20):
            curr_random_month = random.randint(1, 6)
            curr_random_day = random.randint(1, 15)

            x = datetime.date(year=2021, month=curr_random_month, day=curr_random_day)
            rented_date.append(x)
            # print(rented_date[i])

            x = datetime.date(year=2021, month=curr_random_month + 2, day=curr_random_day)
            duedate.append(x)

            x = datetime.date(year=2021, month=random.randint(6, 12), day=random.randint(16, 30))
            return_date.append(x)

            # rented_date.append(str(curr_random_day)+'/'+str(curr_random_month)+'/'+'2021')
            # duedate.append(str(curr_random_day)+'/'+str(curr_random_month+2)+'/'+'2021')
            # return_date.append(str(random.randint(16,30))+'/'+str(random.randint(6,12))+'/'+'2021')

        print(client_data)
        print()
        print(movie_data)

        for i in range(20):
            rent = randomList[i]
            client = client_data[random.randint(0, 19)]
            clid = client.get_id
            movie = movie_data[random.randint(0, 19)]
            movid = movie.get_id

            dueday, duemonth, dueyear = duedate[i].day, duedate[i].month, duedate[i].year
            retday, retmonth, retyear = return_date[i].day, duedate[i].month, duedate[i].year

            if int(dueyear) < int(retyear):
                client.set_blacklist(True)
            elif int(duemonth) < int(retmonth):
                client.set_blacklist(True)
            elif int(dueday) < int(retday):
                client.set_blacklist(True)

            #aux = Rental(rent, movid, clid, rented_date[i], duedate[i], return_date[i])

            self.__rental_repo.rental_random(rent,movid,clid,rented_date[i],duedate[i],return_date[i])


    def list_movie(self):
        return self.__movie_repo.list_movie()

    def list_client(self):
        return self.__client_repo.list_client()

    def list_rent(self):
        return self.__rental_repo.list_rent()

    def add_movie(self,id,title,desc,genre):

        self.__movie_repo.add_movie(id,title,desc,genre)


        movie=self.__movie_repo.get_movie_by_id(id)

        fc_undo=FunctionCall(self.remove_movie,movie.get_id)
        fc_redo=FunctionCall(self.add_movie,movie.get_id,movie.get_title,movie.get_description,movie.get_genre)

        cope=CascadedOperation()
        cope.add(Operation(fc_undo,fc_redo))

        self._undo_service.record_operation(cope)

    def add_client(self,id,name,status):

        id=str(id)

        if id.isnumeric():
            self.__client_repo.add_client(id,name,status)
        else:
            raise Exception ("ID must be a numeric value!")

        client=self.__client_repo.get_client_by_id(id)

        fc_undo=FunctionCall(self.remove_client,client.get_id)
        fc_redo=FunctionCall(self.add_client,client.get_id,client.get_name)

        cope = CascadedOperation()
        cope.add(Operation(fc_undo, fc_redo))

        self._undo_service.record_operation(cope)

    def remove_rental_by_client_id(self,id):
        for x in self.__rental_repo.get_rental_data():
            if str(x.get_client_id)==str(id):
                self.remove_rental(x.get_id)


    def remove_movie(self,id):

        id=str(id)

        movie = self.__movie_repo.get_movie_by_id(id)
        self.__movie_repo.remove_movie(id)

        #print(movie)
        fc_undo= FunctionCall(self.add_movie,movie.get_id,movie.get_title,movie.get_description,movie.get_genre)
        fc_redo = FunctionCall(self.remove_movie,movie.get_id)

        cope = CascadedOperation()
        cope.add(Operation(fc_undo, fc_redo))

        self._undo_service.record_operation(cope)

    def undo(self):
        self._undo_service.undo()

    def redo(self):
        self._undo_service.redo()

    def remove_client(self,id):
        client=self.__client_repo.get_client_by_id(id)

        cope = CascadedOperation()

        self.__client_repo.remove_client(id)


        fc_undo=FunctionCall(self.add_client,client.get_id,client.get_name)
        fc_redo=FunctionCall(self.remove_client,client.get_id)


        cope.add(Operation(fc_undo, fc_redo))

        fc_undo = FunctionCall(self.set_client_status, client.get_id, client.get_name, client.get_blacklist)
        fc_redo = 0



        cope.add(Operation(fc_undo, fc_redo))

        self._undo_service.record_operation(cope)

    def set_client_status(self,id,name,status):

        client=self.__client_repo.update_client(id,name,status)
        #client.set_blacklist(status)


    def update_movie(self,id,title,desc,genre):
        movie=self.__movie_repo.get_movie_by_id(id)
        movie_title=movie.get_title
        movie_desc=movie.get_description
        movie_gen=movie.get_genre
        self.__movie_repo.update_movie(id,title,desc,genre)

        fc_undo=FunctionCall(self.update_movie,movie.get_id,movie_title,movie_desc,movie_gen)
        fc_redo=FunctionCall(self.update_movie,movie.get_id,movie.get_title,movie.get_description,movie.get_genre)

        cope = CascadedOperation()
        cope.add(Operation(fc_undo, fc_redo))

        self._undo_service.record_operation(cope)

    def update_client(self,id,name,status):
        client=self.__client_repo.get_client_by_id(id)
        client_name=client.get_name
        client_status=client.get_blacklist
        self.__client_repo.update_client(id,name,status)

        fc_undo=FunctionCall(self.update_client,client.get_id,client_name,client_status)
        fc_redo=FunctionCall(self.update_client,client.get_id,client.get_name,client.get_blacklist)

        cope = CascadedOperation()
        cope.add(Operation(fc_undo, fc_redo))

        self._undo_service.record_operation(cope)

    def rent_movie(self,id,client_id,movie_id,rent_date,due_time,ret_date):

        aux = 0
        bl = 0
        for x in self.__client_repo.get_client_list():
            if str(x.get_id)==str(client_id):
                check=x
                aux=1
                if x.get_blacklist == True:
                    print(x.get_blacklist)
                    bl = 1

        if aux == 0:
            raise Exception("This client doesn't exist")

        if bl == 1:
            raise Exception("This client has been blacklisted, so he isn't allowed to rent movies from us anymore!")

        aux = 0
        for x in self.__movie_repo.get_movie_list():
            if str(x.get_id) == str(movie_id):
                aux = 1

        if aux == 0:
            raise Exception("This movie doesn't exist")


        aux = 0
        for x in self.__rental_repo.get_rental_data():
            if str(x.get_client_id) == str(client_id) and str(x.get_movie_id) == str(movie_id):
                aux = 1

        if aux == 1:
            raise Exception("This client already rented this movie")


        self.__rental_repo.rent_movie(id,client_id,movie_id,rent_date,due_time,ret_date)

        fc_undo=FunctionCall(self.remove_rental,id)
        fc_redo=FunctionCall(self.rent_movie,id,client_id,movie_id,rent_date,due_time,ret_date)

        cope = CascadedOperation()
        cope.add(Operation(fc_undo,fc_redo))
        self._undo_service.record_operation(cope)

    def remove_rental(self,id):
        list=self.__rental_repo.get_rental_data()
        for x in list:
            if str(x.get_id)==str(id):
                rental=x

        self.__rental_repo.remove_rental(rental)

    def return_movie(self,id,today_date):
        self.__rental_repo.return_movie(id,today_date,self.__movie_repo,self.__client_repo)

        fc_undo = FunctionCall(self.set_return_date,id,0)
        fc_redo = FunctionCall(self.return_movie,id,today_date)

        cope = CascadedOperation()
        cope.add(Operation(fc_undo, fc_redo))
        self._undo_service.record_operation(cope)

    def set_return_date(self,id,today_date):
        try:
            self.__rental_repo.set_return_movie(id,today_date,self.__movie_repo,self.__client_repo)
        except:
            raise Exception

    def search_client_id(self,word):
        """
        word: the id we're searching for

        return: the client object with the id equal to the given word
        """
        if word.isnumeric():
            word = int(word)
        else:
            raise Exception("The ID must be a numeric value")

        return self.__client_repo.search_client_id(word)

    @staticmethod
    def part_a_string(word):
        """
        splitting the string received as a parameter into separate words and returning them through a list
        """
        lis=[]

        lis=word.split(' ')

        return lis

    def search_client_name(self,word):
        """
        word: the string for which we're searching

        returns all the client objects that have their name similar to the word given
        """
        word=word.lower()
        lis=self.part_a_string(word)
        return self.__client_repo.search_client_name(lis)

    def search_client_status(self,word):
        """
        status: the string for which we're searching

        returns all the client objects that have their status similar to the given word
        """
        word=word.lower()
        return self.__client_repo.search_client_status(word)

    def search_movie_id(self,word):
        """
        word: the id we're searching for

        return: the movie object that has the same id as the one we're searching for
        """
        if word.isnumeric():
            word = int(word)
        else:
            raise Exception("The ID must be a numeric value")

        return self.__movie_repo.search_movie_id(word)

    def search_movie_name(self,word):
        """
        word: the string for which we're searching

        returns all the movie objects that have their description similar to the word given
        """
        word=word.lower()
        lis=self.part_a_string(word)
        list_of_movies=self.__movie_repo.get_movie_list()
        matching_list=[]

        for x in list_of_movies:
            list_of_names=self.part_a_string(self.__movie_repo.search_movie_name(x))
            #list_of_names=list_of_names.lower()
            #print(list_of_names,lis)
            ok=False
            for y in list_of_names:
                for k in lis:
                    if str(y.lower())==str(k):
                        if ok==False:
                            matching_list.append(x)
                            ok=True
        #print(matching_list)
        if matching_list==[]:
            raise Exception ("Couldn't find any movies to match your search...")
        return matching_list


    def search_movie_description(self,word):
        """
        word: the string for which we're searching

        returns all the movie objects that have their description similar to the word given
        """
        word=word.lower()
        lis=self.part_a_string(word)
        list_of_movies = self.__movie_repo.get_movie_list()
        matching_list = []

        for x in list_of_movies:
            list_of_descriptions = self.part_a_string(self.__movie_repo.search_movie_description(x))
            # list_of_names=list_of_names.lower()
            # print(list_of_names,lis)
            ok = False
            for y in list_of_descriptions:
                for k in lis:
                    if str(y.lower()) == str(k):
                        if ok == False:
                            matching_list.append(x)
                            ok = True
        # print(matching_list)
        if matching_list == []:
            raise Exception("Couldn't find any movies to match your search...")
        return matching_list

    def search_movie_genre(self,word):
        """
        word: the string for which we're searching
        searching for all the movies that have the genre similar to the parameter word
        """
        word=word.lower()
        lis=self.part_a_string(word)
        list_of_movies = self.__movie_repo.get_movie_list()
        matching_list = []

        for x in list_of_movies:
            list_of_genres = self.part_a_string(self.__movie_repo.search_movie_genre(x))
            # list_of_names=list_of_names.lower()
            # print(list_of_names,lis)
            ok = False
            for y in list_of_genres:
                for k in lis:
                    if str(y.lower()) == str(k):
                        if ok == False:
                            matching_list.append(x)
                            ok = True
        # print(matching_list)
        if matching_list == []:
            raise Exception("Couldn't find any movies to match your search...")
        return matching_list

    def most_rented_movies(self):
        """
        returns a sorted list in descending order based on how many days a movie was rented
        """
        list_of_movies=self.__movie_repo.get_movie_list()[:]
        list_of_rentals=self.__rental_repo.get_rental_data()
        list_of_days=[]
        list_of_ids=[]

        for y in list_of_movies:
            curr_days=0
            for x in list_of_rentals:
                if (str(x.get_movie_id)==str(y.get_id)):
                    curr_days=curr_days+self.__rental_repo.calculate_rental_days(x)
            curr_days=int(curr_days)
            list_of_days.append(curr_days)
            list_of_ids.append(y.get_id)
                #print(x.get_movie_id,curr_days.days)

        list_of_days, list_of_ids = zip(*sorted(zip(list_of_days, list_of_ids),reverse=True))

        return list_of_ids,list_of_days


    def get_movie_by_id(self,id):
        """
        returns a movie object by searching for it's id
        """
        return self.__movie_repo.get_movie_by_id(id)

    def most_active_clients(self):
        """
        returns a sorted list in descending order of the clients, based on their activity
        """
        list_of_clients = self.__client_repo.get_client_list()[:]
        list_of_rentals = self.__rental_repo.get_rental_data()
        list_of_days = []
        list_of_ids = []

        for y in list_of_clients:
            curr_days = 0
            for x in list_of_rentals:
                if (str(x.get_client_id) == str(y.get_id)):
                    curr_days = curr_days + self.__rental_repo.calculate_rental_days(x)
            curr_days = int(curr_days)
            list_of_days.append(curr_days)
            list_of_ids.append(y.get_id)
            # print(x.get_movie_id,curr_days.days)

        list_of_days, list_of_ids = zip(*sorted(zip(list_of_days, list_of_ids), reverse=True))

        return list_of_ids, list_of_days

    def get_client_by_id(self,id):
        """
        returns the entire client object by searching for its id
        """
        return self.__client_repo.get_client_by_id(id)

    def late_rentals(self):
        """
        computes how many movies are late in terms of returning at the current moment
        """
        list_of_movies = self.__movie_repo.get_movie_list()[:]
        list_of_rentals = self.__rental_repo.get_rental_data()
        list_of_days = []
        list_of_ids = []

        for y in list_of_movies:
            curr_days=0
            for x in list_of_rentals:
                if (str(x.get_movie_id) == str(y.get_id)):
                    curr_days = curr_days + self.__rental_repo.calculate_late_days(x)
            curr_days = int(curr_days)
            if curr_days!=0:
                list_of_days.append(curr_days)
                list_of_ids.append(y.get_id)

        try:
            list_of_days, list_of_ids = zip(*sorted(zip(list_of_days, list_of_ids), reverse=True))
        except:
            raise Exception ("There are no movies currently rented that are late.")

        return list_of_ids, list_of_days


    def sort_movies_by_ascending_id(self):
        list=data_structure.gnome_sort(self.__movie_repo.get_movie_list(),data_structure.ascending_id)
        return list

    def sort_movies_by_descending_id(self):
        list = data_structure.gnome_sort(self.__movie_repo.get_movie_list(),data_structure.descending_id)
        return list

    def sort_by_ascending_title(self):
        list = data_structure.gnome_sort(self.__movie_repo.get_movie_list(), data_structure.ascending_title)
        return list

    def sort_by_descending_title(self):
        list = data_structure.gnome_sort(self.__movie_repo.get_movie_list(), data_structure.descending_title)
        return list

    def sort_by_ascending_description(self):
        list = data_structure.gnome_sort(self.__movie_repo.get_movie_list(), data_structure.ascending_description)
        return list

    def sort_by_descending_description(self):
        list = data_structure.gnome_sort(self.__movie_repo.get_movie_list(), data_structure.descending_description)
        return list

    def sort_by_ascending_genre(self):
        list = data_structure.gnome_sort(self.__movie_repo.get_movie_list(), data_structure.ascending_genre)
        return list

    def sort_by_descending_genre(self):
        list = data_structure.gnome_sort(self.__movie_repo.get_movie_list(), data_structure.descending_genre)
        return list

    def sort_clients_by_ascending_id(self):
        list = data_structure.gnome_sort(self.__client_repo.get_client_list(), data_structure.ascending_id)
        return list

    def sort_clients_by_descending_id(self):
        list = data_structure.gnome_sort(self.__client_repo.get_client_list(), data_structure.descending_id)
        return list

    def sort_by_ascending_name(self):
        list = data_structure.gnome_sort(self.__client_repo.get_client_list(), data_structure.ascending_name)
        return list

    def sort_by_descending_name(self):
        list = data_structure.gnome_sort(self.__client_repo.get_client_list(), data_structure.descending_name)
        return list

    def sort_by_ascending_status(self):
        list = data_structure.gnome_sort(self.__client_repo.get_client_list(), data_structure.ascending_status)
        return list

    def sort_by_descending_status(self):
        list = data_structure.gnome_sort(self.__client_repo.get_client_list(), data_structure.descending_status)
        return list

    def sort_rentals_by_ascending_id(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.ascending_id)
        return list

    def sort_rentals_by_descending_id(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.descending_id)
        return list

    def sort_by_ascending_movie_id(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.ascending_movie_id)
        return list

    def sort_by_descending_movie_id(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.descending_movie_id)
        return list

    def sort_by_ascending_client_id(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.ascending_client_id)
        return list

    def sort_by_descending_client_id(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.descending_client_id)
        return list

    def sort_by_ascending_rent_date(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.ascending_rent_date)
        return list

    def sort_by_descending_rent_date(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.descending_rent_date)
        return list

    def sort_by_ascending_due_date(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.ascending_due_date)
        return list

    def sort_by_descending_due_date(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.descending_due_date)
        return list

    def sort_by_ascending_return_date(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.ascending_return_date)
        return list

    def sort_by_descending_return_date(self):
        list = data_structure.gnome_sort(self.__rental_repo.get_rental_data(), data_structure.descending_return_date)
        return list

    def filter_title(self,string):
        def something(x):
            return data_structure.filter_title(x,string)

        list = data_structure.filter(self.__movie_repo.get_movie_list(),something)
        return list

    def filter_movies_id(self,string):
        list = data_structure.general_filter(self.__movie_repo.get_movie_list(),data_structure.filter_id,string)
        return list

    def filter_description(self,string):
        list = data_structure.general_filter(self.__movie_repo.get_movie_list(),data_structure.filter_description,string)
        return list

    def filter_genre(self,string):
        list = data_structure.general_filter(self.__movie_repo.get_movie_list(),data_structure.filter_genre,string)
        return list