# Data frames

Last, we are going to play with some data frames. Furthermore, we are going to learn how we would import them from a data file!

## 1. Starting with a classical example

First of all, we are going to work with the typical in-built data frame in R "mtcars". Type this name in the terminal to explore its content
``` R
mtcars
```
---

### QUICK EXERCISE
Get the dimensions, the rownames, and the colnames of this data frame. Afterwards, access the second column

## 2. Acessing the elements of a data frame
You have two ways of getting the number of rows and columns separated.

``` R
# Rows
dim( mtcars )[ 1 ]
all.equal( dim( mtcars )[ 1 ], nrow( mtcars ) )

# Columns
dim( mtcars )[ 2 ]
all.equal( dim( mtcars )[ 2 ], ncol( mtcars ) )
```

If you want to access an element of the data.frame, it works exactly as in the matrices. For instance, if you want to access the 
element from the first to the second row and from the 1st to the third column:
``` R
mtcars[ 1:2, 1:3 ]
```

## 3. Saving a data frame in a file 

If you want to save this data, remember to have previously set your working directory!
After that, we are going to use the function `write.table()` to save this data frame. In order to create a character vector with our path, which is needed for the argument `file`, we are going to use the function paste. Check the theory examples and the corresponding 
documentation to understand what is happening in the command below:

``` R

wd <- "path_to_your_wd"
setwd( wd )
write.table( x = mtcars, file = paste( wd, "mtcars_df.csv", sep = "" ),
             quote = F, sep = ",")
write.table( x = mtcars, file = paste( wd, "mtcars_df.tsv", sep = "" ),
             quote = F, sep = "\t")
```

## 3. Opening a file and saving it as a data frame

Now, if you want to open this file, you can use the function read.table() and save it into a variable so you can later explore this data frame :

``` R

mtcars_fromread <- read.table( file = paste( wd, "mtcars_df.csv", sep = "" ),
                               header = T, stringsAsFactors = F,
                               sep = ",", na.strings = "NA"
                               )

```

Now, you can see that both data sets are the same!

``` R
all.equal( mtcars, mtcars_fromread)

```

***NOTE**: If you had two data frames and you wanted to combine the columns present in both data frames, you could use the function `merge()`.*

