stud = ['False'] * 30

for i in range(28):
  num = int(input())
  stud[num-1] = 'True'

target = list(filter(lambda x: stud[x] == 'False', range(30)))

print(min(target)+1)
print(max(target)+1)