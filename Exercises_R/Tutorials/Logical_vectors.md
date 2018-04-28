# Logical vectors
If you want to give a vector the value of `True`, you can either assign the word `TRUE` or the letter `T` to the name of your variables
without quotation marks. To assign the value of `False`, the same syntax would apply. Therefore:

``` R
a_true <- TRUE
b_true <- T 

c_false <- FALSE
d_false <- F
```

Note that, if you are working with RStudio, you will see that the words `TRUE` and `FALSE` and the letters `T` and `F` are blue. This means that they are reserved words to be used in the R syntax because they mean something (they are Booleans!), so they **SHOULD NOT BE USED** to name variables, functions, arguments for functions, etc. to **AVOID CONFUSION**. Sometimes, we even recommend you type the whole words in case there is a package in which the letters `T` and/or `F` have been used for something else...

## 1. Examples
For the first example, imagine that you have been running your code and you want to print a message if the variable that you have been returned from a function is `False`. 

``` R
returned_val <- FALSE

if ( returned_val == FALSE ){
  print( "This function has not worked. Re-run again changing options" )
}
```

When you runed the code above, you will see how the message is printed because the variable `returned_val` equals to `FALSE`. Note how we type two equals when we are evaluating the content of a variable. If you typed one equal, you would be **ASSIGNING** this value
to the variable (like using the arrow), thus you would not be checking if the value of `returned_val` is `FALSE`. You would be 
assigning the value `FALSE` to the variable `returned_val`. 
**THIS IS NOT WHAT YOU WANT¬** (remember the operators we talked about during the theoretical part!)
For instance, see what would happen if we changed the value of a variable with the same name

``` R
returned_val <- 2 
returned_val
returned_val <- TRUE
returned_val
``` 

Run the code above. What has happened when you have assigned a new value to a variable called the same? This just gives you an idea of how important it is to keep track of the names you give to your variables and to be aware of how easy it is to change its value! This might be useful in some cases, but sometimes it is not what you wish you to do. Therefore, be aware of that!

Now you can practise some of the operators we saw during the the theoretical part correspondg to and, or, and negation.
Run the code below and try to understand what is happening.

``` R
a_true | c_false

a_true & c_false

! b_true 
```

## 2. Exercises

* ### Exercise 1  
  Change the value of `returned_val` to `TRUE`. What happens with the conditional?
  
* ### Exercise 2  
  What do you expect to get when you type `2+2 == 5`? Check it in the terminal.
  
* ### Exercise 3    
  What do you expect to get when you type `T == TRUE`? Check it in the terminal.

* ### Exercise 4  
  Run the following code and try to figure out what is happening with the value of the variable `val_1`:
  ``` R
  val_1 <- FALSE 
  
  if ( val_1 == TRUE ){
    val_1 <- 2
  }else
    val_1 <- TRUE
  
  val_1
  ```
  
* ### Exercise 5  
  Write a code that does the following:  
    a) You have a conditional checking that your variable `X` is higher than 3.  
    b) If this is `TRUE`, then assign a new value to `X`: `FALSE`. Otherwise, assign `X` the value of `2`.  
    c) Print `The value of my variables is` followed by the value of your variable.  
         ***HINT**: Remember how we printed things in R that combined characters and numerical values in the examples given in  
                   the theoretical part!*  
    d) If you want a hard task, try to put an `else if` saying that if your variable is equal to `5`, it should print:  
       `I went into the else if because my variable is equal to 5!`


