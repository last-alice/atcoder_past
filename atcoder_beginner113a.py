list1 = [int(a) for a in input().split()]
list1_0 = list1[0] #A駅B駅のX
list1_1 = list1[1] #B駅C駅のY

print(list1_0 + (list1_1 // 2))