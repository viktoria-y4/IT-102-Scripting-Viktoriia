#!/usr/bin/env python3
# Sample script that writes to a file
# By Viktoriia Y
# Script 1 - Collect info and save to hackme.txt
...

...

#This variables are questions that need to be answered
name=input("What is your name? ")
color=input("What is your favorite color? ")
pet=input("What is your first pets name? ")
maiden=input("What is your mothers maiden name? ")
school=input("What elementary school did you intend? " )

with open("hackme.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Favorite Color: {color}\n")
    file.write(f"First Pet: {pet}\n")
    file.write(f"Mothers Maiden Name: {maiden}\n")
    file.write(f"Elementary Schol: {school}\n")

print ("Saved to hackme.txt Great work!")
