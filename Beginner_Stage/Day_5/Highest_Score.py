"""Compute the highest score from various scores"""

# Note: Not allow to used min() or max() function

scores = input("Enter scores. Separated by space\n").split()

# Setting the highest score to be the first element of scores:
high_score = float(scores[0])

# Looping through scores to compare other element values:
for score in scores:
    if float(score) > high_score:
        high_score = float(score)

print(f"The highest score is: {high_score}")
