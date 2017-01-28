#!/usr/bin/python

a=[]
f = open('pledge.txt','r')
a=f.readlines()
print a
b = set(a)
b = list(b)
print b
fh = open("sample.txt",'w')
#fh.write(line) for line in b
for line in b:
	fh.write(line)
fh.close()
