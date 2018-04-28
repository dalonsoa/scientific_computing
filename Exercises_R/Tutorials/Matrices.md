The first step is working with vectors, but now you can learn how to
arrange these vectors into matrices, so you can work with more than
one dimension. Remember that matrices are one of the mostly used classes
in R to store the data! 

Let's create our first matrix. If you want to know all the arguments
that can be passed to the function to create a matrix, then type
?matrix

vec_1 <- c( 1, 2, 3, 4 )
vec_2 <- c( 5, 6, 7, 8 )
M <- matrix( data = c( vec_1, vec_2 ),
             nrow = 2, ncol = 4, byrow = TRUE )
M

You can also put names to the rows and the columns of this matrix
The functions that you are interested in are "rownames()" and
"colnames()"

colnames( M ) <- c( "1st", "2nd", "3rd", "4th" )
rownames( M ) <- c( "Susan", "Luisa" )
M

If you want to know the dimension of your matrix, you can
always use the function "dim()":

dim( M )

Do you remember that you could access the elements of a vector?
You can do the same with matrices! A vector has only one dimension,
thus you only need to indicate one value to retrieve the element
on that position.
However, a matrix has two dimensions: rows and columns.
This means that you will have to indicate at which row and at which
columns the element you want to retrieve is in the brackets.
The syntax consists of typing the name of the object of class 
matrix, square brackets and, within the brackets, two numbers
separated by a comma. The first number will indicate the position
of the row while the second the position of the column.
Take a look at the following examples

EXAMPLE 1 
M[ 1, 2 ]

EXAMPLE 2

M[ ,3 ]

EXAMPLE 3

M[ 1, ]

What happens when you just write the number corresponding to the
column or the number corresponding to the row? Think a bit before
scrolling down for the solution.

Specifically, the second example will return you all the row that 
belong to column 3. However, the third example will return you
all the columns that belong to the first row.

If you want to access the matrix with the names you have given 
instead of using this numerical syntax, you can do

M[ "Susan", "1st" ]
all.equal( M[ "Susan", "1st" ], M[ 1, 1 ])


########################
---- QUICK EXERCISE ----
########################

1. Access the values that are in the first and second row from the
   second to the third columns of the following matrix:
   M_ex <- matrix( data = c( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
                   nrow = 2, 
                   ncol = 5,
                   byrow = TRUE )

###################
---- SOLUTION  ----
###################

EX. 1
M_ex <- matrix( data = c( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
                nrow = 2, 
                ncol = 5,
                byrow = TRUE )
M_ex[ 1:2, 2:3 ]

There is a very important function that you can use with matrices:
"apply()". Type ?apply to know how it works.
Here you have an example where the mean will be used as a 
function:

EXAMPLE 1 
M_mean_rows <- apply( X = M, MARGIN = 1, FUN = mean )
M_mean_rows

EXAMPLE 2
M_mean_cols <- apply( X = M, MARGIN = 2, FUN = mean )
M_mean_cols

The first example has calculated the mean of each row in matrix
M, while the second one has calculated the mean of each column
in matrix M. Note that this can be done with any function. 
Now let's change the dimension, so instead of being 2x4, we will
shift it to be 4x2
dim( M )
dim( M ) <- c( 4, 2 )
M

Now, we will add another row and another column and change
the names accordingly. We will add one NA value to see how
we can deal with it!

M <- cbind( M, c( 1, 4, 2, 6 ) )
M <- rbind( M, c( 7, NA, 7 ) )
M
colnames( M ) <- c( "1st", "2nd", "3rd" )
rownames( M ) <- c( "Susan", "Luisa", "Chris",
                    "Pete", "Konstas")
M

Now we can apply the function "sum" with the function
apply to both columns and rows!

M_sum_cols <- apply( X = M, MARGIN = 2,
                          FUN = sum, na.rm = TRUE )
M_sum_cols
M_sum_rows <- apply( X = M, MARGIN = 1,
                     FUN = sum, na.rm = TRUE )
M_sum_rows

M_sum_cols

You can also turn into a vector a matrix, that is, 
you can decompose it by doing the following:

M_decomposed <- c( M )
M_decomposed

###################
---- EXERCISEs ----
###################

1. Create a matrix 3x5 with NA values
#
HARD 2. Change the NA values into 0
        HINT: Look into the which() function to find how you
              can get both values for rows and columns!

3. Give dimnames to your matrix
#
4. Duplicate your matrix, transpose it,
   and multiply it by the previous one

###################
---- SOLUTION  ----
###################

EX. 1
M_ex2 <- matrix( data = c( 1, 2, 3, NA, 5,
                           6, NA, 8, 9, 10,
                           4, 5, NA, NA, 8 ),
                nrow = 3, 
                ncol = 5,
                byrow = TRUE )
M_ex2 

EX. 2
pos <- which( is.na( M_ex2 ), arr.ind = T )
M_ex2[ pos ] <- 0
M_ex2

EX. 3
dimnames( M_ex2 ) <- list( c( "Carlos", "Susan", "Lisa" ),
                         c( "1st", "2nd", "3rd", "4th", "5th" ) )
M_ex2

EX. 4 
M_ex3 <- M_ex2
M_ex3 <- t( M_ex3 )
M_ex4 <- M_ex2 %*% M_ex3
M_ex4 

----------------
---------------

###########################
---- EXTRA INFORMATION ----
###########################

There are three functions that you can use to visualize the
content of your matrices: contour, persp, and image. 
Look at their documentation and then try to run them with 
an in-built data set in R, the "volcano" data set

contour( volcano )
persp( volcano )
image( volcano )

Look the content of volcano and discuss it with your class mates!
