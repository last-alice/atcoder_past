list1 = [int(a) for a in input().split()]
list1_0 = list1[0] #A
list1_1 = list1[1] #B

if list1_0 > 8 or list1_1 > 8:
    print(":(")
else:
    print("Yay!")