import random
import string
import datetime
import time
"""
Implement the solution here. 
You may add other source files.
Make sure you commit & push the source code before the end of the test.

Solutions using user-defined classes will not be graded.
"""


def init_number():
    """
    We are generating 4 random digits and we keep composing a number out of them until we have one that doesn't start
    with 0. Then, we return it
    """
    while True:
        c1,c2,c3,c4=random.sample(range(0,9),4)
        start_number=c1*1000+c2*100+c3*10+c4
        if c1!=0:
            return start_number

def bad_number(x):
        """
        We are checking if the input from the user is a valid number
        int x: The input from the user
        return: True if the number is bad, False if it is good
        """
        if len(x)!=4:
            return True

        try:
            x=int(x)
        except:
            return True

        c4=int(x%10)
        c3=int(x/10%10)
        c2=int(x/100%10)
        c1=int(x/1000)


        if (c1==c2 or c1==c3 or c1==c4):
            return True
        elif (c2==c3 or c2==c4):
            return True
        elif (c3==c4):
            return True

        if (c1==0):
            return True

        if (c1>9):
            return True

        return False

def check_numbers(start_number,new_number):
    """
    start_number: The computer's number
    new_number: Our guess

    We are checking for codes and runners by checking each digit
    """
    c1=int(start_number%10)
    c2=int(start_number/10%10)
    c3=int(start_number/100%10)
    c4=int(start_number/1000)

    new_c1=int(new_number%10)
    new_c2=int(new_number/10%10)
    new_c3=int(new_number/100%10)
    new_c4=int(new_number/1000)

    codes=0
    runners=0

    if c1==new_c1:
        codes+=1
    else:
        if(c1==new_c2 or c1==new_c3 or c1==new_c4):
            runners+=1

    if c2==new_c2:
        codes+=1
    else:
        if c2==new_c1 or c2==new_c3 or c2==new_c4:
            runners+=1

    if c3==new_c3:
        codes+=1
    else:
        if c3==new_c1 or c3==new_c2 or c3==new_c4:
            runners+=1

    if c4==new_c4:
        codes+=1
    else:
        if c4==new_c1 or c4==new_c2 or c4==new_c3:
            runners+=1

    return codes,runners


"""                 
                    ^
                    |
                    |
Functions lay there |


UI part lays here...|
                    |
                    |
                    v

"""


def start():
    start_number=init_number()


    while int(time.perf_counter())<60:

        print("Time left: ",60-int(time.perf_counter()),"seconds")
        new_number=input()

        if int(time.perf_counter()>60):
            print("GAME OVER! You ran out of time...")
            return

        if new_number=='8086':
            print(start_number)
        else:
            if (bad_number(new_number)):
                print("GAME OVER! Computer won.")
                return
            new_number=int(new_number)
            curr_codes,curr_runners=check_numbers(start_number,new_number)

            print("Codes:",curr_codes, "\nRunners:", curr_runners)

            if curr_codes==4:
                print("Congratulations, you won! The number was indeed ",start_number)
                return

    print("GAME OVER! You ran out of time...")


start()



