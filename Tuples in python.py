#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:57:34 2022

@author: maryammanjoo
"""
##TUPLES
#Tuples are enclosed with ()

tuple1=("disco",10,1.2)
print(tuple1)

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

#Concatenate
#use +

tuple2=tuple1 + ("hard rock", 10)
print(tuple2)

print(tuple2[3:5]) #returns index 3 to 4
print(tuple2[0:4]) #slice index 0 to 3

rating=(0, 9, 6, 5, 10, 8, 9, 6, 2)
rating_sorted=sorted(rating) #sort tuple rating
print(rating_sorted)

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2))) #Nested tuple
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

##Tuple quiz

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
print(genres_tuple)
print(len(genres_tuple)) #returns the length of the tuple
print(genres_tuple[3]) #returns index 3 of tuple
print(genres_tuple[3:6]) #returns index 3 to 5
print(genres_tuple[0:2]) #returns first two elements of the tuple
print(genres_tuple[7][1])
genres_tuple.index("disco")

C_tuple=(-5, 1, -3)

C_sorted=sorted(C_tuple) #sort C_tuple
print(C_sorted)
