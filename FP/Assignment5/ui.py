
import domain
from services import Services
import tests


class StudentUI:


    @staticmethod
    def __show_menu():
        print("    1. Add a student.")
        print("    2. Display the list of students.")
        print("    3. Filter the list so that students in a given group are deleted from the list.")
        print("    4. Undo the last operation that modified program data.")
        print()

    @staticmethod
    def read_student_data(func):
        id=input("Introduce an ID: ")
        f=input("Introduce first name: ")
        l=input("Introduce last name: ")
        gr=input("Introduce group: ")

        try:
            func.add_student(id,f,l,gr)
        except Exception as ex:
            print(ex)



    @staticmethod
    def start(s):
        tests.run_tests()
        s.init_students()
        while True:

            StudentUI.__show_menu()
            x=input(">>> ")
            if (x=="0"):
                return 0

            elif x=="1":
                StudentUI.read_student_data(s)

            elif x=="2":
                print("\n \n")
                for x in s.get_students():
                    print(x)
                print("\n \n")

            elif x=="3":
                i=input("Enter desired group: ")
                s.filter_students(i)

            elif x=="4":
                try:
                    s.undo()
                except Exception as ex:
                    print(ex)



s=Services()

StudentUI.start(s)