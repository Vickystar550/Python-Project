def hello_function():
    def say_hi():
        return "Hi"
    return say_hi

print("\n")
print(hello_function()())


def print_message(message):
    "Enclosing Function"
    def message_sender():
        "Nested Function"
        print(message)
    
    message_sender()

print("\n")    
print_message("Some random message")


# ----- Creating Decorators:
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    
    return wrapper

def say_hi():
    return "hello there"

# -- traditional way of calling a decorator function:
decorate = uppercase_decorator(say_hi)
print(decorate())

# --- amateur ways:
@uppercase_decorator
def say_hi():
    return 'hello there'

print("\n")
print(say_hi())

#____Applying mulitple decorators to a single variables
import functools
def split_string(function):
    @functools.wraps(function)
    def wrapper():
        return function().split()
    
    return wrapper

@split_string
@uppercase_decorator
def say_so():
    return "somebody is looking up and down"

print("\n")
print(say_so())

#----- Accepting argument in Decorator Functions

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1, arg2))
        function(arg1, arg2)
    
    return wrapper_accepting_arguments

@decorator_with_arguments
def cities(city_one, city_two):
    print("cities i love are {0}, {1}".format(city_one, city_two))
    

print("\n")
print(cities("Nairobi", "Accra"))


# Defining General Purpose Decorators:
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("The positional arguments are:", args)
        print("The keyword arguments are:", kwargs)
        function_to_decorate(*args)
    
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

print("\n")    
function_with_no_argument()


print("\n")
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)
    
function_with_arguments(1, 2, 3, job="Data Scientist")


@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")


print("\n")
function_with_keyword_arguments(first_name="Victor", last_name="Nice")


# Passing Arguments to the Decorator:
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(function_arg1, function_arg2, function_arg3):
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2, decorator_arg3,
                          function_arg1, function_arg2, function_arg3))
            return func(function_arg1, function_arg2, function_arg3)
        
        return wrapper
    
    return decorator

pandas = "Pandas"

@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
    "This is the decorated function with arguments"
    print("This is the decorated function and it only knows about its arguments:"
          " {0} {1} {2}".format(function_arg1, function_arg2, function_arg3))


print("\n")
decorated_function_with_arguments(pandas, "science", "tools")


# Debugging Decorators:
print("\n")
print(decorated_function_with_arguments.__name__)

print(decorated_function_with_arguments.__doc__)