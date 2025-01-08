# 1. What is an integer data type? integers are pieces of data that represent whole numbers. 

#2. In your own words, describe what an if/ else conditional statement is?
# An if/else statement helps a program make decisions based on conditions."

#3. In your own words, describe what a function is? 
# A function is a block of code that runs when called to perform a task.

#4. What is a boolean data type? Booleans are pieces of data that represent true or false values 

#5. In your own words, describe the difference between a function parameter and a function argument?
# A parameter is a placeholder in the function, 
# while an argument is the value passed when calling the function.

#6. Which operator would work best for the following function:
# An digital locker function that needs to have a specific set of numbers to
# be entered in order to lock and unlock a locker in a gym? the best operator is "==".

#7. Which operator would work best for the following function: 
# A height verification function that needs to check if a user 
# is a certain height to get onto an amusement park ride? the best operator is ">=".

# 8. You have been hired as an engineer to develop a sales tax function for the state of Pennsylvania.
# They would like to be able to take in a annual ammount of money businesses in the state 
# make and deduct the proper amount of taxes from the their earnings. 
# state of PA should take 7% of a companies earnings. 
# Your function should take in a total sales amount as an argument and return the
# amount thats owed to the state.

def calculate_sales_tax(total_sales):
    tax_rate = 0.07
    tax_amount = total_sales * tax_rate
    return tax_amount

sales = 200000
print(f"The sales tax owed is ${calculate_sales_tax(sales)}.")

#9. You have been hired by Apple to help them fix their password system.
# They would like you to create A function that will check how long a password is. 

def check_password_length(password):
    password_length = len(str(password))
    if password_length > 10:
        return "Your password is too long."
    elif password_length < 4:
        return "Your password is too short."
    else:
        return "Password created successfully."

password = 12345
print(check_password_length(password))

#10. You have applied to several colleges in the state of PA and as your
# final project, you must create a function that will inform you on whether
# you will be admitted into the school based on the schools' reccomendation letter criteria.
# Your function should take in the name of the school along with whether it is TRUE or FALSE that you 
# recieved a reccomendation letter from one of the staff members at Boys Latin.

def college_admissions(school, letters_count):
    if school == "Temple University" and letters_count >= 1:
        return "You got into Temple University."
    elif school == "Penn State" and letters_count >= 2:
        return "You got into Penn State."
    elif school == "University of Pennsylvania" and letters_count >= 2:
        return "You got into University of Pennsylvania."
    elif school == "Cheyney University" and letters_count >= 1:
        return "You got into Cheyney University."
    else:
        return f"You did not get into {school}."


print(college_admissions("Temple University", 1))
print(college_admissions("Penn State", 1))
print(college_admissions("University of Pennsylvania", 2))
print(college_admissions("Cheyney University", 2))