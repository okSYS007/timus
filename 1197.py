p =[
    [2,3,4,4,4,4,3,2],
    [3,4,6,6,6,6,4,3],
    [4,6,8,8,8,8,6,4],
    [4,6,8,8,8,8,6,4],
    [4,6,8,8,8,8,6,4],
    [4,6,8,8,8,8,6,4],
    [3,4,6,6,6,6,4,3],
    [2,3,4,4,4,4,3,2]
    ]

verbs_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nums = [int(x)+1 for x in range(8)]

N = int(input())
res = []
for i in range(N):

    _str1 = input()
    x = _str1[0]
    y = int(_str1[1])
    dot_x = verbs_.index(x)
    dot_y = nums.index(y)
    
    res.append(p[dot_x][dot_y])
    

for i in res:
    print(i)

     

