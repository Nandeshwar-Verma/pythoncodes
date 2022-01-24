""" generators and iterators homework"""


""" 1: Create a generator that generates the squares of numbers up to some number N."""

def sq_of_num(n):
        for i in range(n):
                yield i**2

x=sq_of_num(5)
i=0
try:
        while i < 7:
                print(next(x))
                i+=1

except StopIteration:
        print("ended")


"""2: Create a generator that yields "n" random numbers between a low and high number (that are inputs)."""


import random

def rand_num(low,high):
        for i in range(10):                                       
                yield random.randint(low,high)

x=rand_num(1,10)
print(next(x))
print(next(x))

print(next(x))

print(next(x))

