We saw in the theoretical part that there are three 
different types of classes for vectors that store numbers:
numeric, integer, and complex.
Run the following code to see some examples of these classes of 
vectors:

a_int <- -786L
class( a_int )

b_complex <- 3+2i 
class( b_complex )

c_num <- 1.5
class( c_num )

Do you remember that we talked about functions for coercion? 
Imagine that we want to change a numeric vector into an
integer one:

num_to_int <- as.integer( c_num )
class( num_to_int )
num_to_int

Do you see what has happend? The decimal part of "1.5", value
assigned to the variable "c_num" has been removed to keep only
the integer part as asked. That is why you see that this 
new variable "num_to_int" equals to "1" :) 

#########################
---- QUICK EXERCISES ----
#########################

1. Try to remember which was the functions used to change the
   class of a variable to complex.
   Then, change the class of the "c_num" variable to complex.
2. Now try to remember the function to change the class of
   a variable into numeric.
   Then, change the class of the "a_int" variable to numeric.

###################
---- SOLUTIONS ----
###################

EX. 1
num_to_comp <- as.complex( c_num )
class( num_to_comp)
num_to_comp

EX. 2
comp_to_num <- as.numeric( a_int )
class( comp_to_num )
comp_to_num

If you want to check the class of a vector, you 
can always run the function is.<CLASS_NAME>( <VARIABLE> ).

x <- 7
is.integer( x )
is.numeric( x )
is.complex( x )

Note that sometimes you do not see a decimal part in a numeric 
vector even though its class is numeric. If you really want to
be working with integers, make sure to use the corresponding
coercion function!

One of the most useful utilities of R is that it can be used 
as a calculator! Therefore, you can use all the variables
that store numbers as value as part of calculations. 
Run the examples below and get familiar with the syntax 
used: 

a <- 2 
b <- 5 

Sum 
a + b 

Subtraction
a - b 

Multiplication
a * b

Divison
a / b

Square root
sqrt ( a )

Exponentiation
a^b

Get the remainder of a division
a %% b

Get the quotient of a division
a %/% b


#########################
---- QUICK EXERCISES ----
#########################

1. Store in a new variable the result of "a" to the power of 2
   and write a condition that prints the result of this
   calculation if this is higher than 5.
2. Store in a new variable the result of the square root "b" and
   write a condition that prints the remainder of dividing
   b into this new variable if this new variable is smaller than
   the result you got in exercise 1.

###################
---- SOLUTIONS ----
###################

EX. 1
a <- 2
res <- a^2 
if ( res > 5 ){
  print( res )
}

EX. 2
b <- 5
res_2 <- sqrt( b ) 
if ( res_2 < res ){
  print( b %% res_2 )
}


The last part of this tutorial will guide you through some 
R functions that you can use for some calculations. 

Function "sum()"
You can type ?sum in the terminal to see how it works.
In the next example, we are going to create a numeric vector with
more than one value. We are going to use this function to get
the sum of all the values of this vector. When we create this
kind of vector, we always put a "c" (which means "combine")
followed by parentheses.
Inside the parentheses, we type all the values separated by commas.
Pay attention to what happens when you place two dots between
two numbers!

vector_1 <- c( 1, 4, 5, 7:9, 12 )
vector_1
sum( vector_1 )

Have you noticed that "7:9" has returned the sequence from 7 to 9?
You can have a sequence between two values by separating them
using ":" or you can also use the function "seq()". 
Type ?seq to see how this function works.

#########################
---- QUICK EXERCISES ----
#########################

1. Create two different numeric vectors with as many values 
   as you want. Then, use the function sum to get 
   the result of summing the values in both vectors.
2. Create a vector that contains a sequence from 1 to 10.
3. Create a vector that contains a sequence from 5 to 1.
   Note that the results should be "5 4 3 2 1"
4. Create a vector that contains a sequence from 1 to 10
   every two numbers, i.e. It should return "1 3 5 7 9"
   HINT: Look how seq() can be used for that!

###################
---- SOLUTIONS ----
###################

EX. 1

vec_1 <- c( 1, 2, 3 )
vec_2 <- c( 4, 5, 6 )
sum( vec_1, vec_2 )

EX. 2
vec_3 <- c( 1:10 )
vec_3

EX. 3
vec_4 <- c( 5:1 )
vec_4 

EX. 4
vec_5 <- c( 1:10 )
vec_5 

EX. 5
vec_6 <- seq( from = 1, to = 10, by = 2 )
vec_6

Functions "min()" and "max()"
Use ?min and ?max to see how these functions work. 
Now run the code below and try to understand the values you are
returned

max( vector_1 )
min( vector_1 )

#########################
---- QUICK EXERCISE ----
#########################

1. Write a code that prints "Maximum and minimum are equal"
   if the maximum number of a vector you create does not equal to
   the minimum number of this same vector. Otherwise, it should
   print "Maximum and minimum are equal" if they are

###################
---- SOLUTION ----
###################

EX. 1

vec_7 <- c( 1, 2, 3, 5 )
if ( max( vec_7 ) != min( vec_7) ){
  print( "Maximum and minimum are not equal")
}else if( max( vec_7 ) == min( vec_7) ){
  print( "Maximum and minimum are equal")
}

Function rep()
Type ?rep and take a look at how this function works.
Imagine that you want a vector with a specific value
repeated X times. You can use this function as in the following
example:
vector_2 <- rep( 6, times = 5)
vector_2

#########################
---- QUICK EXERCISE ----
#########################

1. Repeat a sequence from 1 to 3 five times.

###################
---- SOLUTION ----
###################

EX. 1

vec_8 <- rep( seq( 1, 3 ), times = 5 )
vec_8 


There are many other functions that we can use, but we will either
see them in next tutorials or you will find them when working
with your own data :) 
Now it is time for some exercises!

NOTE: Before getting started with the exercises for this tutorial,
      please make sure that you have checked the following
      functions and you understand how to use them. Otherwise,
      ask the tutors for help :)
      Functions: floor, trunc, round, signif, union,
                 intersect, setdiff, length


####################
----  EXERCISES ----
####################

1. Create to different numeric vectors and find which values 
   are different between the two vectors.
2. Now find which values are the same.
3. Create a third vector that contains the union of 
   these two vectors.
4. Assign the value "6.5789485" to a variable. Find out the class
   of this vector. Afterwards, round this value to the third digit.
5. Now truncate this same value.
6. Create a vector named "test1" that contains a sequence of
   values from 1 to 3 increasing every 0.3 units.
   What is happening when you use the function floor( test1 )?
7. Create a vector named "test2" that contains a sequence of 
   values from 1 to 20 increasing every 0.7 units. 
   How many values does "test" contain?
8. Write some code that prints
   "Vector test1 has more values than test2:", followed by the length
   of test1. Remember the function cat() that we showed you
   during the theory to print strings with both characters and 
   numbers.
   Otherwise, if "test2" has more elements, the code should print
   "Vector test2 has more values than test1:", followed by the length
   of test2. Last, if both lengths are equal, the message that should be printed 
   is "Both lengths are the same:" followed by the corresponding
   length. 


###################
---- SOLUTIONS ----
###################

EX. 1
vec_9  <- c( 1, 4, 5, 1 )
vec_10 <- c( 1, 3, 3, 6 )
setdiff( vec_9, vec_10 )

EX. 2
intersect( vec_9, vec_10 )

EX. 3
vec_11 <- union( vec_9, vec_10 )

EX. 4
vec_12 <- 6.5789485
class( vec_12 )
round( vec_12, digits = 3 )

EX. 5
trunc( vec_12 )

EX. 6
test1 <- seq( from = 1, to = 3, by = 0.3 )
floor( test1 )

EX. 7
test2 <- seq( from = 1, to = 20, by = 0.7 )
length( test2 )

EX. 8

if ( length( test1 ) > length( test2 ) ){
  cat( "Vector test1 has more values than test2:", length( test1 ), "\n" ) 
} else if ( length( test1 ) < length( test2 ) ){
  cat( "Vector test2 has more values than test1:", length( test2 ), "\n" )
} else
  cat( "Both lengths are the same: ", length( test2 ) )
