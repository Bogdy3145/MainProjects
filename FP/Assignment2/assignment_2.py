def print_menu():
    print("General menu. Choose one of the following options:")
    print("1. Add a new number to the list")
    print("2. Show the numbers in the list")
    print("3. Show the longest sequence in the list that consists only of real numbers")
    print("4. Show the longest sequence in the list that is made of consecutive number pairs having equal sum")
    print("5. Add a list of numbers")
    print("6. Press x or 6 to exit")

def show_list(lis,n):

    for i in range(n):
        if (int(lis[i][1])<0):
            print(i+1,". ", str(get_real(lis,i))+str(get_imaginary(lis,i))+"i")
        else:
            print(i + 1, ". ", str(get_real(lis,i)) + "+" + str(get_imaginary(lis,i)) +"i")

def print_properly(lis,i):

    if (int(lis[i][1]) < 0):
        print(str(get_real(lis,i))+str(get_imaginary(lis,i)))
    else:
        print(str(get_real(lis, i)) + "+" + str(get_imaginary(lis, i)) + "i")

def start():

    n=10
    lis=init_list();

    while True:
        print_menu()
        option = input()
        if option=="1":
            set_number(lis)
            n=n+1
        elif option=="2":
            show_list(lis,n)
        elif option=="3":
            seq_real_numbers(lis,n)
        elif option=="4":
            seq_equal_sum(lis)
        elif option=="5":
            n=n+set_list(lis)
        elif option=="x" or option=="6":
            return
        else:
            print("Invalid input, please respect the indications.")


"/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"


def init_list():
    lis=[]
    lis.append([3,1])
    lis.append([1,2])
    lis.append([3,1])
    lis.append([1,2])
    lis.append([3,0])
    lis.append([1,2])
    lis.append([3,0])
    lis.append([1,2])
    lis.append([3,1])
    lis.append([1,2])
    return lis

def set_list(lis):
    """

    :param lis: the list of numbers
    :return: we return n so we can know how many elements we added to this list
    """

    n=input("Choose how many elements you wish to introduce to the list: ")
    n=int(n)

    for i in range (n):
        set_number(lis)

    return n

def set_number(lis):
    q=create_complex()
    lis.append(q)


def create_complex():

    ok=True
    okk=True

    while(ok):
        try:
            real=int(input("Introduce the real part:"))
            ok=False
        except:
            print("Please add a number")
            ok=True

    while(okk):
        try:
            imag=int(input("Introduce the imaginary part:"))
            okk=False
        except:
            print("Please add a number")
            okk=True

    q=[real,imag]

    return q


def get_real(lis,i):
    return lis[i][0]

def get_imaginary(lis,i):
    return lis[i][1]



def seq_real_numbers(lis,n):
    """
    We know the last position in the sequence and the length of it, so we can easily print out the desired elements

    :param lis: the list of numbers
    :param n: the number of elements in the list
    :return: the sequence
    """
    p1,p2=property1(lis,n)

    if (p2==0):
        print("Sorry! There is no real number in the list.")
    else:
        for i in range(p2-p1,p2):
            print_properly(lis,i)




def property1(lis,n):
    """

    :param lis: the list of numbers
    :param n: the number of elements in the list
    :return: the length of the sequence and the position of the last element in this sequence
    """
    k=0
    k=int(k)
    maximum=0
    pos=0

    for i in range (n):

        if get_imaginary(lis,i)==0:
            k=k+1
        else:
            if k>maximum:
                maximum=k
                pos=i
            k=0


    if k > maximum:
        maximum = k
        pos=n

    return maximum,pos

def sum(lis,i,j):


    s1=get_real(lis,i)+get_real(lis,i+1)
    s2=get_imaginary(lis,i)+get_imaginary(lis,j)

    return s1,s2

def property2(lis):

    k=2
    maxim=0
    s=0
    real_sum,imaginary_sum=sum(lis,0,1)

    for i in range (1,len(lis)-1):
        nd_real_sum,nd_imaginary_sum=sum(lis,i,i+1)
        if real_sum==nd_real_sum and imaginary_sum==nd_imaginary_sum:
            k=k+1
        else:
            if k>maxim:
                maxim=k
                pos=i+1
            k=2
        real_sum=nd_real_sum
        imaginary_sum=nd_imaginary_sum

    if k > maxim:
        maxim = k
        pos = len(lis)

    return maxim,pos


def seq_equal_sum(lis):

    p1, p2 = property2(lis)

    for i in range(p2 - p1, p2):
        print_properly(lis, i)


start()
