T = int(input())
answers = []
for i in range(T):
    n = int(input())
    n2 = n ** 2
    counter = 0
    for j in range(1, n2):
        for k in range(1, j):
            if (j ** 2) + (k ** 2) == n2:
                counter += 1
    answers.append(counter)

for answer in answers:
    print(answer)

# answers = []
#
# for i in range(T):
#     n, m, s, t = map(int, input().split())
#     flag = False
#     for j in range(m):
#         u, v = map(int, input().split())
#         if v == s:
#             answers.append(j)
#             flag = True
#     if not flag: answers.append(-1)
# for i in answers:
#     print(i)
