n = int(input())
sum = []

for i in range(n):
  a, b = map(int, input().split())
  sum.append(a+b)

for t in range(n):
  print(f"Case #{t+1}: {sum[t]}")