import sys
input = sys.stdin.readline

def my_round(x):
    return int(x+0.5)

n = int(input())
if n == 0 :
    print(0)
    exit(0)

arr = [int(input()) for _ in range(n)]
arr.sort()
# 앞 뒤 15% 씩 잘라냄 
cut = my_round(n * 0.15)
arr = arr[cut:n-cut]

answer = sum(arr)/len(arr)
print(my_round(answer))