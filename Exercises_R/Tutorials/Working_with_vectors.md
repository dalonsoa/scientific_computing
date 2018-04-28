#######################################################
---- 1. How to access the elements of the vectors? ----
#######################################################

You now know how to work with the different types of R vectors. However,
imagine that you want to know what the value at a specific position
is or that you even want to change it. How do you access this 
element?
Let's see some examples!

Do you remember the character vector with fruits?

fruits <- c( "strawberry", "apple", "orange", "mango" )

Imagine that I want to access the second element, "apple".
In order to do this, the syntax to be used is to write the
name of the variable and, next to it, put inside 
square brackets the number corresponding to the position
that the element you want to access is. In this case:

fruits[ 2 ]

The same applies to other types of vector.
For instance, imagine the following numeric vector:

bets <- c( 5, 100, 60, 80, 2, 64, 234, 1004 )
bets[ 3 ]


The cool thing about being able to access specific elements of
the vectors, is that you can CHANGE THEM.
Let's see some examples:

EXAMPLE 1 

fruits[ 2 ] <- "mandarin"
fruits

In this first example, we have changed the element in the second
position, "apple", to be "mandarin". Therefore, if you now print 
the vector "fruits", apple is no longer there.
However, you can add it back, if you want to:

fruits <- c( fruits, "apple" )
fruits

And then remove it again:

fruits <- fruits[ -length(fruits) ]
fruits

And then put it back :)
fruits <- c( fruits, "apple" )
fruits


EXAMPLE 2 

bets[ 2:4 ] <- rep( 6, times = length( 2:4 ) )
bets

In this second example, we have changed the values that are in
positions from 2 to 4 to be 6. Note what we have done in times.
This is useful in case you do not want to count how many values
you want this to be. As you know that you are going to be
replacing something in the range from 2 to 4, you know that 
you must replace the same amount of "6" than the amount of
values in the range. Therefore, you can get the length of this 
range of values, and just place it as the number of times
the value "6" has to be repeated as it is going to replace
the elements in vector "bet" in positions from 2 to 4 (i.e. in
total 3 times)

###########################
---- THINKING EXERCISE ----
###########################

1. Create the following vector:
   sample_vec <- c( 1, 80, 1, 41, 235, 7, 4 )
   Now grep the value "1" from that vector. You will be returned
   the positions of the values that contain 1 in "sample_vec".
   Save this output in a new vector and use it to replace
   the corresponding values with "YES".

###################
---- SOLUTION  ----
###################
sample_vec <- c( 1, 80, 1, 41, 235, 7, 4 )
positions <- grep( pattern = "1", x = sample_vec )
positions
sample_vec[ positions ] <- "YES"
sample_vec

You can also name the elements of your vectors. In order to do this,
you can use the function "name()".
Type ?name if you want to know more about this function.
Once you have named the elements of your vector, you can also
use them to access the corresponding value in that position.
Here you have an example:

animals <- c( "cat", "dog", "monkey" )
names( animals ) <- c( "an.1", "an.2", "an.3" )
animals
animals[ 3 ]
animals[ "an.3" ]

all.equal( animals[ 3 ], animals[ "an.3" ] )

This last function is very useful when you want to check if
the content of two vectors is equal. If it is equal, it
will return TRUE. Otherwise, it returns FALSE.

########################
---- QUICK EXERCISES ----
########################

1. Create a numeric vector with 3 values and put a name
   for each of them. After that, access the value in 
   the second position using the name that you have 
   given
2. Remove the second value of that vector

###################
---- SOLUTIONS  ----
###################

EX. 1 
num_vec <- c( 1, 4, 6 )
names( num_vec ) <- c( "1st", "2nd", "3rd" )
num_vec[ "2nd" ]

EX. 2 
num_vec <- num_vec[-2]
num_vec


Until now, you have been practising with some conditionals,
but now it is time for you to take a look at how a loop might
look like!

EXAMPLE 3

for ( fruit in seq( 1:length( fruits ) ) ){
  
  cat( "I like to eat", fruits[ fruit ], "\n" )  
  
}

In this first example, we are iterating over all the elements
that are inside the vector "fruits".
We are using the variable "fruit" as the number that will
indicate the position from which we want to access 
the vector fruits.
In order to specify how long the for loop has to run, we use 
"seq( 1:length( fruits ) )". If you run this individually

seq( 1:length( fruits ) )

you will see that yo get numbers from 1 to 6. This means that
every single time the for loop runs, the variable "fruit" will take
values from 1 to 6. After that, every single time that the 
variable "fruit" appears in the code inside the for loop, the 
corresponding value will be used there.
Therefore, what you are doing is using it to access all the elements
of the vector "fruits" from position 1 to position 6.

A more difficult example of for loop is a NESTED for loop.
This is a for loop inside a for loop.
Run the following example and try to figure out what it is 
doing by looking at what is being printed.
After that, talk to the tutors to ask any doubt or explain
them what you think is going on.

EXAMPLE 4 

places <- c( "Bethnal Green", "Hackney Road", "Romand Road")
for ( fruit in seq( 1:length( fruits ) ) ){
  
  for ( place in seq( 1:length( places ) ) ){
    
    cat( "I like to eat", fruits[ fruit ], "in", places[ place ], "\n" ) 
    
  }
  
  cat( "\n" )
  
}

As an exercise, gather in groups and practise a variation of
the nested for loop (e.g. printing different things, changing
the variables, etc.) in example 4 with the help of the tutors.
If you have time, you can also try to think how a while
loop should look like :) 

Last, we will see how to create a very simple function using a
conditional and a for loop. However, we are going to first create
one function that takes one argument and then returns its double.
The syntax is the following

double_function <- function ( x ){
  
  return( 2*x )
  
}

Now, when we want to call it, we call it as if it was an in-built 
function in R. We first set a variable for "x", and then
we pass it as an argument for our function

var_func <- 10 
double_function( var_func )

Now you see how your easy function has returned you 20! 
Let's add a bit of complexity inside our function

function_2 <- function ( x ){
  
  if ( x <  0 ){
    return( abs( x ) )
  }else{
    cat( "Your value is not negative!\n")
    return( x^2 )
  }
  
}
result_func2 <- function_2( var_func )

What is this function doing now? Now, it is taking the argument
that you pass it and it is checking if it is negative first.
If it is negative, it will return the absolute value.
However, if it is not, then it will first print a message 
letting you know that your value is not negative and then 
it will return this value to the power of 2, which we store as
a value of a variable named "result_func2"

########################
---- EXERCISE ----
########################

1. Use the nested for loop of the previous example and
   put it inside a function. This function will use 
   two arguments: fruits and places. After that,
   run your function with the corresponding vectors.
#
   When you observe the results, discuss with your class mates
   this result and think of which alternative vectors
   you can pass to your function and if you would like 
   to change the name of the arguments of your function.

###################
---- SOLUTIONS  ----
###################

function_ex <- function( fruits, places ){ 
  
  for ( fruit in seq( 1:length( fruits ) ) ){
  
    for ( place in seq( 1:length( places ) ) ){
      
      cat( "I like to eat", fruits[ fruit ], "in", places[ place ], "\n" ) 
    
    }
  
    cat( "\n" )
  
  }
}

function_ex( fruits = fruits, places = places )

--------------------------------
--------------------------------

#################################
---- 2. How to plot vectors? ----
#################################
A very important part of dealing with your data is knowing
how to visualize it. The function "plot()" is a basic function
to plot two vectors in the X and Y axis.
You can type ?plot to see all the rest of arguments that you can
pass to that function, which can make your plot look much nicer!
The quickest thing to do is to plot two numeric vectors one
agains the other:

x <- seq( 1:10 )
y <- (seq( 1:10 ) + 4 ) / 0.25

plot( x, y )

You can also do some barplots. Check ?barplot before running the
next command

EXAMPLE 1 
barplot( x )

EXAMPLE 2
expenses <- c( 50, 150, 30, 300 )
names( expenses ) <- c( "Jan", "Feb", "Mar", "Apr" )

Plot 1
barplot( expenses )
Plot 2
barplot( expenses, col = c( "green", "orange", "green", "red" ) )
Plot 3
barplot( expenses, col = c( "green", "orange", "green", "red" ),
         main = "Expenses 2018")
Plot 4
barplot( expenses, col = c( "green", "orange", "green", "red" ),
         main = "Expenses 2018",
         xlab = "Months", ylab = "Money spent")
Plot 5
barplot( expenses, col = c( "green", "orange", "green", "red" ),
         main = "Expenses 2018",
         xlab = "Months", ylab = "Money spent")
pos.xy <- locator()
Plot 6
barplot( expenses, col = c( "green", "orange", "green", "red" ),
         main = "Expenses 2018",
         xlab = "Months", ylab = "Money spent")
legend( x = pos.xy$x,
        y = pos.xy$y,
        legend = c( "Good!", "Be careful!", "You burnt the VISA..."),
        col = c( "green", "orange", "red" ), pch = 15 )
Plot 7
barplot( expenses, col = c( "green", "orange", "green", "red" ),
         main = "Expenses 2018",
         xlab = "Months", ylab = "Money spent")
lines(expenses, lty = 2)
points(expenses)
legend( x = pos.xy$x,
        y = pos.xy$y,
        legend = c( "Good!", "Be careful!", "You burnt the VISA..."),
        col = c( "green", "orange", "red" ), pch = 15 )

NOTES: Visit ?legend, ?pch, ?lines, ?density, ?lty

##################
---- EXERCISE ----
##################
#
1. Design your own barplot and play with the different
   arguments that can be passed to the barplot function

2. Look at examples of other kind of plots with 
   with the functions "boxplot", "histogram", "contour".
   Ask any questions you might have about them.


--------------------------------
--------------------------------

########################################
---- 2. How to deal with NA values? ----
########################################

Sometimes, you might have data with missing value. The word
that R has reserved to call the missing value is "NA". You will see
that it is blue when you type it, which means that you cannot use
it for anything else as it has this specific meaning.

If your data have NA values, there are going to be some functions
that cannot work and will return "NA" if your vector contains
missing value. You should always check the documentation before
running a function to see if there is an argument to specify
that your data have NA values. For instance, look at the "sum()"
function:

results <- c( 1, 2, 1, 1, NA, NA, 2, 2 )
sum( results )
sum( results, na.rm = TRUE )

You can also combine the functions "which()" and 
"is.na()" to find the NA values.
Type ?which and ?is.na to see how they work and then run
the following code

na_values <- which( is.na( results ) )
results <- results[ -na_values ]
results

What has this code done? Think a bit and then continue
reading for the solution.

Specifically, this code is finding the positions in the vector
"results" has missing values. After that, they are saved in the
vector named "na_values". This vector "na_values" is then used
to remove the NA values from the vector results.

Note that the function which() is very powerful. You can
also use it to find specific values in your data.
For instance, imagine that you want to find
the value/s 2 in the vector "results"

which( results == 2 )

This bit of code will return you the positions in "results"
where the values "2" are.

########################
---- QUICK EXERCISES ----
########################

1. You have the following vector:
   results_103 <- c( NA, 1, 3, 5, 6, 7, 10, -3, NA, NA, -4 )
   Find the NA values and remove them
2. Which is the sum of the values in results_103?
HARD 3. Find the maximum value and the minimum value in this vector
        HINT: Remember max() and min() functions. You want the maximum
              and minimum values, not their positions!

###################
---- SOLUTIONS  ----
###################

EX. 1 
results_103 <- c( NA, 1, 3, 5, 6, 7, 10, -3, NA, NA, -4 )
na_values   <- which( is.na( results_103 ) ) 
results_103 <- results_103[ -na_values ]
results_103

EX. 2
sum( results_103 )

EX. 3
max_val <- which( results_103 == max( results_103 ) )
results_103[ max_val ]

min_val <- which( results_103 == min( results_103 ) )
results_103[ min_val ]
