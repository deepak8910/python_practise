#!/usr/bin/python

fd = open("ip.txt",'r')
ip=[]
ip=fd.readlines()
print ip
print set(ip)
