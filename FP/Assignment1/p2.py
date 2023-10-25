# Solve the problem from the second set here
from array import *

def fibo(n):
    """

    :param n: the number from the input
    :return: the number from the Fibonacci sequence that is greater than the given n
    """
    l = []                  #creating the list and adding it's first 2 elements
    l.append(1)
    l.append(1)

    i = 1

    while (l[i] <= n):      #while the current number from the Fibonacci list is still smaller than n, we are looking for the next one
        i = i + 1
        l.append(l[i - 1] + l[i - 2])

    return l[i]

def result():
    print("The smallest number from the Fibonacci sequence greater than the given number is", fibo(n))

def cin():
    n = input("Introduce a number ")
    n = int(n)
    return n;


n=cin()
result()