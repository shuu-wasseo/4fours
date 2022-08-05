# this script comes from Radcliffe on github. for original code, please visit https://gist.github.com/Radcliffe/fab1cefe6e2a3a23466539a7ecbc6edb/.

# This Python 3 script solves the "Four Fours" problem and similar problems.

# The example at the end of the script generates all combinations of [2,3,5,7]
# that equal 10, using the operations of addition, subtraction, multiplication,
# and division.

# Exact arithmetic is used. Only integer exponents between -99 and 99 are allowed.

from fractions import Fraction
import math
import csv

def partition(lst):
    """Recursively partition a list into two nonempty sublists."""
    head, tail = lst[:1], lst[1:]
    yield head, tail
    if len(lst) > 2:
      for left, right in partition(tail):
          yield head + left, right
          yield left, head + right


def generate(lst):
    if len(lst) == 1:
        x = lst[0]
        yield Fraction(x), str(x)
    else:
        for A, B in partition(lst):
            for x, sx in generate(A):
                for y, sy in generate(B):
                    if "1" in op:
                        yield x + y, f'({sx} + {sy})'
                    if "2" in op:
                        yield x - y, f'({sx} - {sy})'
                        if sx != sy:
                            yield y - x, f'({sy} - {sx})'
                    if "3" in op:
                        yield x * y, f'({sx} * {sy})'
                    if "4" in op:
                        if y != 0:
                            yield x / y, f'({sx} / {sy})'
                        if x != 0 and sx != sy:
                            yield y / x, f'({sy} / {sx})'
                    if "5" in op:
                        if abs(y) < 100 and y.denominator == 1 and (x != 0 or y > 0):
                            yield x ** y, f'({sx} ^ {sy})'
                        if sx != sy and abs(x) < 100 and x.denominator == 1 and (y != 0 or x > 0):
                            yield y ** x, f'({sy} ^ {sx})'


def works(num, numofnums, data):
    count = 0
    lis = []
    results = []
    toteqns = 0
    for x in range(numofnums):
        lis.append(num)
    for n, s in generate(lis):
        toteqns += 1
        if toteqns % 1000000 == 0:
            print("eqns analysed: " + str(toteqns) + " for " + str(lis))
        if isinstance(n, complex) == False:
            if n % 1 == 0 and n >= 0:
                results.append(n)
                #print(n)
    results = list(dict.fromkeys(results))
    results.sort()
    #print(results)
    liscount = 0
    for x in range(len(results)):
        if x == results[x]:
            liscount += 1
        else:
            break
    data.append(liscount-1)
    return liscount-1

opl35 = ["123", "124", "125", "134", "135", "145", "234", "235", "245", "345"]

for x in opl35:
    number = int(input("enter your number x: "))
    numberofnumbers = int(input("enter your number y, which is the number of instances of x you would like to include: "))
    header = ["number of instances"]
    op = x
    results = []
    
    for x in range(number):
        header.append(str(x+1))
    
    final = """"""
    non = numberofnumbers
    
    if non > 0:
        y = non
        #for y in range(non-1):
        data = [non]
        for x in range(number+1):
            if x >= 1 and non >= 2:
                print("finding "+str(y)+" instances of "+str(x)+"...")
                works(x, y, data)
        data = data[2:]
        results.append(data)
        print(results)