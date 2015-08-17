#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
random
"""
import random

"""
Zryzar with a simple menu to start up with.
Zryzar doesnt do anything, just presents a menu with some choices.
You should add functinoality to Zryzar.

"""
def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
      _       _
     (_\     /_)
       ))   ((
     .-.......-.
 /^\/  _.   _.  \/^\
 \(   /__\ /__\   )/
  \,  \o_/_\o_/  ,/
    \    (_)    /
     `-.'==='.-'
      __) - (__
     /  `~~~`  \
    /  /     \  \
    \ :       ; /
     \|==(*)==|/
      :       :
       \  |  /
     ___)=|=(___
    {____/ \____}

    """
def menu():
    """
    Display the menu with the options that Zryzar can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage())
    print("Hi, I'm Zryzar. I know everything. What can I do you for?")
    print("1) Present yourself to Zryzar.")
    print("2) Write your age to Zryzar.")
    print("3) Write your weight to Zryzar.")
    print("4) Ask Zryzar how many hour in the minute/minutes you typed.")
    print("5) Let Zryzar convert a temperature from Celsius to Fahrenheit.")
    print("6) Words multiplying.")
    print("7) Random number.")
    print("8) Ask Zryzar for mean value.")
    print("9) Let Zryzar help you check your grades.")
    print("q) Quit.")


def myNameIs():
    """
    Read the users name and say hello to Zryzar.
    """
    name = input("What is your name? ")
    print("\nZryzar says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def myAge():
    """
    Read the users age and count how many seconds they lived.
    """
    age = int(input("How old are you? "))
    userAge = age * 60 * 60 * 24
    print("\nZryzar says:\n")
    print("You have lived at least: " + str(userAge))
    print("What can I do you for?!")

def myWeight():
    """
    Read the users weight and count their weight on moon.
    """
    weight = int(input("Waht's your weight? "))
    userWeight = weight * 1.6
    print("\nZryzar says:\n")
    print("Your weight on moon is: " + str(userWeight) + " N")
    print("What can I do you for?!")

def minuteToHour():
    """
    Read the input minutes and count the hour in it.
    """
    minute = int(input("How many minutes? "))
    minuteInHour = minute/60
    print("\nZryzar says:\n")
    print("Its " + str(minuteInHour) + " hour in " + str(minute))
    print("What can I do you for?!")

def temperature():
    """
    Convert the tempreature from Celsius to Fahrenheit.
    """
    temperatureC = int(input("What is the temperature in Celsius? "))
    temp = (temperatureC * 9 / 5) + 32
    print("\nZryzar says:\n")
    print("Its " + str(temp) + " fahrenheit")
    print("What can I do you for?!")

def wordsMultiplying():
    """
    Read the input word then multiplicate it with an input number.
    """
    word = input("Write a word ")
    number = int(input("Write a number "))
    wordsMulti = word * int(number)
    print("\nZryzar says:\n")
    print(str(wordsMulti) + "\n")
    print("What can I do you for?!")

def randomNumber():
    """
    Read the input min and max number then get th random numbers in between.
    """
    minNum = input("Type a min number ")
    maxNum = input("Type a max number ")
    numList = [minNum, maxNum]
    minOut = min(numList)
    maxOut = max(numList)
    print("\nZryzar says:\n")
    for minOut in range(10):
        print(random.randint(int(minOut), int(maxOut)), end=" ")
        print("What can I do you for?!")
    
def meanAndSum():
    """
    Count the mean value.
    """
    total = 0
    while True:
        number = input("Type some numbers then type 00 when you are done ")
        wt = "00"
        total += int(number)
        if number != wt:
            continue
        elif number == wt:
            print("The mean value is " + total/len(number))
            break

def grades():
    """
    Read the input max points and users points then let them know their grade.
    """
    while True:
        maxPoints = float(input("Type the max points of a course "))
        grade = float(input("Type your grade: "))
        a = float(maxPoints) * 0.9
        b = float(maxPoints) * 0.8
        c = float(maxPoints) * 0.7
        d = float(maxPoints) * 0.6
        f = float(maxPoints) * 0.6
        if grade >= a:
            print("A")
        elif grade >= b:
            print("B")
        elif grade >= c:
            print("C")
        elif grade >= d:
            print("D")
        elif grade <= f:
            print("F")



def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return

        elif choice == "1":
            myNameIs()
            
        elif choice == "2":
            myAge()
            
        elif choice == "3":
            myWeight()
            
        elif choice == "4":
            minuteToHour()
            
        elif choice == "5":
            temperature()
            
        elif choice == "6":
            wordsMultiplying()
            
        elif choice == "7":
            randomNumber()
            
        elif choice == "8":
            meanAndSum()
            
        elif choice == "9":
            grades()
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")



if __name__ == "__main__":
    main()

