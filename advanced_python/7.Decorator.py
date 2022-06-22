#function treated as object -assigned a function to a variable
def add(a,b):
    return a+b
func =add

print(add(1,5))


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)

greet(shout)
greet(whisper)





def div(a,b):
    print(a/b)


def smart(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div = smart(div)
div(4,2)

#returns a function
def print_msg(arg):
    message = "Hello man"
    def printer():
        print("yor are super",arg)
    return printer

printfunc = print_msg('helllllddd')
printfunc()

#decorator. It helps to add some thing to original function printer without touching it
def printer():
    print("hello bro")
def display_function(func):
    def inner():
        print("inner func")
        func()
        print("end of func")
    return inner

funct = display_function(printer)
funct()













def swapfunc(func):
    def inner(a,b):
        print("swapping")
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
@swapfunc
def divide(a,b):
    print(a/b)
divide(3,9)
