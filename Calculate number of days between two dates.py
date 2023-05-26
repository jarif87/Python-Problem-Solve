from datetime import date
first_date=date(2022,5,8)
last_date=date(2022,8,10)
x=last_date-first_date
print(x.days)

#%%
from datetime import date

# Get the first date from the user
first_year = int(input("Enter the year of the first date: "))
first_month = int(input("Enter the month of the first date: "))
first_day = int(input("Enter the day of the first date: "))
first_date = date(first_year, first_month, first_day)

# Get the second date from the user
last_year = int(input("Enter the year of the last date: "))
last_month = int(input("Enter the month of the last date: "))
last_day = int(input("Enter the day of the last date: "))
last_date = date(last_year, last_month, last_day)

# Calculate the difference
difference = last_date - first_date
print("The difference in days is:", difference.days)

