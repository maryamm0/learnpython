#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:17:22 2022

@author: maryammanjoo
"""
##DICTIONARIES
#Dictionaries consist of keys and values

#Create a dictionary
Dictionary_1 = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dictionary_1)

Dictionary_1["key1"] #Access key1 #keys can be a string
Dictionary_1[(0,1)] #Access key (0,1) #keys can be tuples

release_year_dictionary = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
    
print(release_year_dictionary)

#A dictionary hold a set of sequence enclosed with curly brackets
#Keys can only be strings, numbers, or tuples
#Values represented by the keys can be any data type

release_year_dictionary["Thriller"] #returns the value held by key "Thriller"
release_year_dictionary["Their Greatest Hits (1971-1975)"] #returns year 1976

release_year_dictionary.keys() #retrieves all keys in dictionary

release_year_dictionary["Graduation"]='2007' #append key and value to dictionary
print(release_year_dictionary)

del(release_year_dictionary["Graduation"]) #delete key Graduation and its value 
print(release_year_dictionary)

##Quiz on dictionaries 

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(soundtrack_dic)

soundtrack_dic.keys() #returns all the keys in dict
soundtrack_dic.values() #returns the values for keys in dict

album_sales_dict={"Back in Black":50, "The Bodyguard":50,"Thriller":65}
print(album_sales_dict)

album_sales_dict["Thriller"] #returns sales for album Thrillers
album_sales_dict.keys() #returns all the albums
album_sales_dict.values() #returns all sales made by the albums 