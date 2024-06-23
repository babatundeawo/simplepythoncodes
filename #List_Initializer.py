import random

# Initialize a list of 5 random integers
random_list = [random.randint(1,100) for i in range(5)]
print(f"Initial List: {random_list}")

# Append a new integer to the list
new_integer = random.randint(1, 100)
random_list.append(new_integer)
print(f"List after appending {new_integer}: {random_list}")

# Sort the list in ascending order
random_list.sort()
print(f"List after sorting: {random_list}")

# Reverse the list
random_list.reverse()
print(f"List after reversing: {random_list}")

