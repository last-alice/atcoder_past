list1 = [int(a) for a in input().split()]
list1_0 = list1[0] #AB
list1_1 = list1[1] #BC
list1_2 = list1[2] #CA

if (list1_0 * list1_1 // 2) > 1:
    print(list1_0 * list1_1 // 2)
else:
    print(list1)