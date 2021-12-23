N = int(input())
_res = 0

for i in range(N):
    _str = input()
    plus_one = _str.split('+')
    if len(plus_one) > 1:
        _res += 2
    else:
        _res +=1 

_res += 2
if _res == 13:
    _res+=1

print(_res*100)