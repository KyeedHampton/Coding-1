# data types - level 1: most basic building block of 
# code . (number, letters, true or false)

# operators - level 2: the ability to manipulate and
# do things with data types 
# (math, comparisons, assignment, etc. )

#functions - level 3: taking the first two concepts and 
# organizing these operations and data types 
# into instructions 

3# conditional statements: level 3a: beeing able 
# to add ,ore control on our function instructions. 


# Billing System Function. 
#Goal: To be able to check and see if a user is past
#due or up-to-date on their subscription.

# We nedd to know if their account is 
# past due Or up-to-date

# function definition - tells the computer what the
# function actually does and how its supposed to work.
def checkSubscription(userMoneyInAccount, userDueDate): 
    if userDueDate == 6:
      if userMoneyInAccount == True:
        print('subscription is paid- auto withdraw payment.')
      else: 
        print('payment still do- could not withdraw fund.')
    else:
     print('payment is not due yet.') 
    
    
checkSubscription(True)