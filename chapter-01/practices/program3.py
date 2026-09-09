# take 2 numbers from the user and print their sum
# find sum, difference, product, quotient and remainder of 2 numbers
# also find the average of 2 numbers
# also find the greater number among the 2 numbers

# get 2 numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# calculate sum, difference, product, quotient and remainder
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
remainder = num1 % num2

# calculate average
average = sum_result / 2

# find the greater number
if num1 > num2:
    greater = num1
else:
    greater = num2


# print the results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Remainder:", remainder)
print("Average:", average)
print("Greater number:", greater)