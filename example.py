n, m = map(int, input().split())
bask = list(range(1,n+1))

for _ in range(m):
  i, j = map(int, input().split())
  temp = bask[i-1:j]
  temp.reverse()
  bask[i-1:j] = temp

for q in bask:
  print(q, end=" ")