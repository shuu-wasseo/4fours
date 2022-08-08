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
        yield x, pcomp(x)
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
                    try:
                        y.denominator
                    except:
                        pass
                    else:
                        if abs(y) < 100 and y.denominator == 1 and (x != 0 or y > 0):
                            yield x ** y, f'({sx} ^ {sy})'
                    try:
                        x.denominator
                    except:
                        pass
                    else:
                        if sx != sy and abs(x) < 100 and x.denominator == 1 and (y != 0 or x > 0):
                            yield y ** x, f'({sy} ^ {sx})'


def works(num, numofnums, data):
    count = 0
    lis = []
    results = []
    toteqns = 0
    for x in range(numofnums):
        lis.append(num)
        #print(lis)
    for n, s in generate(lis):
        toteqns += 1
        if toteqns % 100000 == 0:
            print("eqns analysed: " + str(toteqns) + " for " + str(lis))
        if n.imag % 1 == 0 and n.imag >= 0 and n.real == 0:
            results.append(n.imag)
            #print(s + "=" + str(n.imag))
            #print(n)
    results = list(dict.fromkeys(results))
    results.sort()
    print(results)
    liscount = -1
    for x in range(len(results)):
        if x == results[x]:
            print(str(x) + "found")
            liscount += 1
        else:
            break
    data.append(liscount)
    return liscount-1

def pcomp(comp):
    if comp.real == 0 and comp.imag == 0:
        return str(0)
    elif comp.real == 0 and comp.imag != 0:
        return str(comp.imag) + "i"
    elif comp.real != 0 and comp.imag == 0:
        return str(comp.real)
    else:
        return str(comp.real) + " + " + str(comp.imag) + "i"

number = int(input("enter number x in xi: "))
numberofnumbers = int(input("enter your number y, which is the number of instances of x you would like to include: "))
header = ["number of instances"]
results = []

final = """"""
non = numberofnumbers

if non > 0:
    for y in range(non):
        data = [non]
        for x in range(number):
            if x+1 > 0 and y > 0:
                print("finding "+str(y)+" instances of "+str(x+1)+"i...")
                works(complex(0, x+1), y, data)
        data = data[2:]
        results.append(data)
        for x in results:
            print(str(x)[1:-1])
