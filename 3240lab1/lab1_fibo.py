<<<<<<< HEAD
__author__ = 'Michael'


def fibonacci1(a):
    if a < 0:
        raise ValueError()
    if a == 0:
        return "Please enter a positive integer, n, to find the n-th fibonacci number"
    if a == 1 or a == 2:
        return 1
    num1 = 1;
    num2 = 1;
    total = 0;
    for x in xrange(2, a):
        total = num1 + num2
        num1 = num2
        num2 = total
    return total

def fibonacci2(param):
    myList = [];
    num1 = 1;
    myList.append(num1)
    num2 = 1;
    myList.append(num2)
    total = 0;
    for x in xrange(2, param):
        total = num1 + num2
        num1 = num2
        num2 = total
        myList.append(total)
    return myList

def main():
    print fibonacci1(0)
    print fibonacci1(1)
    print fibonacci1(2)
    print fibonacci1(5)
    try:
        fibonacci1(-5)
    except ValueError:
        print "Oops! No negative numbers allowed. Please try again..."


=======
__author__ = 'Michael'


def fibonacci1(a):
    if a < 0:
        raise ValueError()
    if a == 0:
        return "Please enter a positive integer, n, to find the n-th fibonacci number"
    if a == 1 or a == 2:
        return 1
    num1 = 1;
    num2 = 1;
    total = 0;
    for x in xrange(2, a):
        total = num1 + num2
        num1 = num2
        num2 = total
    return total

def fibonacci2(param):
    myList = [];
    num1 = 1;
    myList.append(num1)
    num2 = 1;
    myList.append(num2)
    total = 0;
    for x in xrange(2, param):
        total = num1 + num2
        num1 = num2
        num2 = total
        myList.append(total)
    return myList

def main():
    print fibonacci1(0)
    print fibonacci1(1)
    print fibonacci1(2)
    print fibonacci1(5)
    try:
        fibonacci1(-5)
    except ValueError:
        print "Oops! No negative numbers allowed. Please try again..."


>>>>>>> origin/master
main()