# Introduction to R

As you have seen during the theoretical part, there are different data types in R. We are going to practise with each of them so you can get more familiar and comfortable with them. For each of the tutorials, you should open a new R file in RStudio and start with the following code:

```
# Introduction to R – 180428
# This code contains the material used for the Introduction to R part of the 
# SRUK Scientific Computing course
# Tutorial #X - <write the tutorial here>

# First, we are going to clean the environment to ensure that anything
# from previous sessions is loaded 
rm( list = ls( ) )

# Now we are going to set our working directory. The variable wd will be assigned a specific value: your working directory.
# Therefore, it is going to be a character vector!
wd <- “type_here_the_path_to_your_wd”

# Now, we are going to set our working directory to this path. This means that if you save something, it will be saved in this directory now
setwd( wd )

# We are going to set a specific seed, in case you want to reproduce exactly
# the cases that we are going to be practising here.
# Setting a seed is like putting a label to this code so every single time 
# that you run it you will get the same results. This is very important to 
# use as scientists, as we all want to be working with REPRODUCIBLE results 
# so we can get the same results that another person has obtained! 
# By default, it is an odd number, and people tend to use 12345. However,
# feel free to change this number if you want to. Just make sure you do not 
# change it when you rerun this code! Keep it always the same to always 
# reproduce the same results!

set.seed( 12345 )

# From now onwards, remember to comment why you are doing something and why you are using a specific command. This might helpset our working directory to this path. This means that if you save something, it

```

# VECTORS

The first data type we are going to work with is the vector data type. Remember that there were 6 different types of vectors:
* Logical 
* Numeric
* Integer
* Complex
* Character
* Raw

We are going to have a closer look at each of them, except for the “raw” vector. As introduced during the theory, this type of vector is very specific and the data we are going to be working with does not need it. However, if you are keen on knowing more about the “raw” vector, you can visit this website for more information.

##	Logical vectors

Logical vectors are used to return either True or False. They are very useful if you want to set a specific condition to, for instance, start a function, a loop, print a statement, etc. We are going to see some examples so you can keep practising!

## Numeric, Integer, and Complex vectors
The vectors which value is a number have a different class depending on the kind of numbers stored: numeric, integer, or complex. Get ready to play with some examples so it is easier for you to differentiate them! 

## Character vectors
 The last vectors we are going to see are the character vectors. These vectors contain strings, which are anything enclosed in quotation marks. Let’s get started!

Now that you know better how to work with the different R vectors, the next exercises are going to teach you the following:
1.	How to access the elements stored in the vectors
2.	How to plot the content of the vector
3.	How to deal with missing values (NA)

# LISTS
The next data type we are going to work with is the list. 

# FACTORS
If you want to arrange your data into levels, it is important that you convert your data into factor class. Learn how in the next tutorial!

# MATRICES
The first step is working with vectors, but now you can learn how to arrange these vectors into matrices, so you can work with more than one dimension. Remember that matrices are one of the mostly used classes in R to store the data! 

# DATA FRAMES
Last, we are going to play with some data frames. Furthermore, we are going to learn how we would import them from a data file!

