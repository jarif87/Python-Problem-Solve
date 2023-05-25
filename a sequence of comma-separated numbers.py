# A tuple is container which holds a series of comma separated values (items or elements) between parentheses such as an (x, y) co-ordinate. Tuples are like lists, except they are immutable (i.e. you cannot change its content once created) and can hold mix data types.

# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')


values=input("Enter your number :")
z=values.split(",")
my_tuple=tuple(z)

print("My List is :",z)
print("My Tuple is :",my_tuple)


