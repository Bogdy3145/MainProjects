
import domain
from pprint import pprint

class Services:

    __lis=[]
    __undo_lis=[[]]
    __undo_cont=0

    def init_students(self):
        for i in range (10):
            s1=domain.StudentInit()
            self.__lis.append(s1)


    def add_student(self,id,fname,lname,gr):

        for i in self.__lis:
            if (id==i.id):
                raise Exception ("IDs cannot be the same")




        self.__undo_lis[self.__undo_cont]=self.__lis[:]
        self.__undo_cont += 1
        self.__undo_lis.append([])


        stud=domain.Student(id,fname,lname,gr)
        self.__lis.append(stud)

    def filter_students(self,gr):

        self.__undo_lis[self.__undo_cont] = self.__lis[:]
        self.__undo_cont += 1
        self.__undo_lis.append([])

        ok=True
        while ok==True:
            ok=False
            for i in self.__lis:

                if (int(gr)==int(i.group)):

                    self.__lis.remove(i)
                    ok=True

    def undo(self):

        if self.__undo_cont>0:
            self.__lis=self.__undo_lis[self.__undo_cont-1]

            self.__undo_lis.pop()
            self.__undo_cont-=1
        else:
            raise Exception ("Can't undo from here! You're at the beginning")


    def get_students(self):
        return self.__lis

