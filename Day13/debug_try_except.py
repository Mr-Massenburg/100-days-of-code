# Day 13 | Debugging Practice

# Fixed Code
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again with numerical response. (ie. 15)")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")

# Original Code
# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")
