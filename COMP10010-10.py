# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n - 1)

# n = int(input("n: "))
# print(sum(n))

# scores = []
# choice = None
# while choice != "0":
#     print(
#         """
# High Scores

# 0-exit
# 1-show scores
# 2-add a score
# 3-remove a score
# 4-sort a score
# """
#     )
#     choice = input("Choice: ")
#     if choice == "0":
#         print("Good-byeee")
#     if choice == "1":
#         print("High Scoers")
#         for i in scores:
#             print(i, end = " ")
#     if choice == "2":
#         score = int(input("What score did u get? "))
#         scores.append(score)
#     if choice == "3":
#         score = int(input("Which score to remove? "))
#         if score in scores:
#             scores.remove(score)
#         else:
#             print(f"{score} is not in the list of high scores")
#     if choice == "4":
#         scores.sort(reverse=True)



# print("Here's your random sequence")
# print(seq_num)
# sorted_seq_num = []
# for i in range(0, n):
#     maxv = 0
#     maxp = -1
#     for j in range(0, len(seq_num)):
#         if(seq_num[j]> maxv):
#             maxv = seq_num[j]
#             maxp = j
#     sorted_seq_num += seq_num[maxp],
#     del seq_num[maxp]

# print(sorted_seq_num)

import random

n = int(input("n: "))

seq_num = []
for i in range(0, n):
    seq_num += random.randrange(0, 100),

print(seq_num)

for i in range(0, n):
    for j in range(0, n - 1 - i):
        if seq_num[j] < seq_num[j + 1]:
            seq_num[j], seq_num[j + 1] = seq_num[j + 1], seq_num[j]
print(seq_num)