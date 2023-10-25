from main import Taxi
class Repo:

    def __init__(self):
        self.__data=[]

    def get_list(self):
        return self.__data

    def generate_random(self,x,y):
        pass

    def add_ride(self,id,x,y):
        a_taxi=Taxi(id,x,y)
        self.__data.append(a_taxi)



