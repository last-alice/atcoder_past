list1 = [int(a) for a in input().split()]
m_a = list1[0] #a
m_b = list1[1] #b
m_c = list1[2] #c
m_d = list1[3] #d

if abs(m_a - m_c) <= m_d:
    print("Yes")
elif abs(m_b - m_c) <= m_d and abs(m_b - m_a) <= m_d:
    print("Yes")
else:
    print("No")