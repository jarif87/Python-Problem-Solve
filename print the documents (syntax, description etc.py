
print(abs.__doc__)

#%%
def custom_abs(x):
    """
    Custom implementation of the absolute value function.

    This function takes a number as input and returns its absolute value.
    If the input is positive or zero, the same number is returned.
    If the input is negative, its negation is returned.
    """

    if x >= 0:
        return x
    else:
        return -x

print(custom_abs.__doc__)
