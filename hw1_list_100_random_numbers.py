import random

# Create a list of 100 random numbers between 0 and 1000
numbers = [random.randint(0, 1000) for _ in range(100)]

# Sort the list from min to max without using sort()
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap numbers[j] and numbers[j + 1]
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Print the sorted list
print("Sorted List from min to max without using sort():")
print(numbers)

# Initialize variables to keep track of sums and counts for even and odd numbers
sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0

# Iterate through the sorted list to calculate the sum and count for even and odd numbers
for num in numbers:
    if num % 2 == 0:
        # If the number is even, add it to the sum of even numbers and increment the count of even numbers
        sum_even += num
        count_even += 1
    else:
        # If the number is odd, add it to the sum of odd numbers and increment the count of odd numbers
        sum_odd += num
        count_odd += 1

# Calculate the average of even and odd numbers
average_even = sum_even / count_even if count_even > 0 else 0
average_odd = sum_odd / count_odd if count_odd > 0 else 0

# Print the averages
print(f"Average of even numbers: {average_even}")
print(f"Average of odd numbers: {average_odd}")