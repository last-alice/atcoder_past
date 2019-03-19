list1 = [int(a) for a in input().split()]
list1_0 = list1[0] #A
list1_1 = list1[1] #B

abc_0 = list1_0 * list1_1 * 1
abc_1 = list1_0 * list1_1 * 2
abc_2 = list1_0 * list1_1 * 3

if abc_0 in [3, 9, 15, 21, 27]:
    print("Yes")
elif abc_1 in [3, 9, 15, 21, 27]:
    print("Yes")
elif abc_2 in [3, 9, 15, 21, 27]:
    print("Yes")
else:
    print("No")