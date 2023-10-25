import unittest
#from repo import Repo
#from services import Function
from main import Player,Computer
from table import PlayingTable

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.player=Player()
        self.computer=Computer()

        self.table=PlayingTable(6)

    def test_strike(self):
        self.table.strike(1,1,"X")

        self.assertEqual(self.table.get_table()[1][1],"X")
        self.assertEqual(self.table.get_table()[2][2],-1)
        self.assertEqual(self.table.get_table()[0][0],-1)
        self.assertEqual(self.table.get_table()[0][1],-1)
        self.assertEqual(self.table.get_table()[2][1],-1)
        self.assertEqual(self.table.get_table()[2][2],-1)
        self.assertEqual(self.table.get_table()[1][2],-1)

        try:
            self.table.strike(1,1,"X")
        except Exception as ex:
            self.assertEqual(str(ex),"You can't strike in this place!")

        #self.assertEqual(self.table.strike(1,1,"X"),"You can't strike in this place!")

    def test_game_is_won(self):
        self.table.strike(0,0,"X")
        self.table.strike(0,3,"O")
        self.table.strike(0, 5, "X")
        self.table.strike(3,0,"O")
        self.table.strike(3, 3, "X")
        self.table.strike(3, 5, "O")
        self.table.strike(5, 0, "X")
        self.table.strike(5, 3, "O")
        self.table.strike(5, 5, "X")

        self.assertEqual(self.table.game_is_won(),True)


    def test_repair_last_move(self):
        self.table.strike(3,3,"X")
        self.table.repair_last_move(3,3)
        self.assertEqual(self.table.get_table()[3][3],0)



    def tearDown(self) -> None:
        pass