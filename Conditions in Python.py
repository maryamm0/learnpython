#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:25:20 2022

@author: maryammanjoo
"""
##CONDITIONS

#Condition statements
#equaL:=
#not equal: !=
#greater thab: >
#less than: <


#Condition equal
a=5
a==6 #checking if a is equal to 6

i=5
i<6 #checking if i is less than 6
i>5 #checking if i is greater than 5

i2 = 2
i2 != 6 #checking if i2 is not equal to 6


"Hello World" == "Hello Earth" #use equality to check for strings

"Hello World" != "Hello Earth"

'B' > 'A'

#Branching
#Use the if statement

age=19 #set age to 19

if age>18: #set condition
 print("You can enter") #Result if condition is true
 print("You can move on") #Result regardless if condition is True or False
 
 #Else statement
age2= 18 #set age2 to 18

if age2>18: #set condition
 print("You can enter") #Result if condition is True
 
else:
    print("Go see One Direction") #Result if condition is false

print("You can move on") #Result irrelevant of Condition

#Elif statement (Else if statement)
#Check for additional conditions before else stament or result irrelevant to condition 

age3=18

if age3>18:
    print("You can enter")  
elif age3==18: #Additional condition if age3<=18
    print("Go see Zayn Malik")
else:
    print("Go see One Direction")
print("You can move on")


age4=17

if age4>18:
    print("You can enter")  
elif age4==18:
    print("Go see Zayn Malik")
else:
    print("Go see One Direction")
print("You can move on")


album_year=1970

if album_year>1980:
    print("Album year is greater than 1980")
    
print("Do something")
    
 
album_year2=1980

if album_year2>1980:
    print("Album year is greater than 1980")
else:
    print("Album year is less than 1980") #Result if statenent above if False
print("Do something")

#Logical Operators
#And, Or, not

album_year3 = 1990

if(album_year3 < 1980) or (album_year3 > 1989): #if album_year3 meets either one of the 2 conditions
    print ("Album was not made in the 1980's") #Result if ine condition is met
else:
    print("The Album was made in the 1980's ") #Result if both conditions are False



album_year4 = 1983

if not (album_year4 == 1984):
    print ("Album year is not 1984")
    
    
album_rating=8.5

if album_rating>8:
    print("This album is Amazing!")
 
album_rating2=7
if album_rating2>8:
    print("This album is Amazing!")
else:
    print("This album is ok")
    

#method 1:
album_year5=1993

if (album_year5<1980):
    print("The album came out in 1980")
elif(album_year5==1991):
    print("The album came out in 1991")
elif(album_year5==1993):
    print("The album came out in 1993")
    
#Method 2 

album_year6=1993

if album_year6 < 1980 or album_year6 == 1991 or album_year6 == 1993:
    print("This album came out in year", album_year6)
    

  

 