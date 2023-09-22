new = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))
need = []

for i in range(6):
  need.append(new[i] - found[i])

for t in need:
  print(t, end = " ")