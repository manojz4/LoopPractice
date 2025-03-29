'''Multiplication table: Write a program that prints the multiplication 
table of any number provided by the user.
'''

store = int(input("Enter a number  : "))
for i in range(1,11):
    print(store, "x", i, "=", store*i)