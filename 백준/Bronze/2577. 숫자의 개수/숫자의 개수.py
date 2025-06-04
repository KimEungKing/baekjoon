import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
abc = str(a*b*c)
arr = [0]*10

for i in range(len(abc)):
    arr[int(abc[i])] += 1
    
for i in arr:
    print(i)