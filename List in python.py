#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 10:18:39 2022

@author: maryammanjoo
"""
#Create a list
L=["Michael Jackson",10.1,1982]

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )


L=["Michael Jackson",10.1,1982,"MJ",1]
print(L[3:5]) #slicing the list

L=L.append(["pop",10])
print(L)

#List are mutable, hence can be changed
A=["disco",10,1.2]
print("Before changes: ",A)
A[0]="Hard Rock" #changing first index to Hard Rock
print("After changes: ",A)

print("Before changes: ",A)
del(A[0]) #deletee first index in list
print("After changes: ",A)

#Split string

print('hard rock'.split()) #convert a string into list using split
print("A,B,C,D".split(',')) #convert string ABCD into list using comma as separator

#Copy and Clone
A=["hard Rock",10,10.1]
B=A
print("A:",A)
print("B:",B)

print("B[0]: ",B[0])
A[0]="Jazz"
print("B[0]: ",B[0])

#Clone by value
Original=["Original Value",1,1.1]
Clone = Original[:]
print(Clone)

#TASK

a_list=[1,"hello",[1,2,3],True]
print(a_list)

print(a_list[1]) #returns the value of index 1 
print(a_list[1:4]) #returns index 1- 3 of list

#Concatenate list
concat1=[1, 'a']
concat2=[2, 1, 'd']

concatenate=concat1+concat2
print(concatenate)
