n = int(input())
sum = []
num = []

for i in range(n):
  num.append(list(map(int, input().split())))
  sum.append(num[i][0] + num[i][1])

for t in range(n):
  print(f"Case #{t+1}: {num[t][0]} + {num[t][1]} = {sum[t]}")