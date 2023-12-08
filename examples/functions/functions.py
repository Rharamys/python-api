# this will throw an error because the function has no instance yet
# hello_world()

def hello_world():
    print("Hello, World!")

hello_world()

def age_to_days():
    age = int(input("Provide your age: "))
    days = age * 365
    print(f"You've being alive for {days} days")

age_to_days()

list = [10,20]

def add_num():
    num = int(input("Provide a number: "))
    list.append(num)
    print(list)

add_num()

def add (x, y = 5):
    print(f"x->{x} | y->{y}")
    return x + y

# x will be 10 and y will be 2
result = add(10, 2)

# with this pylance will show error
# result = add(x=10, 2)

# but this can happen
result = add(10, y=2)

# x will be 2 and y will be 10
result = add(y=10, x=2)
print(result)

# x will be 2 and y will be 5
result = add(x=2)
print(result)


# x will be 2 and y will be 5
result = add(2)
print(result)

# *******************************************
# Arbitrary values
def args_function(*args):
    print(args)
    print(type(args))
    for arg in args:
        print(arg)
        print(type(arg))

args_function('Rharamys', "Bordini", 32, 2023, "Parameters")

def key_words_args_function(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'key->{key} | v->{value}')

key_words_args_function(name='Rharamys', lastname="Bordini", age=32, year=2023, param="Parameters")


# *******************************************
# Recursive functions
def factor(num):
    if(num == 1) :
        return num
    else:
        return num * factor(num-1)

print(factor(4))