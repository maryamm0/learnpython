#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:25:56 2022

@author: maryammanjoo
"""
#LOOPS

#Range
# Use range to repeat operations

#For loops
#Executes a code multiple times over given range

dates = [1982,1980,1973]
N = len(dates) #result is length of dates string

for i in range(N): #For variable in range 0 to 2
    print(dates[i])  #print dates for assigned index
    
for i in range(0,8): #for variable 0 to 7
   print(i) #print the variable index
    
for year in dates:
    print(year)
    
squares = ['red', 'yellow', 'green', 'purple', 'blue']
s=len(squares)

for i in range(0,s):
    print("Before square", i, "is",squares[i])
    squares[i]="white" #replacing all elements in squares list to white
    print("After square",i,"is",squares[i])
    
squares = ['red', 'yellow', 'green', 'purple', 'blue'] #recreate original squares list
for i, square in enumerate(squares): #square will provide ordered enumerated list of squares
    print(i, square)

#While loops
#Executes a code until condition is False
dates1 = [1982, 1980, 1973, 2000]

i = 0 #set first value of index
year1 = dates1[0] #set first value of year1

while(year1 != 1973): #code will execute until year is 1973
    print(year1) 
    i = i + 1 #move to other index 
    year1 = dates1[i]  

print("It took ", i ,"repetitions to get out of loop.") #prints when result is false/code stops

range1=range(-5,5)
print(range1)

for i in range1:
    print("element in index",i,"is",i)
    
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

range2=range(0,len(Genres))

for i2 in range2:
    print("Element in index",i2,"is",Genres[i2])
    
#Other method
enres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)   

squares=['red', 'yellow', 'green', 'purple', 'blue']

for square in squares:
    print(square)
    
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []

i_s=0
while(squares[i_s]=="orange"):
    new_squares.append(squares[i_s])
    i_s=i_s+1
print(new_squares)
    

    
    
    
    