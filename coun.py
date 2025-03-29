# Program to count the number of vowels in a string

# Taking input from the user
text = input("Enter a string: ")

# Initializing a variable to store the count of vowels
vowel_count = 0

# Defining a set of vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Using a for loop to check each character in the string
for char in text:
    if char in vowels:
        vowel_count += 1

# Displaying the result
print("Number of vowels:", vowel_count)

