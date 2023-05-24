

# The said code imports the "datetime" module, gets the current date and time, and finally prints it in a formatted string.

# The first line import datetime imports the datetime module which supplies classes for manipulating dates and times.
# The second line now = datetime.datetime.now() creates a datetime object for the current date and time.
# The third line print ("Current date and time : ") prints the string "Current date and time : " to the console.
# The fourth line print (now.strftime("%Y-%m-%d %H:%M:%S")) uses the strftime() method of the datetime object to format the date and time as a string in the format "YYYY-MM-DD HH:MM:SS" and prints it to the console.
# The strftime() method returns a string representing the date, controlled by an explicit format string. The format codes used in this example are:

# %Y: year with century as a decimal number.
# %m: month as a zero-padded decimal number.
# %d: day of the month as a zero-padded decimal number.
# %H: hour (24-hour clock) as a zero-padded decimal number.
# %M: minute as a zero-padded decimal number.
# %S: second as a zero-padded decimal number.
# This code can be useful for logging or timestamping events in a program, or for displaying the current date and time in a user interface.


import datetime
now=datetime.datetime.now()

print("Current Date Time")

print(now.strftime("%d-%m-%Y %H:%M:%S"))





