#!/usr/bin/python

def prime(n):
 flag = 0
 for i in range(2,(n/2)+2):
   if n%i==0:
     flag = 1
     return "composite"

 if flag==0:
   return "prime"

#n = int(raw_input("enter number : "))
for n in range(1,1000):
  print n,"is ", prime(n)
