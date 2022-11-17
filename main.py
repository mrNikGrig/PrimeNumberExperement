import random
import time
import math
import rsa

arr = []
primeNumbers = []

def rand(a, b):#для теста ферма нужно, что бы числа не повторялись, тут я это проверяю
    while True:
        n = random.randint(a, b)
        if (n in arr):
            pass
        else:
            arr.append(n)
            return n


def is_prime_number(n):
    arr.clear()
    if (n % 10 == 1) or (n % 10 == 3) or (n % 10 == 7) or (n % 10 == 9):# проятые числа оканчиваются только на эти цифры
        if n <= 33552419:# до этого значения числа я высчитал, так что по чему бы просто не проверить их на наличие в файле
            for i in primeNumbers:
                if n < int(i):
                    return False
                elif n ==int(i):
                    return True
        for i in range(100):#это как раз тест ферма очень хотелось бы увидеть его доказательство. 100 - это константа взятая из статьи в хабре в её правильности я не уверен
            a = rand(5, n - 2)
            if (math.gcd(a, n) != 1):# ну для теста ферма числа должны быть взаимно простые
                return False #простые числа должны быть взаимно простыми со всеми
            if (pow(a, n - 1, n) != 1):# сам тест
                return False
        for i in primeNumbers[:500]:
            if n % int(i) == 0:# тут я пытаюсь отсеить числа карлмайка они не простые и удолетворяют тесту ферма. написано про них здесь https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%BE_%D0%9A%D0%B0%D1%80%D0%BC%D0%B0%D0%B9%D0%BA%D0%BB%D0%B0
                return False
        return True
    else:
        return False



def find_prime_number(n):
    while n % 6 != 0:
        n+=1
    i = n
    while True:
        if is_prime_number(i+1):# тут я иду по спиралям в которых содержатся простые числа
            return i+1
        elif is_prime_number(i+5):
            return i+5
        i += 6
        #print("попытка")


def factorization(n):#алгоритм для факторизации, это один из способов проверки числа на простоту
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            print(i)



def generatePrimeNumbers(colBits):
    primeNumbers.clear()
    f = open("finalChek.txt", "r")
    for i in f:
        primeNumbers.append(i)
    n = find_prime_number(random.randint( 2 ** (colBits // 2), 2 ** ((colBits//2) + 1)))
    n1 = find_prime_number(random.randint(2 ** ((colBits//2) -1) , 2 ** (colBits//2)))
    #print(n)
    #print(n1)

if __name__ == "__main__":
    myTime = []
    normalTime = []
    for i in range(100):
        t1 = time.time()
        generatePrimeNumbers(256)
        myTime.append(time.time() - t1)


        t1 = time.time()
        rsa.newkeys(256)
        normalTime.append(time.time() - t1)

    print("my median" + str(sum(myTime) / len(myTime)))
    print("normal people madian" + str(sum(normalTime) / len(normalTime)))

    myTime = []
    normalTime = []
    for i in range(100):
        t1 = time.time()
        generatePrimeNumbers(2048)
        myTime.append(time.time() - t1)

        t1 = time.time()
        rsa.newkeys(2048)
        normalTime.append(time.time() - t1)

    print("my median" + str(sum(myTime) / len(myTime)))
    print("normal people madian" + str(sum(normalTime) / len(normalTime)))

    myTime = []
    normalTime = []
    for i in range(100):
        t1 = time.time()
        generatePrimeNumbers(4096)
        myTime.append(time.time() - t1)

        t1 = time.time()
        rsa.newkeys(4096)
        normalTime.append(time.time() - t1)

    print("my median" + str(sum(myTime) / len(myTime)))
    print("normal people madian" + str(sum(normalTime) / len(normalTime)))


