"""This program check if two lovers are compatible using their names"""

print("Welcome to your beloved lover's compatible calculator\n")

# Ask for the lovers' names:
first_name = input("Enter the first person name\n")
second_name = input("\nEnter the second person name\n")

# concatenate theirs name together and make it case insentitive:
joint_name = " ".join([first_name, second_name]).lower()

# count the occurences of t, r, u, e,. l, o, and v in this concatenated string
t_count = joint_name.count("t")
r_count = joint_name.count("r")
u_count = joint_name.count("u")
e_count = joint_name.count("e")
l_count = joint_name.count("l")
o_count = joint_name.count("o")
v_count = joint_name.count("v")

# add the sum of counts of t, r, u and e
sum_of_true = t_count + r_count + u_count + e_count
# add the sum of counts of l, o, v and e
sum_of_love = l_count + o_count + v_count + e_count

# concatenate the sum of 'true' and 'love in the order as of 'true love':
concatenated_sum = int(str(sum_of_true) + str(sum_of_love))

# check this concatenated score againt given conditions and print your desire statement:
if concatenated_sum < 10 | concatenated_sum > 90:
    print(f"\nYour score is {concatenated_sum}. You go together like coke and mentos")
elif concatenated_sum >= 40 & concatenated_sum <= 50:
    print(f"\nYour score is {concatenated_sum}. You are alright together")
else:
    print(f"\nYour score is {concatenated_sum}")