from collections import namedtuple

# declaring namedtuple
Student = namedtuple(
    'Student',
    ['name', 'age', 'DOB']
)

# adding values
S = Student('Victor Nice', '19', '2345556')

# access using index
print("The student age using index is : ", end="")
print(S[1])

# # access by keyword
print("The student name using keyname is : ", end="")
print(S.name)

# access using getattr()
