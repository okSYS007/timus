#  |a|b|c|d|e|f|g|h|
# 1| | | | | | | | |
# 2| | | | | | | | |
# 3| | | | | | | | |
# 4| | | |x| | | | |
# 5| | | | | | | | |
# 6| | | | | | | | |
# 7| | | | | | | | |
# 8| | | | | | | | |

N = int(input())
_st1 = input()
_st2 = input()
_st3 = input()

N = 3

verbs_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nums = [int(x)+1 for x in range(8)]

# _st1 = 'a1'
# _st2 = 'd4'
# _st3 = 'g6'

res = 0

for i in range(N):

    verb = _st1[i]
    num = int(i[1])+1
    #индескы
    #0
    dot_x = verbs_.index(verb)+1
    dot_y = nums.index(num)

    if dot_x == 1 or dot_x == 8:
        res += 1
    if dot_y == 1 or dot_y == 8:
        res += 1

    if dot_x <= 6 and dot_x >= 3:
        if dot_x > 2 and dot_x < 5:
            res += 4
        else:
            res += 3*2
    if dot_y <= 6 and dot_y >= 3:
        if dot_y > 2 and dot_y < 5:
            res += 4
        else:
            res += 3*2

    print(res)        

