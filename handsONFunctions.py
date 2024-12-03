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
    
    
    
    
    
