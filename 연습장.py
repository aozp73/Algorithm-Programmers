from collections import defaultdict

dp1 = defaultdict(int)

dp1[1] = 2
print(dp1[1])
print(dp1[0])
print(dp1[3])

print('----------')

dp2 = defaultdict(set)

dp2[1].add(5)
dp2[1].add(5)
dp2[1].add(6)

print(dp2[1])
print(dp2[0])
print(dp2[3])

