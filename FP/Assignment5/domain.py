
import random


class Student:


    def __init__(self,id,fname,lname,group):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.group=group


    def __str__(self):
        return str(self.id) + ' ' + self.fname + ' ' + self.lname + ' ' + str(self.group)

    def get_id(self):
        return self.id




class StudentInit():

    cnt = -1

    randomList=random.sample(range(10,100),10)

    randomFname=["Alex","Bogdan","Mircea","Victor","Deian","Messi","Haaland","Veratti","Florin","Gheorghe"]
    random.shuffle(randomFname)
    randomLname=["Ion","Aioanei","Mariusel","Cretu","Miguel","Martini","Ololosh","Rapunzel","Janu","Salam"]
    random.shuffle((randomLname))

    #randomGroup=random.sample(range(1,5),4)


    def __init__(self):
        StudentInit.cnt+=1
        self.id=self.randomList[StudentInit.cnt]
        self.fname=self.randomFname[StudentInit.cnt]
        self.lname=self.randomLname[StudentInit.cnt]
        self.group=random.randint(1,5)

    def full_name(self):
        return str(self.fname) + ' ' + str(self.lname)



#print(s1.id,s1.fname,s1.lname,s1.group)
#print(s2.id)

"""

    cnt = -1

    randomList = random.sample(range(10, 100), 10)

    randomFname = ["Alex", "Bogdan", "Mircea", "Victor", "Deian", "Messi", "Haaland", "Veratti", "Florin", "Gheorghe"]
    random.shuffle(randomFname)
    randomLname = ["Ion", "Aioanei", "Mariusel", "Cretu", "Miguel", "Martini", "Ololosh", "Rapunzel", "Janu", "Salam"]
    random.shuffle((randomLname))

    # randomGroup=random.sample(range(1,5),4)

    def __init__(self):
        Student.cnt += 1
        self.id = self.randomList[Student.cnt]
        self.fname = self.randomFname[Student.cnt]
        self.lname = self.randomLname[Student.cnt]
        self.group = random.randint(1, 5)
"""