# Function to reverse a word
def reverse_word(word):
    return word[::-1]


print(reverse_word("pet"))
print(reverse_word("book")) 

# Function to get state landmarks
def state_landmark(state):
    state = state.lower() 
    if state == "pennsylvania":
        return "A landmark in Pennsylvania is the Liberty Bell."
    elif state == "new york":
        return "A landmark in New York is the Statue of Liberty."
    elif state == "california":
        return "A landmark in California is the Hollywood Walk of Fame."
    elif state == "texas":
        return "A landmark in Texas is the Alamo."
    else:
        return "The state could not be found."



print(state_landmark("South Carolina"))
print(state_landmark("California")) 