list1 = [int(a) for a in input().split()]
list1_0 = list1[0] #A1
list1_1 = list1[1] #A2
list1_2 = list1[2] #A3

list2 = [list1_0, list1_1, list1_2]
list2.sort()
b = max(list2) - list2[1]
c = list2[1] - min(list2)
print(b + c)