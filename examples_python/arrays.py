""" Arrays are included in numpy, so we need to import that library. We are going to do the following:

1) Create an array with 20 numbers from -5 to 5
2) Create another array that contains the cosine of the first array
3) Create a 1D and 2D array of random numbers uniformly distributed between 0 and 1 with 10 and 25 elements, respectively
4) Compare the result of operating with lists and arrays
5) Save some of the data in a textfile
"""

import numpy as np

# This will create an array with 20 float numers from -5 to 5, both included 
a = np.linspace(-5, 5, 20)
b = np.cos(a)

print(a, b)

# This will also create an array, but instead of defining the number of elements, you define the separation between them. The final point might or might not be included. 
c = np.arange(-5, 5, 0.4)
d = np.cos(c)

print(c, d)

# There are many other distributions implemented, like normal distirbution, binominal, poisson...
random1D = np.random.random(10)
random2D = np.random.random((5,5))

print(random1D)
print(random2D)

# You can opperate with 2D arrays the same that with 1D arrys... but the dimensions need to make snese!!
print(3 + np.cos(a))    # Will work: the number 3 will be added to all the elements of the cos(a)
#print(a + c)            # If you comment out, it will fail since a and c have diffeent sizes. Try it!!

# We compare the result of what happen if you multiply a lsist or an array by an integer. What would happen with a float?
my_list = [1, 2, 3, 4]
my_array = np.array(my_list)    # You can create an array out of alist!

print(my_list*2)
print(my_array*2)

# Save the data in a text file in the current directory, for example, the 2D array
np.savetxt("my_file.txt", random2D)

# And then, we load it back
new2Darray = np.loadtxt("my_file.txt")
print(new2Darray)