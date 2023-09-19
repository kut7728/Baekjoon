left = []

for _ in range(10):
  left.append(int(input())%42)

leftset = list(set(left))
print(len(leftset))