# Create a list of 10 numbers.
# 2. Print the first, last, and middle number.
# 3. Add a new number to the end of the list.
# 4. Replace the third number with 99.
# 5. Loop through the list and print only the even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

print(numbers[0], numbers[4], numbers[9])

numbers.append(11)
print(numbers)

numbers.pop(2)
numbers.insert(2, 99)
print(numbers)

for i in range(len(numbers)):
    
