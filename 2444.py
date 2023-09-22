n = int(input())
full = 2*n-1

for i in range(1, full+1):
  print(' '*abs(n-i)+'*'*((full)-2*abs(n-i)))