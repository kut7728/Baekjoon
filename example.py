n = int(input())
num = str(input())
result = 0

for _ in range(n):
  result += int(num[_])

print(result)