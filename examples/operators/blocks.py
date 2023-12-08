var = 30

if var >= 0:
    # this is one block
    print("it's a positive value")
    new = var + 30
    if new >= 50:
        print('new is greater or equal than 50')
    else:
        print('new is lesser than 50')
    print(f'New value is {new}')
else:
    # this is another block
    print("it's a negative value")