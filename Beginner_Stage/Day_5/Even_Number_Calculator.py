""" This program calculates this sum of even number from 1 to 100 """

sum_num = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_num += i
print(sum_num)
