# handling exceptions
try:
    print(x)
except NameError as e:
    print(e)
    print('Oops, NameError here!')
except Exception as e:
    print(e)
    print('Oops, please try again')
else: 
    print('Executing this after no exceptions')
finally:
    print('Executing this after the process, that can have exceptions or not')

# raising exceptions
def double(n):
    if n <= 0:
        raise Exception('Value must be greater than 0')
    return n * 2

print(double(0))

# custom exceptions
class CustomException(Exception):
    # just inherit the Exception class but dont implement nothing new (pass)
    pass