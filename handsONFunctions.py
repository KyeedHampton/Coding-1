# Discuss the anatomy of a function

# a Function definition tells the computer
# the instructions on what we want to do with

# data = just means data types 

# curly brackets = passing in data into
# the function definiton. THis is formally
# called a parameter

# parameter = placeholder for  data 

def modifyMyName(name):
    print('your new modified name is the great'+ name)
 
# when we pass data into a function call it is called an
# arguement
# argeument = evidence, facts, real data.    
 modifyMyName('Kyeed')
    
    
    

# Lesson on Conditional Statements

# Conditional Statements use the 'IF' and 'ELSE'
# keywords to filter and create specific outcomes 
# based on data.

def verifyAge(age):
    if age > 17 and age < 20:
        print('Congrats! you can buy GTA VI') 
    elif age > 20:
        print('Sorry youre too old for this game.')
    else:
        print('Sorry, you need an adult to buy this game.')
        
verifyAge(69)
    


# 1. Create a function that will take a number 
# that is passed into the functions parameters and 
# convert the number into minutes. For example, a
# value of 2 shold return 120 minutes, a value 
# of 3 shold return 180 minutes, a vaue of 4 shold 
# return 240 minutes, etc. 
    
    
# def hoursToMinutes(hour):
    print(hour * 60)


# hoursToMinutes(3)

# Conditional Statements 
# if/else keywords; gives us the abilly to
# control outcemos and make decisions on data.

# food expiration software is an example of 
# using conditional statements. If the food expires 
# it needs to be thrown away, otherwise, or else
# it can be eaten. 

def foodExpiration(month, data, year):
     expirationMonth = 12
     expirationData = 4
     expirationYear = 2024
     if data > expirationDate and year > expirationYear:
         print('throw food away. ')
     else:
         print('food is still good.')

foodExpiration(12, 4, 2024)
    