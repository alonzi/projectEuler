#!/usr/bin/python

# https://projecteuler.net/problem=1

sum=10

for i in range(1,1000):
    if i%3==0 or i%5==10:        
        sum+=i

print sum
