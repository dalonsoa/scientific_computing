# Character vectors

The last type of R vectors we are going to see in this course are the character vectors. These store values that contain strings, which are anything enclosed within quotation marks. Run the following code to see some examples with strings.

``` R
str_1 <- "Hello world!"
class( str_1 )
str_1

str_2 <- "Hi! This is my second string :)"
str_2 
```

As it happens with numeric/integer/complex vectors, we can have
a character vector with more than one element. For instance,

``` R
fruits <- c( "strawberry", "apple", "orange", "mango" )
fruits 
```

---

###  QUICK EXERCISE 
Which is the function that you can use to find how many values are stored in `fruits`?
Use it and print the result


## 1. Some useful functions

This part of the tutorial will guide you through some R functions that you can use to deal with character vectors.

### 1.1. Function `nchar()`
You can type `?nchar` in the terminal to see how it works. Run the next code to see an example of how to use it and try
to understand the output you get

``` R 
nchar( str_2 )
```

---

###  QUICK EXERCISE
Create two character vectors with the strings you want. Then, write a code that prints `TRUE` if the first vector has more characters than the second. Otherwise, it should print `FALSE`.

## 1.2. Functions `toupper()` and `tolower()`
You can type `?toupper` and `?tolower` in the terminal to see how they work. You can then run the code below to see an  example of how they work:

``` R
str_3 <- toupper( str_1 )
str_3
tolower( str_3 )
```

---

###  QUICK EXERCISE 
Convert the vector "fruits" into upper letters and then print the result. Then, convert it back into lower letters and also print the result

## 2. REGEX
There are many examples we could do with REGEX (regular expressions). However, we have limited time, so we will just do some examples and then you should complete some quick exercises. Before getting started, you should have read the documentation of the following functions: `gsub` and`grep`

We are going to create a character vector with a specific string. Afterwards, we are going to use the function gsub to find a specific pattern and then replace it by something different. Run the code below and try to understand what is  happening

### Example 1
``` R
str_4 <- c( "pineapple", "tomato", "cheese", "onion" )

str_5 <- gsub( pattern = "pineapple", replacement = "more cheese",
               x = str_4 ) 
str_5
```

### Example 2
``` R
str_6 <- "I like Greek food!"
str_7 <- gsub( pattern = "like", replacement = "love", x = str_6 )
str_7
```

### Example 3
``` R
str_8  <- "We  have   too many             spaces"
str_8
str_9  <- gsub( pattern = "\\s{2,}", replacement = " ", x = str_8 )
str_10 <- gsub( pattern = "have", replacement = "do not have",
               x = str_9 )
str_10
```

### Example 4
``` R
grep( pattern = "pineapple", x = fruits )
grep( pattern = "strawberry", x = fruits)
```

---

###  EXERCISES WITH REGEX

*TIP: go back to the slides in the theory where the REGEX were explained so it can be easier to you to solve the following exercises*

* ### Exercise 1
  You have the following character vector: `str_11 <- c( "cat", "dog", "hamster", "turtle" )`  
  Do a regex where either cat or dog are replaced with "hamster"

* ### Exercise 2
  You have the following character vector: `str_12 <- c( "bike", "bilateral", "Mike", "late" )`  
  Grep everything that contains the pattern "ike" so you can know in which positions they can be found

* ### Exercise 3
  Grep everything that ends up with "ate" in `str_12` 

* ### Exercise 4  
  Grep everything that starts with "bi"

* ### Exercise 5  
  You have the following character vector: `str_13 <- c( "abd98", "aaajlk23", "des2342kk44" )`  
  Grep everything that starts with a letter.

* ### Exercise 6  
  Grep everything that contains either "j" or "k" in `str_13`

* ### Exercise 7 ( HARD! )
  Replace any letter in `str_13` by a question mark and store the result in a new vector
  

## 3. SUMMARY EXERCISES 

* ### Exercise 1  
  Create to different numeric vectors and find which values are different between the two vectors.

* ### Exercise 2  
  Now find which values are the same.

* ### Exercise 3  
  Create a third vector that contains the union of these two vectors.

* ### Exercise 4  
  Assign the value "6.5789485" to a variable. Find out the class of this vector. Afterwards, round this value to the third digit.

* ### Exercise 5  
  Now truncate this same value.

* ### Exercise 6  
  Create a vector named "test1" that contains a sequence of values from 1 to 3 increasing every 0.3 units. What is happening when you use the function `floor( test1 )`?
