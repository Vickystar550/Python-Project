# Enter your code here. Read input from STDIN. Print output to STDOUT

n_m_input = input().split()


group_A = []
group_B = []

for _ in range(int(n_m_input[0])):
    group_A.append(input())

for _ in range(int(n_m_input[-1])):
    group_B.append(input())

index_list = []

for item in group_B:
    if item in group_A:
        indices = [j+1 for j in range(len(group_A)) if group_A[j] == item ]
        index_list.append(indices)
    else:
        index_list.append([-1])

print("\n")
for _ in index_list:
    print(*_)

