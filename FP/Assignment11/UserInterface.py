from table import PlayingTable
from main import Player,Computer
from colorama import Fore, Back, Style

class UI:

    def __init__(self):
        self.local_table=PlayingTable(6)

    def print_table(self):
        pass

    def start(self):

        x=input("Press 1 if you want to start first or 2 otherwise: ")
        # local_table = PlayingTable(6)
        player = Player()
        computer = Computer()
        if x == "1":

            print(self.local_table)
            while x!="0":
                current_row=input("Coordinate for row: ")
                current_col=input("Coordinate for colon: ")

                try:
                    player.player_move(current_row,current_col,self.local_table)
                    #local_table.strike(current_row,current_col)
                    print(self.local_table)
                    if self.local_table.game_is_won():
                        print("Congratulations! You win!")
                        return
                    computer.computer_move(self.local_table)
                    print(self.local_table)
                    if self.local_table.game_is_won():
                        print("Hehe.. I win!")
                        return

                    #print(Fore.BLUE + "watever")


                except Exception as ex:
                    print(self.local_table)
                    print(str(ex))
            x=input()
        elif x == "2":
            print(self.local_table)
            while x != "0":


                try:
                    computer.computer_move(self.local_table)
                    print(self.local_table)
                    if self.local_table.game_is_won():
                        print("Hehe.. I win!")
                        return

                    current_row = input("Coordinate for row: ")
                    current_col = input("Coordinate for colon: ")

                    player.player_move(current_row, current_col, self.local_table)
                    # local_table.strike(current_row,current_col)
                    print(self.local_table)
                    if self.local_table.game_is_won():
                        print("Congratulations! You win!")
                        return


                except Exception as ex:
                    print(self.local_table)
                    print(str(ex))
            x=input()
        else:
            print("Invalid input!")



        #x=input()


start=UI()

start.start()

