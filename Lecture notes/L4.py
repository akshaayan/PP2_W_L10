# from L3 import *
import L3
import math


import requests

print(dir(L3))
owed_class = L3.Human() 
print(L3.test)
x = 1000

def outer(): #к примеру, создает список
    
    x = 100
    
    def inner(): # сортирует тот же список что и ввреху в outer
        # nonlocal x
        # x = 10
        print("inner: ", x)
    inner()
    
    print("outer: ", x)
outer()    
print("global: ", x)

import datetime

x = datetime.datetime.now()

print(x.strftime("%d %B %y %H"))

test_str= '2018-10-14 14:55'
format='%Y-%m-%d'
res_time = datetime.datetime.strptime(test_str, format)
# datetime.date
print(res_time)
# print(type(x))