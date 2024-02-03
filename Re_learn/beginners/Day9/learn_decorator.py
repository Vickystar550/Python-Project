def plus_one(number):
    return number + 1


def function_call(function):
    number_to_add = 5
    return function(number_to_add)


print(function_call(plus_one))


# ------------------
def hello_function():
    def say_hi():
        return "Hi"

    return say_hi


hello = hello_function()

print(hello())


# -------------------
def print_message(message):
    "Enclosing Function"

    def message_sender():
        "Nested Function"
        print(message)

    message_sender()


print_message("Some random message")


# ----------- Creating Decorators:
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    return "hello there"


print(say_hi())

import functools


def split_string(function):
    @functools.wraps(function)
    def wrapper():
        return function().split()

    return wrapper


@split_string
@uppercase_decorator
def say_hi():
    return "Hello There"


print(say_hi())


# ----------------
# Accepting arguments in decorator:

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {}, {}".format(arg1, arg2))
        function(arg1, arg2)

    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {} and {}".format(city_one, city_two))


cities("Nairobi", "Accra")


# Defining General Purpose Decorators:
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("The positional arguments are:", args)
        print("The keywords argumnets are:", kwargs)
        function_to_decorate(*args)

    return wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No argument here.")


function_with_no_argument()


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)


@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")


function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")


# -------------------------
# Passing arguments to the decorator:
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
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
    print("This is the decorated function and it only knows about its arguments: {0}"
          " {1}" " {2}".format(function_arg1, function_arg2, function_arg3))


decorated_function_with_arguments(pandas, "Science", "Tools")
