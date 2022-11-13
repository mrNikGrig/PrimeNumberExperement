import random
import time
import math
import rsa

arr = []
def rand(a, b):
    while True:
        n = random.randint(a, b)
        if (n in arr):
            pass
        else:
            arr.append(n)
            return n


def is_prime_number(n):
    if (n % 10 == 1) or (n % 10 == 3) or (n % 10 == 7) or (n % 10 == 9):
        for i in range(100):
            a = rand(33552419 + 1, n -2)
            if (math.gcd(a, n) != 1):
                return False
            if (pow(a, n - 1, n) != 1):
                return False
        f = open("finalChek.txt", "r")
        for i in f:
            if n % int(i) == 0:
                return False
        return True
    else:
        return False



def find_prime_number(n):
    while n % 6 != 0:
        n+=1
    i = n
    while True:
        if (i - 11) % 44 == 0:
            continue
        elif (i - 33) % 44 == 0:
            continue
        elif is_prime_number(i+1):#тут я допишу несколько условий для исключения спиралей в которых нет простых чисел(они пересекаются в некоторых моментах)
            return i+1
        elif is_prime_number(i+5):
            return i+5
        i += 6
        #print("попытка")



def main():
    t1 = time.time()
    n = find_prime_number(random.randint( 2 ** 2048, 2 ** 2049))
    n1 = find_prime_number(random.randint(2 ** 2047, 2 ** 2048))
    t2 = time.time()
    print(t2-t1)
    print(n)
    print(n1)

if __name__ == "__main__":
    '''f = open("finalChek.txt", "r")
    for i in f:
        print(i)'''
    main()
    '''t1 = time.time()
    n = rsa.newkeys(4096)
    t2 = time.time()
    print(t2-t1)
    print(n)'''
    #print(is_prime_number(459))