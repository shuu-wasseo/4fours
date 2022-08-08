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
                    yield x + y, f'({sx} + {sy})'
                    yield x - y, f'({sx} - {sy})'
                    if sx != sy:
                        yield y - x, f'({sy} - {sx})'
                    yield x * y, f'({sx} * {sy})'
                    if y != 0:
                        try:
                            yield x / y, f'({sx} / {sy})'
                        except:
                            pass
                    if x != 0 and sx != sy:
                        try:
                            yield y / x, f'({sy} / {sx})'
                        except:
                            pass
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
        #if n.denominator == z+1 and n % 1 != 0:
            #print(s + " = " + str(n))
        toteqns += 1
        if toteqns % 100000 == 0:
            print("eqns analysed: " + str(toteqns) + " for " + str(lis))
        if isinstance(n, complex) == False:
            try:
                float(n)
            except:
                pass
            else:
                if float(n) % (1/(z+1)) == 0 and n >= 0:
                    results.append(n.numerator)
                    #print(n.numerator)
                #elif n.denominator == z+1:
                    #print(str(float(n)) + " % " + str(1/(z+1)) + " != 0")
    results = list(dict.fromkeys(results))
    results.sort()
    print(results)
    liscount = 0
    for num in range(len(results)):
        if num == results[num]:
            liscount += 1
            print("found " + str(num/z+1))
        else:
            break
    data.append(liscount-1)
    return liscount-1

numer = int(input("enter your numerator: "))
denom = int(input("enter your denominator: "))
numberofnumbers = int(input("enter your number y, which is the number of instances of x you would like to include: "))
header = ["number of instances"]
results = []

final = """"""
non = numberofnumbers

if non > 0:
    for z in range(denom):
        for y in range(non):
            data = [non]
            for x in range(numer):
                if x+1 > 0 and y+1 > 1 and z+1 >= 2:
                    print("finding "+str(y+1)+" instances of "+str((x+1))+"/" + str(z+1) + "...")
                    works((x+1)/(z+1), y+1, data)
            data = data[2:]
            results.append(data)
            for x in results:
                print(str(x)[1:-1])
