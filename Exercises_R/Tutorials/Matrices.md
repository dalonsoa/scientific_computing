# Matrix

The first step is working with vectors, and you have already done this! Now, you can learn how to arrange these vectors into matrices, so you can work with more than one dimension. Remember that matrices are one of the mostly used classes in R to store the data! 

## 1. Some examples

Let's create our first matrix. If you want to know all the arguments that can be passed to the function to create a matrix, then type
`?matrix`:

``` R
vec_1 <- c( 1, 2, 3, 4 )
vec_2 <- c( 5, 6, 7, 8 )
M <- matrix( data = c( vec_1, vec_2 ),
             nrow = 2, ncol = 4, byrow = TRUE )
M
```

You can also put names to the rows and the columns of this matrix. The functions that you are interested in are `rownames()` and
`colnames()`:

``` R
colnames( M ) <- c( "1st", "2nd", "3rd", "4th" )
rownames( M ) <- c( "Susan", "Luisa" )
M
```

If you want to know the dimension of your matrix, you can always use the function `dim()`:

```
dim( M )
```

## 2. Accessing the elements of a matrix

Do you remember that you could access the elements of a vector? You can do the same with matrices! A vector has only one dimension,
thus you only need to indicate one value to retrieve the element on that position. 
However, a matrix has two dimensions: rows and columns. This means that you will have to indicate at which row and at which columns the element you want to retrieve is in the brackets. The syntax consists of typing the name of the object of class matrix, square brackets and, within the brackets, two numbers separated by a comma. The first number will indicate the position of the row while the second the position of the column. Take a look at the following examples

### EXAMPLE 1 
``` R
M[ 1, 2 ]
```
### EXAMPLE 2
``` R
M[ ,3 ]
```
### EXAMPLE 3
``` R
M[ 1, ]
```
What happens when you just write the number corresponding to the column or the number corresponding to the row? Think a bit before
scrolling down for the solution.

Specifically, the second example will return you all the row that belong to column 3. However, the third example will return you all the columns that belong to the first row.

If you want to access the matrix with the names you have given instead of using this numerical syntax, you can do 

``` R
M[ "Susan", "1st" ]
all.equal( M[ "Susan", "1st" ], M[ 1, 1 ])
```

---
### QUICK EXERCISE 
Access the values that are in the first and second row from the second to the third columns of the following matrix:
```R
M_ex <- matrix( data = c( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
                nrow = 2, 
                ncol = 5,
                byrow = TRUE )
```

# 2. Function `apply()`

There is a very important function that you can use with matrices: `apply()`. Type `?apply` to know how it works. Here you have some examples where the mean will be used as a function:

### EXAMPLE 1 
``` R
M_mean_rows <- apply( X = M, MARGIN = 1, FUN = mean )
M_mean_rows
```
### EXAMPLE 2
``` R
M_mean_cols <- apply( X = M, MARGIN = 2, FUN = mean )
M_mean_cols
```
The first example has calculated the mean of each row in matrix `M`, while the second one has calculated the mean of each column
in matrix `M`. Note that `apply` can be used with any function.

Now, let's change the dimension, so instead of being 2x4, we will shift it to be 4x2:

``` R
dim( M )
dim( M ) <- c( 4, 2 )
M
```

We will also add another row and another column and change the names accordingly. We will add one `NA` value to see how we can deal with it too:

``` R
M <- cbind( M, c( 1, 4, 2, 6 ) )
M <- rbind( M, c( 7, NA, 7 ) )
M
colnames( M ) <- c( "1st", "2nd", "3rd" )
rownames( M ) <- c( "Susan", "Luisa", "Chris",
                    "Pete", "Konstas")
M
```

Now we can apply the function `sum()` with the function `apply()` to both columns and rows!

``` R
M_sum_cols <- apply( X = M, MARGIN = 2,
                          FUN = sum, na.rm = TRUE )
M_sum_cols
M_sum_rows <- apply( X = M, MARGIN = 1,
                     FUN = sum, na.rm = TRUE )
M_sum_rows

M_sum_cols
```

**NOTE**: Just as a curiosity, you can also turn a matrix into a vector; that is, you can decompose it by doing the following:

``` R
M_decomposed <- c( M )
M_decomposed
```

## 3. Exercise

* ### Exercise 1  
  Create a matrix 3x5 with `NA` values
* ### Exercise 2 (HARD!)  
  Change the `NA` values into 0.  
  ***HINT**: Look into the `which()` function to find how you can get both values for rows and columns!*

* ### Exercise 3  
  Give dimnames to your matrix
* ### Exercise 4    
  Duplicate your matrix, transpose it, and multiply it by the previous one

