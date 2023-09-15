n, m = map(int, input().split())
bask = [0]*n

for i in range(m):
  a, b, c = map(int, input().split())
  for t in range(a, b+1):
    bask[t-1] = c
    
      
  

for i in range(n):
  print(bask[i],  end=" ")