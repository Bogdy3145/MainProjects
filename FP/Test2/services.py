import random
from main import Taxi

class Function:

    def __init__(self,repo):
        self.__repo=repo

    def get_repo(self):
        return self.__repo.get_list()

    def add_ride(self,id,x,y):
        self.__repo.add_ride(id,x,y)

    def generate_random(self,counter):


        for i in range(counter):
            x=random.randint(0,100)
            y=random.randint(0,100)

            current_list=self.__repo.get_list()
            if len(current_list)==0:
                id=1
            else:
                id=current_list[-1].get_id() + 1

            ok=False

            while ok==False:

                if self.validate_ride(x,y):
                    self.__repo.add_ride(id,x,y)
                    ok=True


    def validate_ride(self,x,y):

        for l in self.__repo.get_list():
            #print(self.manhattan_distance(l.get_row,l.get_col,x,y))
            if self.manhattan_distance(l.get_row(),l.get_col(),x,y)<=5:
                return False

        return True


    def manhattan_distance(self,x1,y1,x2,y2):
        return abs(x2-x1)+abs(y2-y1)

    def add_ride_good(self,x,y,end_x,end_y):
        minimum=200

        for l in self.__repo.get_list():
            if self.manhattan_distance(l.get_row(),l.get_col(),x,y)<minimum:
                minimum=self.manhattan_distance(l.get_row(),l.get_col(),x,y)
                element=l

        element.set_fare(element.get_fare()+self.manhattan_distance(element.get_row(),element.get_col(),end_x,end_y))
        #self.__repo.add_fare(self.manhattan_distance(element.get_row(),element.get_col(),end_x,end_y))

        element.set_row(end_x)
        element.set_col(end_y)

    def simulate_ride(self,counter):
        counter=int(counter)
        for l in range (counter):
            ok=False
            while ok==False:
                x=random.randint(0,100)
                y=random.randint(0,100)

                end_x=random.randint(0,100)
                end_y=random.randint(0,100)

                if self.validate_simulation(x,y,end_x,end_y):
                    ok=True

            self.add_ride_good(x,y,end_x,end_y)


    def validate_simulation(self,x,y,end_x,end_y):
        if self.manhattan_distance(x,y,end_x,end_y)<10:
            return False
        return True

    