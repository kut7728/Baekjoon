n, m = map(int, input().split())
bask = [0]*n

for i in range(n):
  bask[i] = i+1

for i in range(m):
  a, b = map(int, input().split())
  temp = bask[a-1]
  bask[a-1] = bask[b-1]
  bask[b-1] = temp

for i in range(n):
  print(bask[i],  end=" ")