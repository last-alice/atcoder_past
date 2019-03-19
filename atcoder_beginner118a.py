list1 = [int(a) for a in input().split()]
list1_0 = list1[0] #A
list1_1 = list1[1] #B

if (list1_1 % list1_0) == 0:
    print(list1_0 + list1_1)
else:
    print(list1_1 - list1_0)
