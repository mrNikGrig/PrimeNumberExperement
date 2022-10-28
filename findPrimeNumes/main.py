import time
import math


def is_prime_number(n):
    is_pn = True
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            is_pn = False
            break
    return is_pn


def find_prime_number(n):
    while n % 6 != 0:
        n+=1
    for i in range(n, 9999999999999, 6):
        if is_prime_number(i+1):
            return i+1
        elif is_prime_number(i+5):
            return i+5



def main():
    t1 = time.time()
    n = find_prime_number(21000000)
    t2 = time.time()
    print(t2-t1)
    print(n)

if __name__ == "__main__":
    main()