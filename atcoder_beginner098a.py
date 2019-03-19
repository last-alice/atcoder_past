list1 = [int(a) for a in input().split()]
list1_0 = list1[0] #A
list1_1 = list1[1] #B

plus = list1_0 + list1_1
minus = list1_0 - list1_1
mul = list1_0 * list1_1

max_ans = max(plus, minus, mul)

print(max_ans)