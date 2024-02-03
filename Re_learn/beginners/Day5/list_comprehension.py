my_list = [1, 2 , 3, 4, 5, 6, 7, 8, 9]

print(["even" if x % 2 == 0 else "odd" for x in my_list])

squared_list = [x**2 for x in my_list]
print(squared_list)

# Multiple if/else list comprehension:
list_2 = [-3, 5, -5, 0, 3, 0]

categorized_list = ["Positive" if x > 0 else "Negative" if x < 0 else "Zero" for x in my_list]

# Nested List comprehension:
nested_list = [[1, 2, -3], [-4, 0, 3], [6, -7, 8]]

squared_matrix = [[x**2 if x > 0 else x for x in row] for row in nested_list]

print(squared_matrix)