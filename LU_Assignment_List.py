# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:47:33 2021

@author: RASHMI
"""

x=int(input('enter val_1: '))
y=int(input('enter val_2: '))
print(x+y)

x=input('out any numbers: ').split()
x
vals=[]
for i in x:
    vals.append(int(i))
    print(vals)
    
vals=[int(i) for i in  input('out any numbers: ').split()]
vals
    
#List
li = []
li = list()

li = [1, 2, 3, 4, 5, 25, 45, 65, 85]
li
type(li)
li[-1]
li[2:5]  #[start : end]
li[3:]
li[:6]
li[:]

li[::1] #[start : end : step]
li[::2]
li[::3]
li[::-1]  #print list in reverse order

#List Methods
li = [1, 2, 3, 4, 5, 25, 45, 65, 85]
li.insert(0, 15)
li
li.insert(12, 15)
li
li.insert(-40, 15)
li
li.pop()  # delete last value
li.pop(0)
li
li = [1, 2, 3, 4, 5, 25, 45, 65, 85, 'hello']
li.remove('hello')
li
