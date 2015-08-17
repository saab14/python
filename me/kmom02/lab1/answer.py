#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
019e4480e710afec43844d2854db458d generated for saab14 at 2015-02-27 21:19:53 
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 1 - python 
 
If you need to peek at examples or just want to know more, take a look at
the page: https://docs.python.org/3/library/index.html. Here you will find
everything this lab will go through and much more. 
"""

"""
--------------------------------------------------------------------------
Section 1. Integers, strings, floats and basic arithmetics 
 
The foundation of numbers and basic arithmetic. 
"""

"""
Exercise 1.1 
 
Create a variable called 'numOne' and give it the value 23. Create another
variable called 'numTwo' and give it the value 15. Create a third variable
called 'result' and assign to it the sum of the first two variables. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
numOne = 23
numTwo = 15
result = 23 + 15


ANSWER = 38

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Create a variable called 'numThree' and give it the value 40. Create
another variable called 'numFour' and give it the value 98. Subtract
'numThree' from 'numFour' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
numThree = 40
numFour = 98
res1 = numThree - numFour


ANSWER = 58

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Find out the product of 'numOne' and 'numThree' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
res2 = numOne * numThree


ANSWER = 920

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Divide 30 with 5 and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
result = 30 / 5

ANSWER = 6

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Create a variable called 'floatOne' and give it the value 93.86. Create
another variable called 'floatTwo' and give it the value 65.63. Sum the two
values and answer with the result, rounded to 2 decimals. 

Write your code below and put the answer into the variable ANSWER.
"""

floatOne = 93.86
floatTwo = 65.63
res3 = floatOne + floatTwo

ANSWER = 159.49

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Subtract 'floatTwo' from 'floatOne' and answer with the result. Round to 2
decimals. 

Write your code below and put the answer into the variable ANSWER.
"""

res4 = floatTwo - floatOne

ANSWER = 28.23

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Answer with the product of 'floatOne' and 'floatTwo', rounded to 4
decimals. 

Write your code below and put the answer into the variable ANSWER.
"""

res5 = floatOne * floatTwo


ANSWER = 6160.0318

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create three variables: 'n1' = 492, 'n2' = 370 and 'n3' = 74. Sum up 'n1'
and 'n2'. Subtract 'n3' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
n1 = 492
n2 = 370
n3 = 74

res6 = n1 + n2 - n3

ANSWER = 788

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Answer with the result of 645 modulo (%) 38. 

Write your code below and put the answer into the variable ANSWER.
"""

res7 = 645 % 38

ANSWER = 37

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Add the word: 'screen' to the word: 'water' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
str1 = "screen"
str2 = "water"
res8 = str1 + str2

ANSWER = "waterscreen"

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Conditions, exceptions, booleans, if, else and elif 
 
 
"""

"""
Exercise 2.1 
 
Answer with the boolean value of: 333 is less than 98. 

Write your code below and put the answer into the variable ANSWER.
"""

res9 = 333 < 98

ANSWER = False

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Answer with the boolean value of: 126 is larger than 74. 

Write your code below and put the answer into the variable ANSWER.
"""

res10 = 126 > 74

ANSWER = True

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Answer with the boolean value of: 333 == 126. 

Write your code below and put the answer into the variable ANSWER.
"""
res11 = 333 == 126

ANSWER = False

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Create three variables representing dice values: 'd1' = 4, 'd2' = 6 and
'd3' = 1. Sum them up and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

d1 = 4
d2 = 6
d3 = 1
res12 = d1 + d2 + d3

ANSWER = 11

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Create an if statement to see if the total value of your dices is 11 or
higher. If that is the case, answer with the string: 'big', else answer
with the string: 'nothing'.  

Write your code below and put the answer into the variable ANSWER.
"""
if result == 11 or result > 11:
    print("big") 
else:
    print("nothing")

ANSWER = "big"

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Create an elif statement that checks your total dice value. The checks and
results should be: three of the same value = 'triple', total of 11 or
higher = 'big', total of 10 or lower = 'small'. If you get a triple you
should not make more checks. 

Write your code below and put the answer into the variable ANSWER.
"""
res20 = 11
if res20 == "triple":
    print("nth")
elif res20 == 3 and res20 == 3 and res20 == 3:
    print("triple")
elif res20 == 11 or res20 > 11:
    print("big")
elif res20 == 10 or res20 < 10:
    print("small")
else:
    print("good bye")
    
ANSWER = "big"

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, True))

"""
--------------------------------------------------------------------------
Section 3. Built-in functions 
 
Some useful built-in functions 
"""

"""
Exercise 3.1 
 
Use max() to find the largest number in the serie:
6, 8, 95, 2, 12, 152, 4, 78, 621, 45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""

max(6, 8, 95, 2, 12, 152, 4, 78, 621, 45)

ANSWER = 621

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2 
 
Use min() to find the smallest number in the serie:
6, 8, 95, 2, 12, 152, 4, 78, 621, 45. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
min(6, 8, 95, 2, 12, 152, 4, 78, 621, 45)

ANSWER = 2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))

"""
Exercise 3.3 
 
Use len() to find the number of letters in the word: memory. Answer with
the result. 

Write your code below and put the answer into the variable ANSWER.
"""

len("memory")

ANSWER = 6

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.3", ANSWER, False))

"""
Exercise 3.4 
 
Convert the number 524 to a string and add it to the word 'memory'. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word1 = "memory"
res13 = word1 + str(524)

ANSWER = "memory524"

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.4", ANSWER, False))

"""
Exercise 3.5 
 
Convert the number 647.1 to an integer and then to a string. Add it to the
beginning of the word: 'memory'. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
word = "memory"
int(647.1)
str(647)

res14 = str(647) + word


ANSWER = "647memory"

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.5", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 4. Functions 
 
Basic functions 
"""

"""
Exercise 4.1 
 
Create a function called 'prodNr' that takes two arguments, 7 and 76. The
function should return the product of the numbers. Answer with a call to
the function.  

Write your code below and put the answer into the variable ANSWER.
"""
def prodNr(arg1=7, arg2=76):
    """
    A function that return a product of numbers
    """
    res15 = arg1 * arg2
    print(res15)
    return


ANSWER = 532

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.1", ANSWER, False))

"""
Exercise 4.2 
 
Create a function called 'funnyWord' that takes one argument and adds it to
the string ' is a funny word'. If the argument is 'water', the function
should return: 'water is a funny word'. Use the argument 'restaurant' and
answer with a call to the function. 

Write your code below and put the answer into the variable ANSWER.
"""
def funnyWord(word3):
    """
    A function that return diffrenet strings of words
    """
    word3 = "is a funny word"
    if word3 == "water":
        funnyWord("water is a funny word")
        funnyWord("restaurant")

ANSWER = "restaurant is a funny word"

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.2", ANSWER, False))

"""
Exercise 4.3 
 
Create a function called 'inRange' that takes one argument. The function
should return 'true' if the argument is higher than 50 and lower than 100.
If the number is out of range, the function should return 'false'. The
return type should be boolean. Use the argument 47 and answer with a call
to the function. 

Write your code below and put the answer into the variable ANSWER.
"""
def inRange(arg1):
    """
    Checking an argument value
    """
    if arg1 > 50 and arg1 < 100:
        return True
    else:
        return False
    inRange(47)

ANSWER = False

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.3", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 5. Iteration and loops 
 
For-loops and while-loops.  
"""

"""
Exercise 5.1 
 
Create a while-loop that adds 5 to the number 85, 21 times. Answer with the
result.  

Write your code below and put the answer into the variable ANSWER.
"""
count = 85
while count == 85:
    count = count + (5 * 21)

ANSWER = 190

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.1", ANSWER, True))

"""
Exercise 5.2 
 
Create a while-loop that subtracts 7 from 37, 29 times. Answer with the
result.  

Write your code below and put the answer into the variable ANSWER.
"""
count = 0
while count == 7 - 37:
    count = count * 29

ANSWER = -166

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.2", ANSWER, False))

"""
Exercise 5.3 
 
Create a for-loop that counts the number of elements in the serie:
6, 8, 95, 2, 12, 152, 4, 78, 621, 45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
num = 0
serie = ("6, 8, 95, 2, 12, 152, 4, 78, 621, 45")
for num in serie:
    len(serie)

ANSWER = 10

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.3", ANSWER, True))

"""
Exercise 5.4 
 
Create a for-loop that sums up the numbers in the serie:
67, 2, 12, 28, 128, 15, 90, 4, 579, 450. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
num = 0
serie = (67, 2, 12, 28, 128, 15, 90, 4, 579, 450)
for num in serie:
    sum(serie)

ANSWER = 1375

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.4", ANSWER, False))

"""
Exercise 5.5 
 
Create a for-loop that finds the largest number in the serie:
6, 8, 95, 2, 12, 152, 4, 78, 621, 45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
num = 0
serie = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)
for num in serie:
    max(serie)

ANSWER = 621

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.5", ANSWER, False))

"""
Exercise 5.6 
 
Create a for-loop that goes through the numbers:
67, 2, 12, 28, 128, 15, 90, 4, 579, 450. If the current number is even, you should
add it to a variable and if the current number is odd, you should subtract
it from the variable. Answer with the final result.  

Write your code below and put the answer into the variable ANSWER.
"""
num = 0
var = 0
numbers = (67, 2, 12, 28, 128, 15, 90, 4, 579, 450)
for num in numbers:
    if num % 2 == 0:
        res30 = var + num
    else:
        res30 = var - num

ANSWER = 53

# Is the answer as expected? No
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.6", ANSWER, True))


dbwebb.exitWithSummary()
