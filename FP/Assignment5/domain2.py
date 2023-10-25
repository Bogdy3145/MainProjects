
import random


class Student:

    def __init__(self,id,fname,lname,group):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.group=group

class StudentInit:

    randomList=random.sample(range(10,100),10)
    print(randomList)
    cnt=-1
    randomFname=["Alex","Bogdan","Mircea"]
    random.shuffle(randomFname)
    randomLname=["Ion","Aioanei","Mariusel"]
    random.shuffle((randomLname))

    def __init__(self):
        StudentInit.cnt+=1
        self.id=self.randomList[StudentInit.cnt]
        self.fname=self.randomFname[StudentInit.cnt]
        self.lname=self.randomLname[StudentInit.cnt]



s1=StudentInit()
s2=StudentInit()

print(s1.id,s1.fname,s2.lname)
print(s2.id)