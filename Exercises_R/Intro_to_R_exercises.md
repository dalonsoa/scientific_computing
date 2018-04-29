# Introduction to R

As you have seen during the theoretical part, there are different data types in R. We are going to go through different exercises and examples so you become more familiar and comfortable when using these data types in R. For each of them, there is a specific tutorial with a description about the functions being used and some exercises so you can practise all the theory you have been learning :smile: 

In order for you to keep track of the exercises you have carried out, we think that you might find it useful to have a separate R script for each tutorial. Following the GPP, we recommend that you start each of your R scripts with the following code or something very similar:

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

# 1. Vector

The first data type we are going to work with is the vector. Remember that there are 6 different types of vectors:

* Logical 
* Numeric
* Integer
* Complex
* Character
* Raw

We are going to have a closer look at each of them, except for the “raw” vector. As introduced during the theory, this type of vector is very specific and the data we are going to be working with does not use it. However, if you are keen on knowing more about the “raw” vector, you can visit [this website](http://stat.ethz.ch/R-manual/R-patched/RHOME/library/base/html/raw.html) for more information.

##	Logical vectors

Logical vectors are used to return either `True` or `False`. They are very useful if you want to set a specific condition in order to, for instance, start a function, a loop, print a statement, etc. We are going to see some examples so you can keep practising!

* [Tutorial to work with logical vectors](https://github.com/dalonsoa/scientific_computing/blob/master/Exercises_R/Tutorials/Logical_vectors.md)

## Numeric, Integer, and Complex vectors
The vectors which value is a number have a different class depending on the kind of numbers stored: numeric, integer, or complex. Get ready to play with some examples so it is easier for you to differentiate them! 

* [Tutorial to work with numeric, integer, and complex vectors](https://github.com/dalonsoa/scientific_computing/blob/master/Exercises_R/Tutorials/Numbers_vectors.md)

## Character vectors
The last vectors we are going to see are the character vectors. These vectors contain strings, which are anything enclosed in quotation marks. Let’s get started!

* [Tutorial to work with character vectors](https://github.com/dalonsoa/scientific_computing/blob/master/Exercises_R/Tutorials/Character_vectors.md)

## Working with vectors

Your next step is to learn how to access, manipulate, and plot all the vectors that you have learnt in the previous tutorials. Good luck with the next tasks!

* [Tutorial to work with different types of vectors](https://github.com/dalonsoa/scientific_computing/blob/master/Exercises_R/Tutorials/Working_with_vectors.md)

# 2. List
The next data type we are going to work with is the list. 

* [Tutorial to work with objects of class list](https://github.com/dalonsoa/scientific_computing/blob/master/Exercises_R/Tutorials/Lists.md)

# 3. Factor
If you want to arrange your data into levels, it is important that the object that you are working with is of class factor. Learn how to work with this object in the next tutorial!

* [Tutorial to work with objects of class factor](https://github.com/dalonsoa/scientific_computing/blob/master/Exercises_R/Tutorials/Factors.md)

# 4. Matrix
The first step was learning to work with vectors, which have only one dimension. The next step is to learn how to work with matrices, which have more than one dimension! Remember that matrices are one of the mostly used classes in R to store the data! 

* [Tutorial to work with objects of class matrix](https://github.com/dalonsoa/scientific_computing/blob/master/Exercises_R/Tutorials/Matrices.md)

# 5. Data frame
Last, we are going to play with some data frames. Furthermore, we are going to learn how we can import them from a data file and how we can save them in our PC!

* [Tutorial to work with objects of class data frame](https://github.com/dalonsoa/scientific_computing/blob/master/Exercises_R/Tutorials/Data_frames.md)

