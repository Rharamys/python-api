while True:
    print('Printing TRUE')
    break

x = 0

while x < 10:
    print(f'''Value of x is {x}''')
    x+=1

text = None
number = 4
print('*** Provide the right number ***')
print("Type 'exit' to finish process")
print('********************************')
while True:
    if text == None:
        text = input('''Provide a number between 0 and 10: ''')
    else:
        text = input()

    if text == 'exit':
        break
    elif int(text) == number:
        print("Congratulations! You provided the right answer!")
        break
    else:
        print(f"Oops, it's another number. Please provide another number. Provided {text}")


print('Game finished')
