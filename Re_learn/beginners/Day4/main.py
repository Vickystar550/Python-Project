import random

print(random.randint(1, 100))

sequence = [random.randint(0, i) for i in range(10)]

print("Before shuffling", sequence)

random.shuffle(sequence)

print("After Shuffling", sequence)

a = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

for i in range(5):
    print(random.choice(a))

for _ in range(10):
    b = random.sample(a, 2)
    print("random sample", b)


##############

random.seed(12)

print("generating a random sequence of five numbers")

print([random.randint(12, 100) for e in range(5)])

random.seed(12)

print([random.randint(12, 100) for e in range(5)])