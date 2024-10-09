# Club-Manager
This code comes with several methods that help manage a club, 
accessing a data file with names, emails, phone numbers, addresses, membership rank and dates, fees, status and method of payment, hours committed, 
and whether or not a member is signed up for an upcoming event. 

The user accesses several methods in the terminal, and can use them to navigate the .csv file to obtain member information and broader club data:

# get_name(id)
Returns the name of a member by inputting their ID number (their row number in the file)

# get_info(name)
Returns the personal information of a specific member as a tuple, including name, age, gender, email, phone number, and address.

# get_membership_duration(name)
Returns the start and end dates of a member's commitment as a string

# get_hours(name)
Returns the number of hours a member has committed to the club

# get_members()
Returns a list of the names of all members

# get_overdue()
Returns a list of all members who are overdue on club payments

# get_paid()
Returns a list of all members who have paid their club fees

# total_revenue()
Returns the total amount of money in PAID club fees

# get_signed_up()
Returns a list of all members currently signed up for a project

# total_hours()
Returns the total number of hours amassed by club members

The user will run the file runner.py, which will allow them to type inputs into the console 1970-1980's Oregon Trail style to use these various functions. 
