# What is the largest number in the Fibonacci sequence smaller than 1022?

# Tip: The Fibonacci sequence is made by creating a new number by adding the previous two, staring from 0 and 1:
# 0, 1, 1, 2, 3, 5…

# Implementation:
x0 = 0
x1 = 1
while x0 + x1 < 1e22: 
    xtemp = x1 
    x1 = x0 + x1 
    x0 = xtemp

print(x1)
# Solution:
# x1 =  6356306993006846248183 

