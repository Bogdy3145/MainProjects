import unittest
from repo import Repo
from services import Function
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.repo=Repo()
        self.func=Function(self.repo)

    def test_add_ride_good(self):

        self.func.add_ride(1,15,20)

        self.func.add_ride_good(20,25,40,40)

        self.assertEqual(self.repo.get_list()[0].get_row(),40)
        self.assertEqual(self.repo.get_list()[0].get_col(),40)

        self.assertEqual(self.repo.get_list()[0].get_fare(),45)


    def tearDown(self) -> None:
        pass