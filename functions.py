#What is a function?

#A function is a set of instruction that performs a specific
#task or job.

#here are two variations of functions in Python 
# Built-in Functions- instructions that are pre-written in python 
# programming  language.

# print() is a built in  function. WHen we pass in data it will output 
# it into the the terminal automtically. 
print('Coding Class')

# input is a built in function. It allows  us  to write and  pass in 
#dat into our program from terminal.
name = input('What is your name?')
print(name)

number= int(input('please provide a number'))
print(23*number)

# User Defined Functions- custom functions written by engineers.

#Function Syntax - how it is written

def sandwichInstructions():
    print('step 1. get 2 pieces of dread')
    print('step 2. putting ingredients inside of bread')
    print('step 3. put bread with ingredients together.')
    
#there are two states of a user defined function;
   #the function  defintion
   #the function call
   
# this is a function call 

#.sandwichInstructions()

# 11/20/24

# functions using arithmeic operators 

def depositMoney(x):
    checkingAccount = 100
    print('money has been deposited sucessfully')
    print('new checking account balance is below ')
    print(x + checkAcountBalance)

depositMoney(35)    
depositMoney(200)
depositMoney(95)

def withdrawMoney():
    checkAccount=300
    print('money has been withdrawn successfully')
    print('new checking account balance is below: ')
    print(checkAccount - x)
    
    withdrawMoney(200)
    
def checkAcountBlance():
    checkAccount = 1000
    print('here is your current check account balance:')
    print(checkAccount)

checkAcountBlance()