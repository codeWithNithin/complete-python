# take amount and number of people from the user and calculate the amount each person has to pay
amount = float(input("Enter the total amount: "))
num_people = int(input("Enter the number of people: "))

# calculate the amount each person has to pay
amount_per_person = amount / num_people

# print the result
print(f"Each person has to pay: {amount_per_person}")