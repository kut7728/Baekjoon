word = input()
word = word.upper()
count = {}

for i in word:
  try:
    count[i] += 1
  except:
    count[i] = 1

temp = [k for k, v in count.items() if v == max(count.values())]

if len(temp) == 1:
  output = temp[0]
else:
  output = '?'

print(output)