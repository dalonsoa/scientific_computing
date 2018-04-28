# The next data type we are going to work with is the list. 
# The main function of the lists is to keep everything ordered
# under a specific name. You can even think of it as a dictionary,
# because you can access the elements of a list by the name
# you have given to every entry. In order to understand this better,
# let's see an example!


# Susan and Luisa have collected some fossils, so they have decided
# to identify them. In order to differentiate which species have been
# sampled by who, we have created the following list:

fossils <- list( susan = c( "Tomarctus", "Smilodon", "Hesperocyon" ),
                 luisa = c( "Aelurodon", "Enhydrocyon" ))

# If you want to know which species have been sampled by Susan and
# which by Luisa, the syntax to access the entries of a list is to
# first type the name of the list, followed by the dollar sign "$",
# and then the name of the entry (in this case either "susan" or
# "luisa").
# However, if you know the position of the entry you want to retrieve,
# you can also type the name of the list and then, in DOUBLE square
# brackets, the number corresponding to the position of
# the entry you are interested to retrieve

fossils$susan
all.equal( fossils$susan, fossils[[ 1 ]] )

fossils$luisa
all.equal( fossils$luisa, fossils[[ 2 ]] )

# As you can see, it is much understandable to use the dollar sign
# followed by the name of the entry, so we recommend you to name
# the entries of your lists!
# You can also access specific elements of each entry using the
# single square brackets. If you want to get the first element
# of the entry named "susan", just type:

fossils$susan[ 1 ]
all.equal( fossils[[ 1 ]][ 1 ], fossils$susan[ 1 ] )

# Maybe, you want to change the name of the entries at some point.
# If this is the case, you can use the function "names()".
# For instance, imagine that now we want to
# have the first letter of the names of the entries as a capital 
# letter because it is a name:

names( fossils ) <- c( "Susan", "Luisa" )
fossils$Susan
fossils$Luisa 

# Furthermore, there is a function called "attach()" that lets you
# have your list as part of the R path, so you do not need to type
# "fossils$Susan" or "fossils$Luisa" to retrieve the elements of each
# entry. On the contrary, you should just type "Susan" or "Luisa", 
# the names of the entry.
# [[ IMPORTANT ]] When you finish using your list,  please DETACH
# the list from the path. This might save you from more than one
# headache in the future!

attach( fossils )
Susan
Luisa 

detach( fossils )
fossils$Susan
fossils$Luisa

# ###################
# ---- EXERCISES ----
# ###################

# 1. Create a list with the favourite colours of 3 people.
#    HINT: Think how many entries you need for that!
#
# 2. Access the second entry of your list in the two ways
#    you have learnt and check they return the same value!
# 
# 3. Access the first and second elements of the third entry of your 
#    list
#
# 4. Find which are the colours that both the person in the first
#    and in the second entry like.
#    HINT: Remember some functions we used with the numeric vectors!

# ###################
# ---- SOLUTION  ----
# ###################

# EX. 1
colours <- list( Anastasis = c( "blue", "yellow", "green"),
                 Sandra = c( "blue", "black", "white"),
                 Marta = c( "blue", "yellow", "purple") )

# EX. 2
colours$Sandra
colours[[ 2 ]]
all.equal( colours$Sandra, colours[[ 2 ]] )

# EX. 3
colours$Marta[ c( 1,2 ) ]
colours[[ 3 ]][ c( 1,2 ) ]

# EX. 4 
intersect( colours$Anastasis, colours$Sandra )


