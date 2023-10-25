from domain import Client,Movie,Rental

class DataStructure():

    def __init__(self):
        self.__data=[]
        self.__index=0

    def __add__(self, other):
        self.__data.append(other)

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        self.__data[key]=value

    def __delitem__(self, key):
        del self.__data[key]

    def __next__(self):
        try:
            item=self.__data[self.__index]
            self.__index += 1
            return item
        except IndexError:
            pass

    # def __iter__(self):
    #     return self

    def __str__(self):
        return str(self.__data)

    def append(self,other):
        self.__data.append(other)

    def remove(self,key):
        del self.__data[key]

ds=DataStructure()

ds.__add__(1)
ds.__add__(2)

myiter=iter(ds)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


def gnome_sort(list,sort_type):
    index = 0
    while index < len(list):
        if index == 0:
            index = index + 1
        if sort_type(list[index-1],list[index]):
            index = index + 1
        else:
            list[index], list[index - 1] = list[index - 1], list[index]
            index = index - 1

    return list


def ascending_numbers(x,y):
    if x<=y:
        return True
    return False


def descending_numbers(x,y):
    if x>=y:
        return True
    return False


def ascending_strings(x,y):
    if x<=y:
        return True
    return False


def descending_strings(x,y):
    if x>=y:
        return True
    return False


def ascending_id(x,y):
    if x.get_id<=y.get_id:
        return True
    return False


def descending_id(x,y):
    if x.get_id>=y.get_id:
        return True
    return False


def ascending_name(x,y):
    x_name=x.get_name.lower()
    y_name=y.get_name.lower()
    return ascending_strings(x_name,y_name)


def descending_name(x,y):
    x_name=x.get_name.lower()
    y_name=y.get_name.lower()
    return descending_strings(x_name,y_name)


def ascending_status(x,y):
    if x.get_blacklist <= y.get_blacklist:
        return True
    return False


def descending_status(x,y):
    if x.get_blacklist >= y.get_blacklist:
        return True
    return False


def ascending_title(x,y):
    x_tit=x.get_title.lower()
    y_tit=y.get_title.lower()
    return ascending_strings(x_tit,y_tit)


def descending_title(x, y):
    x_tit = x.get_title.lower()
    y_tit = y.get_title.lower()
    return descending_strings(x_tit,y_tit)


def ascending_description(x,y):
    x_desc = x.get_description.lower()
    y_desc = y.get_description.lower()
    return ascending_strings(x_desc,y_desc)


def descending_description(x,y):
    x_desc=x.get_description.lower()
    y_desc=y.get_description.lower()
    return descending_strings(x_desc,y_desc)


def ascending_genre(x,y):
    x_gen=x.get_genre.lower()
    y_gen=y.get_genre.lower()
    return ascending_strings(x_gen,y_gen)


def descending_genre(x,y):
    x_gen = x.get_genre.lower()
    y_gen = y.get_genre.lower()
    return descending_strings(x_gen,y_gen)


def ascending_movie_id(x,y):
    x_id=int(x.get_movie_id)
    y_id=int(y.get_movie_id)
    return ascending_numbers(x_id,y_id)


def descending_movie_id(x,y):
    x_id=int(x.get_movie_id)
    y_id=int(y.get_movie_id)
    return descending_numbers(x_id,y_id)


def ascending_client_id(x,y):
    x_id=int(x.get_client_id)
    y_id=int(y.get_client_id)
    return ascending_numbers(x_id,y_id)


def descending_client_id(x,y):
    x_id=int(x.get_client_id)
    y_id=int(y.get_client_id)
    return descending_numbers(x_id,y_id)


def ascending_rent_date(x,y):
    x_date=x.get_rented_date
    y_date=y.get_rented_date
    return ascending_numbers(x_date,y_date)


def descending_rent_date(x,y):
    x_date = x.get_rented_date
    y_date = y.get_rented_date
    return descending_numbers(x_date,y_date)


def ascending_due_date(x,y):
    x_date=x.get_due_date
    y_date=y.get_due_date
    return ascending_numbers(x_date,y_date)


def descending_due_date(x,y):
    x_date=x.get_due_date
    y_date=y.get_due_date
    return descending_numbers(x_date,y_date)


def ascending_return_date(x,y):
    x_date=x.get_return_date
    y_date=y.get_return_date
    return ascending_numbers(x_date,y_date)


def descending_return_date(x,y):
    x_date = x.get_return_date
    y_date = y.get_return_date
    return ascending_numbers(x_date, y_date)


def filter(list,criteria):
    for x in list:
        if criteria(x):
            pass
        else:
            del(x)


def filter_title(x,y):
    if x.get_title=="movie":
        return True
    return False





c1=Client(1,"Bogdan",True)
c2=Client(2,"Andrei",False)
c3=Client(3,"Mata",False)

m1=Movie(1,"Movie","desc","gen")
m2=Movie(2,"Alo","zet","Jet")
m3=Movie(3,"Da","nu","ce")



list=[m1,m2,m3]


#list=(gnome_sort(list,ascending_genre))
