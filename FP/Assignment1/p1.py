# Solve the problem from the first set here
def prime(n):
    """

        :param n: the number to check whether it's prime or not
        :return: 1 if n is prime, 0 if it is not

    """
    if n == 2:
        return 1
    else:
        if (n % 2 == 0 or n==1):
            return 0
        else:
            for i in range(2, int(n / 2)+1):
                if n % i == 0:
                    return 0
    return 1


def cautare(n):
    """

    :param n: the given number
    :return: the 2 prime numbers which added equal to the number n (if they exist)
    """
    gasit = 0
    for i in range(2, n):
        if prime(i) and gasit == 0:
            if prime(n - i):
                print("The prime numbers which added equal",n,"are", i,"and",n - i)
                gasit = 1
    if gasit == 0:
        print("There are no p1 and p2 such that p1+p2 =", n)

def cin():
    n = input("Introduce a number ")
    n = int(n)
    return n;


print (prime(1))
n=cin()
cautare(n)





