<<<<<<< HEAD
__author__ = 'Michael'
import math
from lxml import html
import requests


def multiple_3_5(n):
    ans = 0
    mul3 = 3
    mul5 = 5
    mul_list = []
    while mul3 < n:
        if not mul3 in mul_list:
            mul_list.append(mul3)
        mul3 += 3
    while mul5 < n:
        if not mul5 in mul_list:
            mul_list.append(mul5)
        mul5 += 5
    for x in mul_list:
        ans += x
    print ans

def even_fib():
    prev = 1
    curr = 2
    sum = 0
    while curr < 4000000:
        if curr % 2 == 0:
            sum += curr
        temp = curr
        curr += prev
        prev = temp
    print sum

def largest_prime_factor(n):
    # finding a list of prime numbers
    # prime_list = []
    # for num in range(3,10000,2):
    #     if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
    #         prime_list.append(num)
    x = 2
    while n > x:
        if n % x == 0:
            n /= x
            x = 2
        else:
            x += 1
    print n

def check_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True

def largest_palindrome_product():
    largest = 0
    for x in xrange(100, 999):
        for y in xrange(100, 999):
            if check_palindrome(x * y):
                if largest < x * y:
                    largest = x * y
    print largest

def smallest_multiple():
    smallest = 20
    while True:
        if smallest % 20 == 0:
            if smallest % 19 == 0:
                if smallest % 18 == 0:
                    if smallest % 17 == 0:
                        if smallest % 16 == 0:
                            if smallest % 15 == 0:
                                if smallest % 14 == 0:
                                    if smallest % 13 == 0:
                                        if smallest % 12 == 0:
                                            if smallest % 11 == 0:
                                                    print smallest
                                                    break
        smallest += 1

def sum_sq_diff():
    sum_sq = 0
    for x in xrange(1, 101):
        sum_sq += x
    sum_sq *= sum_sq
    sq_sum = 0
    for x in xrange(1, 101):
        sq_sum += x*x
    print sum_sq - sq_sum

def prime():
    # get 10001st prime number
    count = 1
    i = 1
    while count < 10001:
        i += 2
        for k in range(2, 1+int(math.sqrt(i+1))):
            if i%k == 0:
                break
        else:
            count += 1
    print i

def largest_product(n):
    product = 0
    for x in xrange (0, len(n)-13):
        temp_product = int(n[x])
        for y in xrange(1,13):
            temp_product *= int(n[x+y])
        if temp_product > product:
            product = temp_product
    print product

def special_py_triplet():
    for x in xrange(1,1000):
        y = x+1
        z = y+1
        while z <= 1000:
            while z * z < x * x + y * y:
                z = z + 1

            if z * z == x * x + y * y and z <= 1000:
                if x + y + z == 1000:
                    print x*y*z
                    return

            y = y + 1
    # alternate slower sqrt method
    # for x in 1 .. N
    # for y in x+1 .. N
    #     z = (int) sqrt(x * x + y * y)
    #     if z * z == x * x + y * y then use x, y, z

def sum_prime(n):
    sum = 0
    for num in range(3, n, 2):
        if all(num %i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            sum += num
    sum += 2
    print sum

if __name__ == '__main__':
    #multiple_3_5(1000)
    #even_fib()
    #largest_prime_factor(600851475143)
    #largest_palindrome_product()
    #smallest_multiple()
    #sum_sq_diff()
    #prime()
#     largest_product("73167176531330624919225119674426574742355349194934"
# "96983520312774506326239578318016984801869478851843"
# "85861560789112949495459501737958331952853208805511"
# "12540698747158523863050715693290963295227443043557"
# "66896648950445244523161731856403098711121722383113"
# "62229893423380308135336276614282806444486645238749"
# "30358907296290491560440772390713810515859307960866"
# "70172427121883998797908792274921901699720888093776"
# "65727333001053367881220235421809751254540594752243"
# "52584907711670556013604839586446706324415722155397"
# "53697817977846174064955149290862569321978468622482"
# "83972241375657056057490261407972968652414535100474"
# "82166370484403199890008895243450658541227588666881"
# "16427171479924442928230863465674813919123162824586"
# "17866458359124566529476545682848912883142607690042"
# "24219022671055626321111109370544217506941658960408"
# "07198403850962455444362981230987879927244284909188"
# "84580156166097919133875499200524063689912560717606"
# "05886116467109405077541002256983155200055935729725"
# "71636269561882670428252483600823257530420752963450")
    #special_py_triplet()
    sum_prime(2000000)

=======
__author__ = 'Michael'
import math
from lxml import html
import requests


def multiple_3_5(n):
    ans = 0
    mul3 = 3
    mul5 = 5
    mul_list = []
    while mul3 < n:
        if not mul3 in mul_list:
            mul_list.append(mul3)
        mul3 += 3
    while mul5 < n:
        if not mul5 in mul_list:
            mul_list.append(mul5)
        mul5 += 5
    for x in mul_list:
        ans += x
    print ans

def even_fib():
    prev = 1
    curr = 2
    sum = 0
    while curr < 4000000:
        if curr % 2 == 0:
            sum += curr
        temp = curr
        curr += prev
        prev = temp
    print sum

def largest_prime_factor(n):
    # finding a list of prime numbers
    # prime_list = []
    # for num in range(3,10000,2):
    #     if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
    #         prime_list.append(num)
    x = 2
    while n > x:
        if n % x == 0:
            n /= x
            x = 2
        else:
            x += 1
    print n

def check_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True

def largest_palindrome_product():
    largest = 0
    for x in xrange(100, 999):
        for y in xrange(100, 999):
            if check_palindrome(x * y):
                if largest < x * y:
                    largest = x * y
    print largest

def smallest_multiple():
    smallest = 20
    while True:
        if smallest % 20 == 0:
            if smallest % 19 == 0:
                if smallest % 18 == 0:
                    if smallest % 17 == 0:
                        if smallest % 16 == 0:
                            if smallest % 15 == 0:
                                if smallest % 14 == 0:
                                    if smallest % 13 == 0:
                                        if smallest % 12 == 0:
                                            if smallest % 11 == 0:
                                                    print smallest
                                                    break
        smallest += 1

def sum_sq_diff():
    sum_sq = 0
    for x in xrange(1, 101):
        sum_sq += x
    sum_sq *= sum_sq
    sq_sum = 0
    for x in xrange(1, 101):
        sq_sum += x*x
    print sum_sq - sq_sum

def prime():
    # get 10001st prime number
    count = 1
    i = 1
    while count < 10001:
        i += 2
        for k in range(2, 1+int(math.sqrt(i+1))):
            if i%k == 0:
                break
        else:
            count += 1
    print i

def largest_product(n):
    product = 0
    for x in xrange (0, len(n)-13):
        temp_product = int(n[x])
        for y in xrange(1,13):
            temp_product *= int(n[x+y])
        if temp_product > product:
            product = temp_product
    print product

def special_py_triplet():
    for x in xrange(1,1000):
        y = x+1
        z = y+1
        while z <= 1000:
            while z * z < x * x + y * y:
                z = z + 1

            if z * z == x * x + y * y and z <= 1000:
                if x + y + z == 1000:
                    print x*y*z
                    return

            y = y + 1
    # alternate slower sqrt method
    # for x in 1 .. N
    # for y in x+1 .. N
    #     z = (int) sqrt(x * x + y * y)
    #     if z * z == x * x + y * y then use x, y, z

def sum_prime(n):
    sum = 0
    for num in range(3, n, 2):
        if all(num %i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            sum += num
    sum += 2
    print sum

if __name__ == '__main__':
    #multiple_3_5(1000)
    #even_fib()
    #largest_prime_factor(600851475143)
    #largest_palindrome_product()
    #smallest_multiple()
    #sum_sq_diff()
    #prime()
#     largest_product("73167176531330624919225119674426574742355349194934"
# "96983520312774506326239578318016984801869478851843"
# "85861560789112949495459501737958331952853208805511"
# "12540698747158523863050715693290963295227443043557"
# "66896648950445244523161731856403098711121722383113"
# "62229893423380308135336276614282806444486645238749"
# "30358907296290491560440772390713810515859307960866"
# "70172427121883998797908792274921901699720888093776"
# "65727333001053367881220235421809751254540594752243"
# "52584907711670556013604839586446706324415722155397"
# "53697817977846174064955149290862569321978468622482"
# "83972241375657056057490261407972968652414535100474"
# "82166370484403199890008895243450658541227588666881"
# "16427171479924442928230863465674813919123162824586"
# "17866458359124566529476545682848912883142607690042"
# "24219022671055626321111109370544217506941658960408"
# "07198403850962455444362981230987879927244284909188"
# "84580156166097919133875499200524063689912560717606"
# "05886116467109405077541002256983155200055935729725"
# "71636269561882670428252483600823257530420752963450")
    #special_py_triplet()
    sum_prime(2000000)

>>>>>>> origin/master
