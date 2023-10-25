# Solve the problem from the third set here
def prim(n):
    """

    :param n: the number to check whether it's prime or not
    :return: 1 if n is prime, 0 if it is not

    """
    if n == 2:
        return 1
    else:
        if n % 2 == 0 or n==1:
            return 0
        else:
            for i in range(2, int(n / 2)+1):
                if n % i == 0:
                    return 0
    return 1

def divizori(n,i):
    """

    :param n: the number itself
    :param i: the divisor to check whether it's prime or not
    :return: through k we return the number of times the divisor I will be shown instead of the number n

    """
    k=0

    if (n%i==0 and prim(i)):
        for l in range(i):
             k=k+1

    k=int(k)
    return k

def calcul(n):
    """

    :param n: the position where the element we are looking for is
    :return: the value on the position n

    """
    i = 1                                       #i represents the position, from 1-n
    x = 1                                       #x counts how many numbers we have so far in total
    while (x < n and i <= n):                   #The while repeats as long as we don't exceed the desired position
        if (prim(i) == 0):                      #We are checking for divisors only if the number ISN'T a prime number
            for l in range(2, int(i / 2) + 1):
                x = x + divizori(i, l)          #adding up the numbers in the variable x
                # print(x)
                if x >= n:                      #if x exceeds the desired position, it means that l is the number which is in the n position
                    return l

        else:                                   #if the initial position is a prime number it means it won't have any divisors, so we just add 1
            x = x + 1
            if x >= n:
                return i

        i = i + 1

def result(n):
    print()
    if n == 1:
        print("The element on position", n, "is 1")
    else:
        print("The element on position", n, "is", calcul(n))

def cin():
    n = input("Introduce the desired position ")
    n = int(n)
    return n




n=cin()

result(n)

