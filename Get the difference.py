# The said script defines a function called 'difference' that takes input(n) as an argument. Using an if-else statement the function checks whether the input value of n is less than or equal to 17. If the input value of n is less than or equal to 17, the function will return the difference of 17 - n. If the input value of n is greater than 17, the function will return double the difference of n - 17.

# Now the script calls the function twice with the input values of 22 and 14, respectively.

# In the first case the input is greater than 17, so the function returns (22-17)*2 = 10. Therefore, the script will print 10.

# In the second case the input value is less than or equal to 17, so the function returns 17-14 = 3. Therefore, the script will print 3.

def get_difference(n):
    if n <= 17:
        x = 17 - n
        return x
    else:
        x = n - 17
        y = x * 2
        return y

get_difference(22)
