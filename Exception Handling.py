#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:52:11 2022

@author: maryammanjoo
"""
#Exception Handling

#Exception: Error that occurs during the execution of a code

#error examples:

1/0 #ZeroDivisionErrorwhen dividing by zero

y = a + 5 #a is not defined causing undefined name error

#exception handling is how to handle the errors
#How to make program perform another task instead of halting the execution
#Use try except 

#Use try to execute code
#use except to catch exception/error caused by try code

"""
try:
    # code to try to execute
except:
    # code to execute if exception/error occurs
    
# code that will execute regardless of exception/error
"""


x = 1

try:
    y = 0
    x = x/y #division by zero is not permissible
    print("Success x=",x)
except:
    print("There is an error")  #code excuted due to error
    
#Except, Else 
#Else checkcs if there is no exception
#code after else will run if no exception available


#Finally
#Finally code executed if there are exceptions or not
x1 = 1

try:
    y1 = 0
    x1 = x1/y1
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0") #code executed due to try code error
except ValueError:
    print("You did not provide a number") #code executed due to try code error
except:
    print("Something went wrong")
else:
    print("success x1=",x1) #code execute if no error/exception
finally:
    print("Processing Complete") #Code executed at end
    
    
    
