"""
Exercise 1 — Sum

Given:

numbers = [10, 20, 30, 40, 50]

Calculate the sum using a loop.

Expected:

150

Don't use sum() yet.
"""


numbers = [10, 20, 30, 40, 50]

sumOfAll = 0
for number in numbers:
    sumOfAll = number + sumOfAll

print(f"Sum of all the given numbers is: {sumOfAll}")


"""
Exercise 2 — Find maximum

Given:

numbers = [12, 45, 7, 89, 23, 56]

Find the largest number without using max().

Expected:

89

This is a very important DSA-style problem.
"""

numbers = [12, 45, 7, 89, 23, 56]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print(f"The largest number is: {largest_number}")


"""
Exercise 3 — Count even numbers

Given:

numbers = [1, 4, 7, 10, 13, 16, 20]

Count how many are even.

Expected:

4
"""


numbers = [1, 4, 7, 10, 13, 16, 20]

evenNoCount = 0

for number in numbers:
    if number % 2 == 0:
        evenNoCount += 1

print(f"Total number of even numbers are: {evenNoCount}")

"""
Exercise 4 — Reverse

Given:

numbers = [1, 2, 3, 4, 5]

Create a new list containing:

[5, 4, 3, 2, 1]

Try doing it without using .reverse().
"""

numbers = [1, 2, 3, 4, 5]


numbers_reversed = []

for i in range(len(numbers) - 1, -1, -1):
    numbers_reversed.append(numbers[i])

print(f"The reversed numbers are: {numbers_reversed}")

"""
Exercise 5 — Search

Given:

servers = ["web01", "web02", "db01", "cache01"]

Ask the user for a server name.

Print:
    Server found

or:
    Server not found

"""

servers = ["web01", "web02", "db01", "cache01"]

userInput = input("Enter the servername: ")

serverFound = False

for server in servers:
    if userInput == server:
        serverFound = True
        break

if serverFound:
    print("Server found")
else:
    print("Server not found")

"""
Exercise 6 — ⭐ Challenge

Given:

numbers = [10, 20, 10, 30, 20, 40, 10]

Count how many times 10 appears.

Expected:

3

Don't use .count().
"""

numbers = [10, 20, 10, 30, 20, 40, 10]

totalCount=0

for number in numbers:
    if(number==10):
        totalCount+=1

print(f"Total number of 10 in the given list is: {totalCount}")
