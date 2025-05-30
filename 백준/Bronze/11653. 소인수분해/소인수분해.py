num = int(input())

i=2
while i < num+1 :
  if num % i == 0:
    print(i)
    num = num/i
    i = 1
  i += 1