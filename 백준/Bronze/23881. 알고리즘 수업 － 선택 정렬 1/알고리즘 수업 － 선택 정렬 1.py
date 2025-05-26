import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

def selection(arr):
    max_num =0
    cnt = 0
    for i in range(n-1,0,-1):     # N downto 2
        last = i
        max_num = arr[i]
        for j in range(i):
            if arr[j] > arr[last] :  # 가장 큰 수 idx
                last,max_num = j, arr[j]
        if last!=i:     # idx 다르면 교환
            cnt += 1
            arr[i],arr[last] = arr[last],arr[i]
        if cnt == k :
            print(arr[last],arr[i])
            sys.exit(0)     #교환 횟수 k 달성 시 종료
    print(-1)
    return 0

selection(arr)

## 함수 내에서 for 를 실행하면 제어변수가 local로 지정돼서 더 빠르다
## 그냥 for 를 실행하면 제어변수가 global 이 돼서 느림. 그래서 계속 시간초과가 떴음.
