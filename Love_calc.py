# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:25:45 2023

@author: 16198
"""

print("The Love Calculator is calculating your score...")
name1 = "David Beckham" # What is your name?
name2 = "Victoria Beckham" # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# Assign the words "TRUE" and "LOVE" to variables so that they can be iterated through and put into a list by individual letter.
word = "TRUE"
secword = "LOVE"
# Create a dictionary that can store the number of times a letter occurs with key : value pairs. 
ltrcnt = {}
ltrcnt2 = {}
ltrcnt3 = {}
ltrcnt4 = {}
final_sum = 0
final_sum2 = 0

#Create the lists where the word is broken down into individual letters.
frstltrlst = [letter for letter in word]
scndltrlst = [letter for letter in secword]

#Iterate through each letter in frstltrlst
for letter in frstltrlst:
    count = name1.lower().count(letter.lower())
    count2 = name2.lower().count(letter.lower())
    ltrcnt[letter] = count
    ltrcnt2[letter] = count2
    total_sum = sum(ltrcnt.values())
    total_sum2 = sum(ltrcnt2.values())
    final_sum = total_sum + total_sum2

for letter in scndltrlst:
    count = name1.lower().count(letter.lower())
    count2 = name2.lower().count(letter.lower())
    ltrcnt3[letter] = count
    ltrcnt4[letter] = count2
    total_sum = sum(ltrcnt3.values())
    total_sum2 = sum(ltrcnt4.values())
    final_sum2 = total_sum + total_sum2

finalnum = int(str(final_sum) + str(final_sum2))



if finalnum <10 or finalnum >90:
    print(f"Your score is {finalnum}, you go together like coke and mentos.")
elif 40<finalnum<50:
    print(f"Your score is {finalnum}, you are alright together.")
else: 
    print(f"Your score is {finalnum}.")