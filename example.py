a = list(map(int, input().split()))
b = list(set(a))

if len(b) == 1:
  print(10000+b[0]*1000)

elif len(b) == 2:
  for i in b:
    if a.count(i) == 2:
      print(1000+i*100)
    else:
      continue


elif len(b) == 3:
  print(max(b)*100)
