list1 = [int(a) for a in input().split()]
list1_0 = list1[0] #N
list1_1 = list1[1] #K

if list1_0 % list1_1 == 0:
    print(0)
else:
    print(1)