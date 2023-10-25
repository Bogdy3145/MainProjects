import unittest
import repository
import datetime
import services
import data_structure

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = repository.Repo()
        self.movie=repository.MovieRepo()
        self.client=repository.ClientRepo()

    def test_sort(self):
        list=[1,4,2,9,5]
        self.assertEqual(data_structure.gnome_sort(list, data_structure.ascending_numbers),[1,2,4,5,9])
        self.assertEqual(data_structure.gnome_sort(list,data_structure.descending_numbers),[9,5,4,2,1])
        list=["abc","cba","bac"]
        self.assertEqual(data_structure.gnome_sort(list,data_structure.ascending_strings),["abc","bac","cba"])
        self.assertEqual(data_structure.gnome_sort(list,data_structure.descending_strings),["cba","bac","abc"])

    def test_sort_movies(self):
        self.movie.add_movie(1,"Movie","desc","genre")
        self.movie.add_movie(3,"Whats","aaa","z")
        self.movie.add_movie(2,"Boooo","bbb","c")


        list = data_structure.gnome_sort(self.movie.get_movie_list(), data_structure.ascending_id)
        self.assertEqual(list[1],self.movie.get_movie_by_id(2))

        list = data_structure.gnome_sort(self.movie.get_movie_list(), data_structure.descending_id)
        self.assertEqual(list[0], self.movie.get_movie_by_id(3))

        list = data_structure.gnome_sort(self.movie.get_movie_list(), data_structure.ascending_title)
        self.assertEqual(list[0],self.movie.get_movie_by_id(2))

        list = data_structure.gnome_sort(self.movie.get_movie_list(), data_structure.descending_title)
        self.assertEqual(list[0], self.movie.get_movie_by_id(3))

        list = data_structure.gnome_sort(self.movie.get_movie_list(), data_structure.ascending_description)
        self.assertEqual(list[0], self.movie.get_movie_by_id(3))

        list = data_structure.gnome_sort(self.movie.get_movie_list(), data_structure.descending_description)
        self.assertEqual(list[0], self.movie.get_movie_by_id(1))

        list = data_structure.gnome_sort(self.movie.get_movie_list(), data_structure.ascending_genre)
        self.assertEqual(list[0], self.movie.get_movie_by_id(2))

        list = data_structure.gnome_sort(self.movie.get_movie_list(), data_structure.descending_genre)
        self.assertEqual(list[0], self.movie.get_movie_by_id(3))

    def test_sort_clients(self):
        self.client.add_client(1,"Bogdan",True)
        self.client.add_client(2,"Andrei",False)
        self.client.add_client(3,"Marian",True)

        list = data_structure.gnome_sort(self.client.get_client_list(), data_structure.ascending_id)
        self.assertEqual(list[0], self.client.get_client_by_id(1))

        list = data_structure.gnome_sort(self.client.get_client_list(), data_structure.descending_id)
        self.assertEqual(list[0], self.client.get_client_by_id(3))

        list = data_structure.gnome_sort(self.client.get_client_list(), data_structure.ascending_name)
        self.assertEqual(list[0], self.client.get_client_by_id(2))

        list = data_structure.gnome_sort(self.client.get_client_list(), data_structure.descending_name)
        self.assertEqual(list[0], self.client.get_client_by_id(3))

        list = data_structure.gnome_sort(self.client.get_client_list(), data_structure.ascending_status)
        self.assertEqual(list[0], self.client.get_client_by_id(2))

        list = data_structure.gnome_sort(self.client.get_client_list(), data_structure.descending_status)
        self.assertEqual(list[0], self.client.get_client_by_id(3))


    def test_sort_rentals(self):
        self.movie.add_movie(1, "Movie", "desc", "genre")
        self.movie.add_movie(3, "Whats", "aaa", "z")
        self.movie.add_movie(2, "Boooo", "bbb", "c")

        self.client.add_client(1, "Bogdan", True)
        self.client.add_client(2, "Andrei", False)
        self.client.add_client(3, "Marian", True)

        rent = datetime.date(year=2021, month=7, day=15)
        due = datetime.date(year=2021, month=9, day=15)
        ret = 0

        self.repo.rent_movie(1,1,1,rent,due,ret)
        rent = datetime.date(year=2020, month=7, day=15)
        due = datetime.date(year=2020, month=9, day=15)
        ret = 0

        self.repo.rent_movie(2,2,1,rent,due,ret)
        rent = datetime.date(year=2021, month=5, day=15)
        due = datetime.date(year=2021, month=6, day=15)
        ret = 0

        self.repo.rent_movie(3,3,3,rent,due,ret)

        list = data_structure.gnome_sort(self.repo.get_rental_data(),data_structure.ascending_id)
        self.assertEqual(list[0],self.repo.get_rental_by_id(1))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.descending_id)
        self.assertEqual(list[0], self.repo.get_rental_by_id(3))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.ascending_movie_id)
        self.assertEqual(list[0], self.repo.get_rental_by_id(2))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.descending_movie_id)
        self.assertEqual(list[0], self.repo.get_rental_by_id(3))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.ascending_client_id)
        self.assertEqual(list[0], self.repo.get_rental_by_id(1))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.descending_client_id)
        self.assertEqual(list[0], self.repo.get_rental_by_id(3))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.ascending_rent_date)
        self.assertEqual(list[0],self.repo.get_rental_by_id(2))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.descending_rent_date)
        self.assertEqual(list[0], self.repo.get_rental_by_id(1))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.ascending_due_date)
        self.assertEqual(list[0], self.repo.get_rental_by_id(2))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.descending_due_date)
        self.assertEqual(list[0], self.repo.get_rental_by_id(1))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.ascending_return_date)
        self.assertEqual(list[0], self.repo.get_rental_by_id(1))

        list = data_structure.gnome_sort(self.repo.get_rental_data(), data_structure.descending_return_date)
        self.assertEqual(list[0], self.repo.get_rental_by_id(1))

    def test_filter(self):
        self.movie.add_movie(1,"TItle","desc","action")
        self.movie.add_movie(2,"Title","desc","horror")
        self.movie.add_movie(3,"smth","lol","action")

        list = data_structure.general_filter(self.movie.get_movie_list(),data_structure.filter_id,"1")
        self.assertEqual(list[0], self.movie.get_movie_by_id(1))

        self.movie.add_movie(2, "Title", "desc", "horror")
        self.movie.add_movie(3, "smth", "lol", "action")

        list = data_structure.general_filter(self.movie.get_movie_list(), data_structure.filter_title, "Title")

        self.assertEqual(list[0], self.movie.get_movie_by_id(2))

        self.movie.add_movie(3, "smth", "lol", "action")

        list = data_structure.general_filter(self.movie.get_movie_list(),data_structure.filter_description,"lol")
        self.assertEqual(list[0],self.movie.get_movie_by_id(3))

        self.movie.add_movie(2, "xd", "lol", "horror")

        list = data_structure.general_filter(self.movie.get_movie_list(),data_structure.filter_genre, "horror")
        self.assertEqual(list[0],self.movie.get_movie_by_id(2))

    def test_structure(self):
        list = data_structure.DataStructure()

        list.__add__(1)
        self.assertEqual(list.__getitem__(0),1)

        list.remove(1)
        self.assertEqual(len(list),0)

        list.append(1)
        self.assertEqual(list.__getitem__(0), 1)

        list.__delitem__(0)
        self.assertEqual(len(list), 0)

        list.__add__(1)
        list.__add__(2)

        self.assertEqual(list.__next__(),1)
        self.assertEqual(list.__next__(),2)


        self.assertEqual(list.__next__(),None)
        self.assertEqual(list.__next__(),None)


    def tearDown(self) -> None:
        pass

