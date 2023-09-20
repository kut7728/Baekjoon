T = int(input())
a=[]

for _ in range(T):
  R, S = input().split()
  b = str()
  for i in range(len(S)):
    b += S[i]*int(R)
  a.append(b)

for t in range(T):
  print(a[t])