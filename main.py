import random
import time
import math
#import rsa

def is_prime_number(n):
    if pow(n, n-2, n-1) == 1:# это условие должно по идее отсеивать числа которые не выполняют условие теоремы ферма но без него оно работает точно за то же время
        if (n%10 == 1) or (n%10 == 3) or (n%10 == 7) or (n%10 == 9):
            for i in range(3, int(math.sqrt(n))+1, 2):
                if (n % i == 0):
                    return False
            return True
        else:
            return False
    else:
        return False



def find_prime_number(n):
    while n % 6 != 0:
        n+=1
    for i in range(n, 9999999999999999999999999999999999999, 6):
        if is_prime_number(i+1):#тут я допишу несколько условий для исключения спиралей в которых нет простых чисел(они пересекаются в некоторых моментах)
            return i+1
        elif is_prime_number(i+5):
            return i+5



def main():
    t1 = time.time()
    n = find_prime_number(2 ** 50)
    t2 = time.time()
    print(t2-t1)
    print(n)
    #print(n1)

if __name__ == "__main__":
    main()
    '''t1 = time.time()
    rsa.newkeys(108)
    t2 = time.time()
    print(t2-t1)'''
    #print(is_prime_number(13))