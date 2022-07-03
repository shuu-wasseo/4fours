# this script comes from Radcliffe on github. 

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
          yield head+left, right
          yield left, head+right

def generate(lst):
    if len(lst) <= 1:
        x = lst[0]
        yield Fraction(x), str(x)
        yield math.ceil(x), f'⌈{x}⌉'
        yield math.floor(x), f'⌊{x}⌋'
        if x >= 0:
            yield math.factorial(int(x)), f'{x}!)'
            yield math.sqrt(x), f'√{x}'
    else:
        for A, B in partition(lst):
            for x, sx in generate(A):
                for y, sy in generate(B):
                    try:
                        yield x+y, f'({sx}+{sy})'
                        yield x-y, f'({sx}-{sy})'
                        if sx != sy:
                            yield y-x, f'({sy}-{sx})'
                        yield x*y, f'({sx}*{sy})'
                        if y != 0:
                            yield x/y, f'({sx}/{sy})'
                        if x != 0 and sx != sy:
                            yield y/x, f'({sy}/{sx})'
                        if abs(y) < 100:
                            yield x**y, f'({sx} ^ {sy})'  
                        if sx != sy and abs(x) < 100 and (y != 0 or x > 0):
                           yield y**x, f'({sy} ^ {sx})'
                        if y != 0 and abs(y) < 100:
                            yield x**(1/y), f'{sy}√{sx}'
                        if x != 0 and sx != sy and abs(x) < 100:
                            yield y**(1/x), f'{sx}√{sy}'  
                    except:
                        pass
def works(num, numofnums, total):
    count = 0
    lis = []
    sols = []
    for x in range(numofnums):
        lis.append(num)
    for n, s in generate(lis):
        if n == total:
            count += 1
            sols.append(s)
            continue
    sols = list(dict.fromkeys(sols))
    return len(sols)

def findupperlimit (numb, numbofnumbs):
    start = 0
    while 1:
        if works(numb, numbofnumbs, start) != 0:
            start += 1
        else:
            break
    return start-1

number = int(input("enter your number x: "))
numberofnumbers = int(input("enter your number y, which is the number of instances of x you would like to include: "))
header = ["number of instances"]
results = []

for x in range(number):
    header.append(str(x+1))

non = numberofnumbers
if non > 0:
    for y in range(non+1):
        data = [non]
        for x in range(number+1):
            if x >= 1 and non >= 2:
                print("finding "+str(non)+" instances of "+str(x)+"...")
                data.append(works(x, non))
        results.append(data)
results = results[2:]
final = """"""
for x in results:
    string = str(x)[1:-1]
    final = final+string+"\n"
print(final)
