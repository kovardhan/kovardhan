# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:15:57 2021

@author: k
"""
from SIMPLY import *
p=[]
name=str(input("please enter your name: "))#my name is kovardhan.R.R
rollno=str(input("please enter the rollno: "))
name=list(name)
rollno=list(rollno)
print(name,rollno)
def huffmanoutputs(a,t=""):
    for i in a:
        t=t+out[i]
    return t
p.append(huffmanoutputs(name))
p.append(huffmanoutputs(rollno))
print(f"HENCE THE HUFFMAN CODE FOR THE NAME IS{p[0]}")   
print(f"HENCE THE HUFFMAN CODE FOR THE ROLLNO IS-->{p[1]}")    