#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:23:14 2022

@author: maryammanjoo
"""
##SETS

set1={"pop","rock","soul","jazz","rock","R&B","disco","rock"}
print(set1)

#Convert list to set
album_list=["Michael Jackson","Thriller",1982,"00:42:19",\
            "Pop,Rock,R&B",46.0,65,"30-Nov-82",None,10.0
            ]
album_set=set(album_list)
print(album_set)

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"]) #convert list to set
print(music_genres)

sample1 = set(["Thriller", "Back in Black", "AC/DC"])
print(sample1)

sample1.add("NSYNC") #add element to set
print(sample1)

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

print(album_set1)
print(album_set2)

intersection= album_set1 & album_set2 #to find the intersection of albumset1 and 2
print(intersection)

print(album_set1.difference(album_set2)) #elements only in album_set1
print(album_set2.difference(album_set1)) #elements only in album_set2

print(album_set1.intersection(album_set2)) #find the intersection of two albums

album_set1.union(album_set2) #union of two sets

set(album_set1).issuperset(album_set2)  #check if album_set1 is superset of album_set2

set(album_set2).issubset(album_set1) #check if album_set2 is subset of album_set1

list1=['rap','house','electronic music', 'rap']
set2=set(list1) #convert list1 into set
print(list1)

album_1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_3=album_1.union(album_2)
print(album_3)

album_1.issubset(album_3) #check if album1 is a subset of album2




