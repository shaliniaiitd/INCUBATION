# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)


greet(shout)
greet(whisper)


# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x + y

    return adder

print(create_adder(15)(10))
add_15 = create_adder(15)

print(add_15(10))


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1(*args, **kwargs):
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func(*args,**kwargs)

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used(args):
    print("This is inside the function created by !!", args)


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
inner1 = hello_decorator(function_to_be_used)

# calling the function
inner1("Shalini")

@hello_decorator
def new_func(x):
    print("Printing x:",x)

new_func("shalini")

@hello_decorator
def func_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

inpt = {"one": 1, "two": 2}

func_kwargs(**inpt)

@hello_decorator
def func_args(*args):
    for arg in args:
        print(arg)

lst = ["variable", "number", "of", "parameters"]

func_args(*lst)