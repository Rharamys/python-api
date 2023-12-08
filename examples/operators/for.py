string = "this is a string"

for letter in string:
    if letter in ['a','e','i','o','u']:
        break
    print(letter)

print("--------------")

for letter in string:
    if letter in ['a','e','i','o','u']:
        continue
    print(letter)

print("--------------")

for num in range(5,11):
    print(num)

print("--------------")

numbers = [10, 4.5, 7.6, 9, 4]
quantity = len(numbers)
total = 0
for number in numbers:
    total += number
print(f'mean is {round(total/quantity, 2)}')
