from collections import Counter

s = list(map(str,input().upper()))
res = Counter(s).most_common()

if len(res) > 1 and res[0][1] == res[1][1]:
    print('?')
else :
    print(res[0][0])