def addition_simplified(*args):
    print(type(args))
    return sum(args)

print(addition_simplified(3, 4, 5, 7, 9, 8))

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print(type(kwargs))
    
what_are_kwargs(2, 3, 4, 5, 6, 7, 8, job="Programming", school="Code", expected = "Distinction")