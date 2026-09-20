"""
Challenge 1 — Second largest

Given:

numbers = [10, 50, 20, 40, 30]

Find:

40

without using:

sort()
sorted()
max()

Try to solve it with a loop.
"""

numbers = [10, 50, 20, 40, 30, -80, 400, 400]

largest = None
second_largest = None


for number in numbers:
    if largest is None:
        largest = number

    elif number > largest:
        second_largest = largest
        largest = number

    elif number < largest and (second_largest is None or number > second_largest):
        second_largest = number


print(second_largest)
print(largest)


"""
Challenge 2 — Remove duplicates manually

Given:

numbers = [1, 2, 2, 3, 4, 4, 5]

Create:

[1, 2, 3, 4, 5]

Don't use set() yet.

Hint: you'll need to think about:

if item not in ...

Extra:  Sorted the new list 
"""

numbers = [1, 2, 2, 3, 4, 4, 5, 2, 4, 3, 10, 10, 0, -1]

non_duplicate_numbers = []

for number in numbers:
    if number not in non_duplicate_numbers:
        non_duplicate_numbers.append(number)

# non_duplicate_numbers.sort()


for i in range(len(non_duplicate_numbers)):
    for j in range(len(non_duplicate_numbers) -i - 1):
        if non_duplicate_numbers[j] > non_duplicate_numbers[j + 1]:
            non_duplicate_numbers[j], non_duplicate_numbers[j + 1] = (
                non_duplicate_numbers[j + 1],
                non_duplicate_numbers[j],
            )


print(non_duplicate_numbers)


"""
Challenge 3 — Count positive, negative and zero

Given:

numbers = [10, -5, 0, 7, -3, 0, 8, -1]

Produce:

Positive: 3
Negative: 3
Zero: 2

Try to do it with one loop.
"""


numbers = [10, -5, 0, 7, -3, 0, 8, -1]

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    elif number == 0:
        zero_count += 1

print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")
print(f"Zeor: {zero_count}")
