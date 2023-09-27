word = input()
half = len(word)//2

if len(word)%2==True:
  if word[:half]==word[-1:-half-1:-1]:
    print("1")
  else:
    print("0")
else:
  if word[:half]==word[-1:-half-1:-1]:
    print("1")
  else:
    print("0")

