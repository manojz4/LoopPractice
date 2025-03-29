'''Sum of n numbers: Write a program that calculates the sum of all numbers from 1 to n, where 
n is provided by the user.'
'''

n = int(input("Enter a number : "))
summ = 0
for i in range(1,n +1):
    summ +=i
print(summ)
'''
Enter a number : 5
15
'''