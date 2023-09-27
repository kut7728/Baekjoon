word = input()
word.upper()
count = {}

for i in word:
  try:
    count[i] += 1
  except:
    count[i] = 1

max(count.values())