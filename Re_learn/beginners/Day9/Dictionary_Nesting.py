student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectation"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

print("\n")
x = ("Apple", "Beans", "Straw Berry")
for i, j in enumerate(student_scores, 1):
    print(i, j)

print("\n")
for i, j in enumerate(student_scores):
    print(i, j)

# ----------------
travel_log = []


def add_new_country(country, visits, list_of_cities):
    travel_log.append({"country": country, "visits": visits, "cities": list_of_cities})


add_new_country("Nigeria", 5, ["Rivers", "Edo", "ABJ", "Kano", "Delta"])
print(travel_log)