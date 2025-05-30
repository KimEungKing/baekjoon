n = int(input())
lst = [input() for _ in range(n)]
lst = list(set(lst))
lst.sort(key=lambda x: (len(x),x))

for l in lst:
    print(l)