class Taxi:

    def __init__(self,id,row,col):
        self.__fare=0
        self.__id=id
        self.__row=row
        self.__col=col

    def get_id(self):
        return self.__id

    def get_fare(self):
        return self.__fare

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__col

    def set_fare(self,new_fare):
        self.__fare=new_fare

    def set_row(self,new_row):
        self.__row=new_row

    def set_col(self,new_col):
        self.__col=new_col

    def __str__(self):
        return "ID: " + str(self.__id) + " ROW: " + str(self.__row) + " COL: "+ str(self.__col) + " FARE: " +str(self.__fare)



