import pandas

# List comprehension:
# squaring numbers:
numbers = [1, 18, 24, 3, 45, 68, 4, 5, 6, 78, 9878, 6464]
print([n ** 2 for n in numbers])

# filtering even numbers:
print([n for n in numbers if n % 2 == 0])

student_list = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Dictionary Comprehension:
new_dict = {key: value for (key, value) in student_list.items()}
print(new_dict)

# Looping with pandas DataFrame:
student_data_frame = pandas.DataFrame(student_list)

for (index, row) in student_data_frame.iterrows():
    print(row.score)