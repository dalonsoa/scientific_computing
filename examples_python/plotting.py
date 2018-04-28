""" For plotting, we use the tools in matplotlib, so we have to import the library. We also import numpy, 
since very often we will plot the data contained in arrays. 

"""
import matplotlib.pyplot as plt
import numpy as np

# This will create an array with 20 float numers from -5 to 5, both included 
a = np.linspace(-5, 5, 25)
b = np.cos(a)

# Time to plot using lines (-) and dots (o), the first in red and the second in blue. We also add some labels to put int he legend, a title for the x axis and the y axis. There are tons of options!!! 
plt.figure(1)
plt.plot(a, b, "r-o", label="My data red")
plt.plot(a, 2*b, "b-o", label="My data blue")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()

# We can plot now the 2D array with random numbers. 
random2D = np.random.random((25,25))

# imshow is a straight forward method for ploting 2D data, but does not allow to set the values of the x and y axis easily. The data is just plotted as pixels. 
plt.figure(2)
plt.imshow(random2D)
plt.colorbar()

# Let´s create a slightly more interesting data multipliying b by our 2D array. We can do so because they have the same number of elements
new2Darray = b*random2D

plt.figure(3)
plt.imshow(new2Darray)
plt.colorbar()

# If we want colour plots but with better control, we need to create slightly different variables
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 80)
X, Y = np.meshgrid(x, y)

# X and Y (capital letters) are now arrays with 8000 elements with all possible combinations of the elements of x and y
other2D = np.cos(Y*2)*np.cos(X*3)*np.exp(-(X*Y)**2)

plt.figure(4)
plt.contourf(X, Y, other2D, 100, cmap=plt.cm.jet)
plt.colorbar()

# The above just plot the data, but to show it on the screen we need
plt.show()