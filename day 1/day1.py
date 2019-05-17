# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:02:46 2019

@author: SOURABH
"""
#day 1
#challenge 1
travel = int(input("enter the km"))
fuel = int(input("enter the fuel"))
avg = travel/fuel
print (avg)

#challenge 2
travel_in_day = int(input("enter the km"))
cost_per_liter = 80
fuel_average = 18
average_cost = cost_per_liter/fuel_average
cost_per_day = travel_in_day/average_cost
print(cost_per_day)

#challenge 3
a1 = int(input("enter the marks"))
a2 = int(input("enter the marks"))
a3 = int(input("enter the marks"))
e1 = int(input("enter the marks"))
e2 = int(input("enter the marks"))
weighted_score = (( a1+a2+a3 ) * 0.1) + ((e1+e2 ) * 0.35)
print(weighted_score)

#challenge 4
print("* "*8)
print(" *"*8)
print("* "*8)
print(" *"*8)
print("* "*8)
print(" *"*8)
print("* "*8)

#challenge 5
import math
value = int(input("enter the number"))
print(math.factorial(value))

