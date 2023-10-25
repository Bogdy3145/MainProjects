from main import Taxi
from repo import Repo
from services import Function

class UI:

    def __init__(self,functions):
        self.__func=functions

    def print_situation(self):
        for x in self.__func.get_repo():
            print(x)

    def start(self):

        x=input("Number of taxis: ")
        x=int(x)
        self.__func.generate_random(x)




        while True:
            self.print_situation()
            x=input('>>> ')
            try:
                x=int(x)
            except:
                print("Please introduce a available number")
            if x==0:
                return
            if x==1:
                row=int(input("row: "))
                col=int(input("col: "))
                end_row=int(input("end_row: "))
                end_col=int(input("end_col: "))
                self.__func.add_ride_good(row,col,end_row,end_col)

            if x==2:
                counter=input("nr of simulations: ")
                self.__func.simulate_ride(counter)

repo=Repo()
functions=Function(repo)
ui=UI(functions)

ui.start()

