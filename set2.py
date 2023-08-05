#Problem *1: Print the following pattern*
#Write a program to print the following number pattern using a loop.
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
# Solution:-

n = 5  

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#Solution

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)
