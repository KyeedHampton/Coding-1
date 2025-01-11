# Question 1
frozen_food = ["Ice Cream", "Frozen Pizza", "Frozen Vegetables", "Fish Sticks", "Frozen Fries"]
international_food = ["Soy Sauce", "Tortilla", "Curry Powder", "Ramen Noodles", "Tikka Masala Sauce"]
produce = ["Apples", "Bananas", "Carrots", "Lettuce", "Tomatoes"]

# Question 2
numbers = [1, 30, 39, 50, 293, 100]

print("Number at index 0:", numbers[0]) 
print("Number at index 3:", numbers[3]) 
print("Number at index 4:", numbers[4]) 

# Question 3
def multiply_index_4(factor):
    result = numbers[4] * factor
    return result


print("Result of multiplying number at index 4 by 2:", multiply_index_4(2))