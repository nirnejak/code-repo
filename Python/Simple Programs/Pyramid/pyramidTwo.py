# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:55:42 2017

@author: Jittu
"""

n=int(input("Enter End of Series : "))

for i in range(1,n+1):
	for j in range(n,n-i,-1):
		print(j, end=" ")
	for k in range(i,n+1):
		print(k, end=" ")
	print("\r")

x=input()