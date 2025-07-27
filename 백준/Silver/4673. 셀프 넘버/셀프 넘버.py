import sys
input = sys.stdin.readline

arr = [i for i in range(10000)]

for i in range(10000):
    tmp = 0
    tmp += i
    for j in range(len(str(i))):
        tmp += int(str(i)[j])
    if tmp < 10000:
        arr[tmp] = 0

for i in sorted(set(arr))[1:]:
    print(i)