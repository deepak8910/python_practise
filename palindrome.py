#!/usr/bin/python
# purpose to check whether the given string is palindrome or not

s=raw_input("Enter string to check:")
j=len(s)-1
i=0
while(i<j):
        if s[i]!=s[j]:
                print "not palindrome"
                exit()
        i=i+1
        j=j-1

print "palindrome"
