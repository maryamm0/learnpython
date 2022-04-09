#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 19:50:32 2022

@author: maryammanjoo
"""
##FUNCTIONS
#Begins with def and function name followed by ():

#Creating addition function
def add1(a):
    """
    add 1 to a
    """
    b=a+1
    print(a,"plus one is",b) 
    return b
    
for a in range(0,5):
    print(add1(a)) #add1(a) calls the function
    
#Creating multiplication function
def multi(c,d):
    """
    Parameters
    ----------
    c : integer or float
    d : integer, string or float

    Multiplies c by d
    -------
    """
    m=c*d
    return(m)

c=2 #assign value to c
d="Hello" #assign value to c #strings can also be assigned, the reuslt will be hello twice in one stringss
multi(c,d) #call multi function
    

##Variable in function
#Local variable: Variable inside function
#Global variable: Variable outside a function


def squr(s):
    v = 1 #local variabe is b
    n = (s*s)+v
    print(s, "squared+1", n) 
    return(v)

n2=4 #n2 is the global variable
x=squr(n2)


def MJ():
    print('Michael Jackson')
    
MJ()
print(MJ()) #result for MJ and MJ1 are the same
    
def MJ1():
    print('Michael Jackson')
    return(None)
MJ1()
print(MJ1())


#Use if condition inside a function

def type_of_album(singer, album, album_year):
    
    print(singer, album, album_year)
    if album_year > 1980:
        return "New"
    else:
        return "Old"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)



artist = "Zayn Malik"
def printer1(singer):
    local_var1 = singer
    print(singer, "is an artist")
    
printer1(singer)
printer1(local_var1) #Because local_var1 is a local variable, it is not recognised outside the function



#Create a global variable inside a function

singer1="Shawn Mendes" #Define variable singer1

def Sing(singer1):
    global non_local_var 
    non_local_var="Harry Styles"
    print(singer1,"is an artist")

Sing(singer1) 
Sing(non_local_var)

#Function that divides the first input by the second input:
    
def div(m,i):
    j=m/i
    return(j)





