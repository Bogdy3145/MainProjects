import unittest
import repository
import datetime
import services
from UndoService import Operation,FunctionCall,CascadedOperation,UndoService

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = repository.Repo()
        self.movie=repository.MovieRepo()
        self.client=repository.ClientRepo()
        self.undo_service=UndoService()
        self.services=services.Functions(self.movie,self.client,self.repo,self.undo_service)



    def test_add_movie(self):

        self.movie.add_movie(1,"Film","A great movie","action")
        self.assertEqual(self.movie.get_movie_list()[0].get_id,1)
        self.assertEqual(self.movie.get_movie_list()[0].get_title,"Film")
        self.assertEqual(self.movie.get_movie_list()[0].get_description,"A great movie")
        self.assertEqual(self.movie.get_movie_list()[0].get_genre,"action")


    def test_add_client(self):

        self.client.add_client(1,"Bogdan")
        self.assertEqual(self.client.get_client_list()[0].get_id,1)
        self.assertEqual(self.client.get_client_list()[0].get_name,"Bogdan")
        self.assertEqual(self.client.get_client_list()[0].get_blacklist,False)
        # self.repo.add_student(1, "test", 912)
        # self.repo.update_student(1, "NEW TEST NAME", 99999)
        # self.assertEqual(self.repo.return_students_for_test()[0].student_id,1)
        # self.assertEqual(self.repo.return_students_for_test()[0].student_name, "NEW TEST NAME")
        # self.assertEqual(self.repo.return_students_for_test()[0].student_group ,99999)

    def test_remove_movie(self):
        self.movie.add_movie(1,"Film","A great movie","action")
        self.movie.remove_movie(1)
        self.assertEqual(self.movie.get_movie_list(),[])

        try:
            self.movie.remove_movie(1)
        except Exception as ex:
            self.assertEqual(str(ex),"The movie with the given ID does not exist!")

    def test_remove_client(self):
        self.client.add_client(1,"Bogdan")
        self.client.remove_client(1)
        self.assertEqual(self.client.get_client_list(),[])

        try:
            self.client.remove_client(1)
        except Exception as ex:
            self.assertEqual(str(ex),"The client with the given ID does not exist!")

    def test_update_client(self):
        self.client.add_client(1,"Bogdan")
        self.client.update_client(1,"Laur","False")

        self.assertEqual(self.client.get_client_list()[0].get_name,"Laur")
        self.assertEqual(self.client.get_client_list()[0].get_blacklist,False)


    def test_update_movie(self):
        self.movie.add_movie(1,"Movie","desc","action")
        self.movie.update_movie(1,"New title","new desc","new genre")


        self.assertEqual(self.movie.get_movie_list()[0].get_id,1)
        self.assertEqual(self.movie.get_movie_list()[0].get_title,"New title")
        self.assertEqual(self.movie.get_movie_list()[0].get_description,"new desc")
        self.assertEqual(self.movie.get_movie_list()[0].get_genre,"new genre")


    def test_rent_movie(self):
        self.movie.add_movie(2,"Movie","desc","action")
        self.client.add_client(3, "Bogdan")

        rent=datetime.date(year=2021,month=7,day=15)
        due=datetime.date(year=2021,month=9,day=15)
        ret=0

        self.repo.rent_movie(1,3,2,rent,due,ret,self.movie,self.client)
        self.assertEqual(self.repo.get_rental_data()[0].get_id,1)
        self.assertEqual(self.repo.get_rental_data()[0].get_client_id,3)
        self.assertEqual(self.repo.get_rental_data()[0].get_movie_id,2)
        self.assertEqual(self.repo.get_rental_data()[0].get_rented_date,rent)
        self.assertEqual(self.repo.get_rental_data()[0].get_due_date,due)
        self.assertEqual(self.repo.get_rental_data()[0].get_return_date,ret)


    def test_return_movie(self):
        self.movie.add_movie(2, "Movie", "desc", "action")
        self.client.add_client(3, "Bogdan")

        rent = datetime.date(year=2021, month=7, day=15)
        due = datetime.date(year=2021, month=9, day=15)
        ret = 0
        tod = datetime.date(year=2021,month=9, day=15)
        self.repo.rent_movie(1, 3, 2, rent, due, ret,self.movie,self.client)
        self.repo.return_movie(1,tod,self.movie,self.client)

        self.assertEqual(self.repo.get_rental_data()[0].get_return_date,tod)
        self.assertEqual(self.client.get_client_list()[0].get_blacklist,False)

        try:
            self.repo.return_movie(1, tod,self.movie,self.client)
        except Exception as ex:
            self.assertEqual(str(ex),"There must be a mistake, this movie appears to be with us already")

    def test_calculate_rental_days(self):
        self.movie.add_movie(2, "Movie", "desc", "action")
        self.client.add_client(3, "Bogdan")

        rent = datetime.date(year=2021, month=7, day=15)
        due = datetime.date(year=2021, month=9, day=15)
        ret = 0
        today=datetime.date.today()
        self.repo.rent_movie(1, 3, 2, rent, due, ret, self.movie, self.client)

        item=self.repo.get_rental_data()[0]

        self.assertEqual(self.repo.calculate_rental_days(item), (today - rent).days)        #1

        self.movie.add_movie(3, "SecondMovie", "desc", "action")

        rent = datetime.date(year=2021, month=7, day=15)
        due = datetime.date(year=2021, month=9, day=15)
        ret = datetime.date(year=2021, month=10, day=20)
        self.repo.rent_movie(2, 3, 3, rent, due, ret, self.movie, self.client)

        second_item=self.repo.get_rental_data()[1]

        self.assertEqual(self.repo.calculate_rental_days(second_item),(ret-rent).days)      #2

    def test_calculate_late_days(self):
        self.movie.add_movie(2, "Movie", "desc", "action")
        self.client.add_client(3, "Bogdan")

        rent = datetime.date(year=2021, month=7, day=15)
        due = datetime.date(year=2021, month=9, day=15)
        ret = 0
        today = datetime.date.today()
        self.repo.rent_movie(1, 3, 2, rent, due, ret, self.movie, self.client)

        item = self.repo.get_rental_data()[0]

        self.assertEqual(self.repo.calculate_late_days(item),(today-due).days)  #1


        self.movie.add_movie(3, "Movie", "desc", "action")

        rent = datetime.date(year=2021, month=7, day=15)
        due = datetime.date(year=2022, month=9, day=15)
        ret = 0
        today = datetime.date.today()
        self.repo.rent_movie(2, 3, 3, rent, due, ret, self.movie, self.client)

        item = self.repo.get_rental_data()[1]

        self.assertEqual(self.repo.calculate_late_days(item), 0)        #2



        self.movie.add_movie(4, "Movie", "desc", "action")

        rent = datetime.date(year=2021, month=7, day=15)
        due = datetime.date(year=2021, month=9, day=15)
        ret = datetime.date(year=2021, month=9, day=15)
        today = datetime.date.today()
        self.repo.rent_movie(3, 3, 4, rent, due, ret, self.movie, self.client)

        item = self.repo.get_rental_data()[2]

        self.assertEqual(self.repo.calculate_late_days(item), 0)

    def test_search_client_id(self):
        self.client.add_client(3, "Bogdan")
        self.client.add_client(2, "Bogdan Alexandru")
        self.client.add_client(1, "Alexandru")

        self.assertEqual(self.client.search_client_id(1),self.client.get_client_list()[2])

        try:
            self.client.search_client_id(5)
        except Exception as ex:
            self.assertEqual(str(ex),"There are no clients with that ID")

    def test_search_client_name(self):
        self.client.add_client(3, "Bogdan")
        self.client.add_client(2, "Bogdan Alexandru")
        self.client.add_client(1, "Alexandru")

        lis=[]
        lis.append(self.client.get_client_list()[0])
        lis.append(self.client.get_client_list()[1])
        lis.append(self.client.get_client_list()[2])

        #print(self.client.search_client_name('Bogdan'))

        self.assertEqual(self.services.search_client_name("bogdan alexandru"),lis)

        try:
            self.client.search_client_name("alala")
        except Exception as ex:
            self.assertEqual(str(ex),"There are no clients with such name.")

    def test_search_client_status(self):
        self.client.add_client(3, "Bogdan")
        self.client.add_client(2, "Bogdan Alexandru")
        self.client.add_client(1, "Alexandru")

        self.assertEqual(self.client.search_client_status("false"),self.client.get_client_list())

        self.client.get_client_list()[0].set_blacklist("True")
        lis=[]
        lis.append(self.client.get_client_list()[0])

        self.assertEqual(self.client.search_client_status("true"), lis)

    def test_search_movie_id(self):
        self.movie.add_movie(1,"movie","desc","gen")
        self.movie.add_movie(2,"film","descriere","action")
        self.movie.add_movie(3,"orice","desc","horror")

        self.assertEqual(self.movie.search_movie_id(1),self.movie.get_movie_list()[0])

    def test_search_movie_name(self):
        self.movie.add_movie(1,"movie","desc","gen")
        self.movie.add_movie(2,"film","descriere","action")
        self.movie.add_movie(3,"orice","desc","horror")

        lis=[]
        lis.append(self.movie.get_movie_list()[0])

        self.assertEqual(self.services.search_movie_name("movie"),lis)

        try:
            self.services.search_movie_name("alala")
        except Exception as ex:
            self.assertEqual(str(ex), "Couldn't find any movies to match your search...")

    def test_search_movie_description(self):
        self.movie.add_movie(1, "movie", "desc", "gen")
        self.movie.add_movie(2, "film", "descriere", "action")
        self.movie.add_movie(3, "orice", "desc", "horror")

        lis = []
        lis.append(self.movie.get_movie_list()[1])

        self.assertEqual(self.services.search_movie_description("descriere"), lis)

        try:
            self.services.search_movie_description("alala")
        except Exception as ex:
            self.assertEqual(str(ex), "Couldn't find any movies to match your search...")

    def test_search_movie_genre(self):
        self.movie.add_movie(1, "movie", "desc", "gen")
        self.movie.add_movie(2, "film", "descriere", "action")
        self.movie.add_movie(3, "orice", "desc", "horror")


        lis = []
        lis.append(self.movie.get_movie_list()[2])

        self.assertEqual(self.services.search_movie_genre("horror"), lis)

        try:
            self.services.search_movie_genre("alala")
        except Exception as ex:
            self.assertEqual(str(ex),"Couldn't find any movies to match your search...")
        #self.assertEqual(self.services.search_movie_genre("alal"),"Couldn't find any movies to match your search...")

    def test_most_rented_movies(self):
        self.movie.add_movie(1, "movie", "desc", "gen")
        self.movie.add_movie(2, "film", "descriere", "action")
        self.movie.add_movie(3, "orice", "desc", "horror")
        self.client.add_client(1, "Bogdan")
        self.client.add_client(2, "Bogdan Alexandru")
        self.client.add_client(3, "Alexandru")

        rent = datetime.date(year=2021, month=7, day=15)
        due = datetime.date(year=2021, month=9, day=15)
        ret = datetime.date(year=2021, month=9, day=15)
        today = datetime.date.today()
        self.repo.rent_movie(1,1,1, rent, due, ret, self.movie, self.client)




        rent = datetime.date(year=2020, month=7, day=15)
        due = datetime.date(year=2021, month=9, day=15)
        ret = datetime.date(year=2021, month=9, day=15)
        today = datetime.date.today()
        self.repo.rent_movie(2, 2, 2, rent, due, ret, self.movie, self.client)

        lis=(2,1,3)
        days = (427, 62, 0)


        self.assertEqual(self.services.most_rented_movies(),(lis,days))

    def test_most_active_clients(self):
        self.movie.add_movie(1, "movie", "desc", "gen")
        self.movie.add_movie(2, "film", "descriere", "action")
        self.movie.add_movie(3, "orice", "desc", "horror")
        self.client.add_client(1, "Bogdan")
        self.client.add_client(2, "Bogdan Alexandru")
        self.client.add_client(3, "Alexandru")

        rent = datetime.date(year=2021, month=7, day=15)
        due = datetime.date(year=2021, month=9, day=15)
        ret = datetime.date(year=2021, month=9, day=15)
        today = datetime.date.today()
        self.repo.rent_movie(1, 1, 1, rent, due, ret, self.movie, self.client)

        rent = datetime.date(year=2020, month=7, day=15)
        due = datetime.date(year=2021, month=9, day=15)
        ret = datetime.date(year=2021, month=9, day=15)
        today = datetime.date.today()
        self.repo.rent_movie(2, 3, 2, rent, due, ret, self.movie, self.client)


        self.assertEqual(self.services.most_active_clients(),((3,1,2),(427,62,0)))

    def test_late_rentals(self):

        try:
            self.services.late_rentals()
        except Exception as ex:
            self.assertEqual(str(ex),"There are no movies currently rented that are late.")

        self.movie.add_movie(1, "movie", "desc", "gen")
        self.movie.add_movie(2, "film", "descriere", "action")
        self.movie.add_movie(3, "orice", "desc", "horror")
        self.client.add_client(1, "Bogdan")
        self.client.add_client(2, "Bogdan Alexandru")
        self.client.add_client(3, "Alexandru")

        rent = datetime.date(year=2020, month=7, day=15)
        due = datetime.date(year=2020, month=9, day=15)
        ret = 0
        today = datetime.date.today()
        self.repo.rent_movie(1, 1, 1, rent, due, ret, self.movie, self.client)

        rent = datetime.date(year=2019, month=7, day=15)
        due = datetime.date(year=2020, month=9, day=15)
        ret = 0
        today = datetime.date.today()
        self.repo.rent_movie(2, 3, 2, rent, due, ret, self.movie, self.client)

        date=today-due

        self.assertEqual(self.services.late_rentals(),((2, 1), (date.days,date.days)))

    def test_random_generators(self):

        self.services.rental_random_generator(self.movie,self.client)

        self.assertEqual(len(self.movie.get_movie_list()),20)
        self.assertEqual(len(self.client.get_client_list()),20)
        self.assertEqual(len(self.repo.get_rental_data()),20)

    def test_service_get_movie_by_id(self):

        self.movie.add_movie(1,"BlaBla","wat","xd")

        self.assertEqual(self.services.search_movie_id("1"),self.movie.search_movie_id(1))

        try:
            self.services.search_movie_id("lolo")
        except Exception as ex:
            self.assertEqual(str(ex),"The ID must be a numeric value")

    def test_service_get_client_by_id(self):

        self.client.add_client(1,"bogdan")

        self.assertEqual(self.services.search_client_id("1"), self.client.search_client_id(1))

        try:
            self.services.search_client_id("lolo")
        except Exception as ex:
            self.assertEqual(str(ex), "The ID must be a numeric value")

    def test_record_operation(self):

        self.services.add_client("1","Bogdan")

        client=self.client.get_client_by_id("1")

        fc_undo = FunctionCall(self.services.remove_client, client.get_id)
        fc_redo = FunctionCall(self.services.add_client, client.get_id, client.get_name)

        cope = CascadedOperation()
        cope.add(Operation(fc_undo, fc_redo))

        #self.undo_service.record_operation(cope)

        self.assertEqual(len(self.undo_service.get_list()),1)


        self.services.add_client("2", "Bogdan")

        client = self.client.get_client_by_id("2")

        fc_undo = FunctionCall(self.services.remove_client, client.get_id)
        fc_redo = FunctionCall(self.services.add_client, client.get_id, client.get_name)

        cope = CascadedOperation()
        cope.add(Operation(fc_undo, fc_redo))

        self.undo_service.undo()

        self.assertEqual(len(self.undo_service.get_list()), 2)

        self.services.add_client("3", "Bogdan")

        client = self.client.get_client_by_id("3")

        fc_undo = FunctionCall(self.services.remove_client, client.get_id)
        fc_redo = FunctionCall(self.services.add_client, client.get_id, client.get_name)

        cope = CascadedOperation()
        cope.add(Operation(fc_undo, fc_redo))

        self.assertEqual(len(self.undo_service.get_list()), 2)

        try:
            self.undo_service.undo()
            self.undo_service.undo()
            self.undo_service.undo()
        except Exception as ex:
            self.assertEqual(str(ex),"There are no commands left to undo! :( ")


        self.undo_service.redo()
        self.undo_service.redo()

        self.assertEqual(len(self.client.get_client_list()),2)

        try:
            self.undo_service.redo()
        except Exception as ex:
            self.assertEqual(str(ex),"There are no commands left to redo! :(")

    def test_service_add_remove_movie(self):
        self.services.add_movie("1","title","desc","gen")

        self.assertEqual(len(self.undo_service.get_list()),1)

        self.services.remove_movie(1)

        self.assertEqual(len(self.movie.get_movie_list()),0)

    def test_service_add_client(self):
        self.services.add_client("1","Bogdan")

        self.assertEqual(len(self.undo_service.get_list()),1)

    def test_service_update_movie(self):
        self.services.add_movie("1", "title", "desc", "gen")

        self.services.update_movie("1","smth","smth","smth")

        self.assertEqual(len(self.undo_service.get_list()),2)

    def test_service_update_client(self):
        self.services.add_client("1","Bogdan")

        self.services.update_client("1","andrei","false")

        self.assertEqual(len(self.undo_service.get_list()),2)

    def test_remove_rental(self):
        self.services.add_client("1","Bogdan")
        self.services.add_movie("1","Movie","a","a")

        rent_date=datetime.date(year=2020,month=12,day=1)
        due_date=datetime.date(year=2021,month=12,day=1)

        self.services.rent_movie("1","1","1",rent_date,due_date,0)

        self.assertEqual(len(self.undo_service.get_list()),3)

        self.undo_service.undo()

        self.services.rent_movie("1", "1", "1", rent_date, due_date, 0)

        self.assertEqual(len(self.undo_service.get_list()),3)

        today_date=datetime.date(year=2020,month=12,day=15)
        self.services.return_movie("1",today_date)

        self.assertEqual(len(self.undo_service.get_list()),4)

        self.undo_service.undo()

    def tearDown(self) -> None:
        pass