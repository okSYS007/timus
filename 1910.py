n = int(input())
sp = list(map(int, (input().split())))
ind = 0
MAX = sum(sp[:2])
for i in range(n - 2):
    if  sum(sp[i:i+3]) > MAX:
        MAX = sum(sp[i:i+3])
        ind = sp.index(sp[i]) + 2

print(MAX, ind)