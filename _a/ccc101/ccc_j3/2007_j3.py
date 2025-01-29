briefcase_values = {
1 : 100,
2 : 500,
3 : 1000,
4 : 5000,
5 : 10000,
6 : 25000,
7 : 50000,
8 : 100000,
9 : 500000,
10 : 1000000}
sum_of_briefcase_values = sum(briefcase_values.values())

briefcases_eliminated = int(input())
for _ in range(briefcases_eliminated):
    sum_of_briefcase_values -= briefcase_values[int(input())]
bankers_offer = int(input())

if bankers_offer > sum_of_briefcase_values / (len(briefcase_values) - briefcases_eliminated):
    print("deal")
else:
    print("no deal")