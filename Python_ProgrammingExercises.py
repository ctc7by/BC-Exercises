# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:19:54 2020

@author: Christina
"""

# Exercise 1: Print the Time
import datetime
print(datetime.datetime.now())

# Exercise 2: Make a Simple Stopwatch
starttime = datetime.datetime.now()

greeting = "hello world"
print(greeting)

endtime = datetime.datetime.now()
print(endtime - starttime)

# Exercise 3: Print a Word Provided by the User
# prompt user for a word
userword = input("Please enter a word: ")
print(userword)

# Exericse 4: Validate User Input
userword=str(input("Please enter a word: "))
if not userword.isalpha():
    print("Your word must consist of letters only")
    userword=str(input("Please enter a word: "))
    print("Your word is " + userword)
else:
    print("Your word is " + userword)


# Exercise: Record and Print a List
input_string = input("Enter a list numbers or elements separated by space: ")
userList = input_string.split()
for int in userList:
    print(int)

    

