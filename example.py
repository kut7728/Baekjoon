phone = [['a', 'b', 'c'],['d', 'e', 'f'],['g', 'h', 'i'],['j', 'k', 'l'],['m', 'n', 'o'],['p', 'q', 'r', 's'],['t', 'u', 'v'],['w', 'x', 'y', 'z']]

get = input().lower()
time = 0

for i in get:
  for j in range(8):
      try:
        phone[j].index(i)
        time += (j+3)
      except:
         continue
         
print(time)