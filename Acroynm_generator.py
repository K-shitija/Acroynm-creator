# -*- coding: utf-8 -*-
"""
Spyder Editor
Author :Kshitija ghode
This is a temporary script file.
"""

#Take input from user
user_input = input("Enter the phrase: ")

#Replace "of"word using Replace() method and Spilliting the user input into individual words using split() method
phrase = (user_input.replace('of','')).split()

#Initializing the empty string to append the acroynm
a =""

#for loop to append acroynm
for word in phrase :
    a= a + word[0].upper()

print(f'Acronym of {user_input} is {a}')    