n = int(input())

if n%4 != 0:
  print("다시 입력하시오")
else:
  print("long "*(n//4)+"int")