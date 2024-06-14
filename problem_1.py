#!/usr/bin/python

# https://projecteuler.net/problem=1

## this is my edit

sum=0

for i in range(1,1000):
    if i%3==0 or i%5==0:        
        sum+=i

print sum
