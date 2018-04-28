# Factor
If you want to arrange your data into levels, it is important that you convert your data into factor class. Learn how in the next tutorial!

## 1. Some examples

Imagine that you have a big database where the information people have provided you with can be classified into three categories:
"Academia", "Industry", "Both". You have asked 10 people about the places that they have worked/are currently working. The following
vector contains the answers of these people:

``` R
work <- c( "Academia", "Academia", "Academia", "Industry", "Both",
           "Both", "Both", "Industry", "Both", "Academia", "Industry")
```

In this case, you see that these three answers are repeated, which means that you can think of them as `levels` in an object of class
factor in R. In order to convert identify the levels of a vector,you just have to type the following command using the function
`factor()`:

``` R
types_work <- factor( work )
types_work
class( types_work )
```

When you print the content of `types_work`, you see that the 10 names appeared first, labelled from 1 to 10. After that, you see
that it is printed `3 Levels: Academia ... Industry`. This means that your `types_work` variable contains the levels of your data already!
If you want to retrieve only the name of your `levels`, you can use he function `levels()`:
``` R
levels( types_work )
```

One of the most important utilities of the factors is the way they can be used to plot the information they refer to. Let's add now another part of the information we have in our database:

a) The amount of time they had worked in a previous job
b) The amount of time they have been working in current job

``` R
time_previous <- c( 0, 1, 0, 5, 6, 10, 2, 10, 20, 1 )
time_current <- c( 5, 8, 3, 2, 5, 3, 3, 1, 2, 4 )
```
Now, let's plot the content of these variables!

``` R
# Plot without information about level
plot( time_previous, time_current )

# Plot with information about level
plot( time_previous, time_current, pch = as.integer( types_work ) )

```

Note that in the second plot, you can see different symbols. This is because, for each level, the argument `pch` has assigned a different symbol so you can identify which point belongs to which level. However, you also need the legend!

``` R
points <- locator()
legend( x = points$x, y = points$y,
        legend = levels( types_work ),
        pch = unique( as.integer( types_work ) ) )
```

***NOTE**: Read the documentation of `?unique`*

## 2. Exercise
Partner with some of your class mates and discuss all the examples presented in this tutorial. Change parameters, plot different values, look into new functions, etc. For instance, you could try to see how you can have one specific colour in the plot for each level!

