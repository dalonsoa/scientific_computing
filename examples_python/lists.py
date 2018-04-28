""" This is a block comment, often used to explain the funcitonality of a module, a function or a class.

Create a list with the following elements:

“vanilla", "strawberry", "chocolate", ”paella", "bacon", "green egg", "snail and lettuce”

1) Swap the first two items in the list. 
2) Reverse the list with slices (what are slices?)

Slices area way of accessing and using a group of elements of a list (or a numpy array) at once. For exmaple:

my_list[1:4]

will select the elements between the 2nd (remember that indices in Pyton start in 0) and the 4th. The element 
indicated by the first index is included but the one indicated by the last one is not. 
A third index indicates the step:

my_list[1:4:2]

will select the 2nd and the 4th elements only, not the 3rd. If the step is negav¡tive, the order in which the elemtns
are given is reveresed... as long as we give indices in the oposite order:

my_list[1:4:-2]     <-- This will produce an enpty list
my_list[3:0:-2]     <-- This will produce the same list that my_list[1:4:2] but in the opposite order

3) Sort the list of icecream flavours alphabetically
4) Remove the “egg” and insert two additional flavours of your choice. 
"""

icecream_flavours = ["vanilla", "strawberry", "chocolate", "paella", "bacon", "green egg", "snail and lettuce"]
print(icecream_flavours)

icecream_flavours[0], icecream_flavours[1]  = icecream_flavours[1], icecream_flavours[0] 
print(icecream_flavours)

icecream_flavours = icecream_flavours[::-1]
print(icecream_flavours)

icecream_flavours.sort()
print(icecream_flavours)

icecream_flavours.remove("green egg") 	#This will produce an error if “green egg” does not exists
icecream_flavours.append("fried chicken")
icecream_flavours.append("pineapple")
print(icecream_flavours)
