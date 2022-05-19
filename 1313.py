#110100100010000
#В первой строке находится целое число N (1 ≤ N ≤ 65535). 
# В i-й из N последующих строк записано целое число Ki — номер позиции в последовательности (1 ≤ Ki ≤ 231 − 1).

firstStr = input()
my_str = ''
for st in range(int(firstStr)):
    my_str = ''.join(str(input() + ' '))

print(my_str)


num = int(input())
arr = []
for i in range(num):
    temp_arr = input().split(' ')
    arr.append(temp_arr)
string = ''
for i in range(num):
        k = i
        j = 0
        while k >= 0:
                string += (arr[k][j] + ' ')
                k -= 1
                j += 1
for i in range(1,num,1):
        k = num - 1
        j = i
        while j != num:
                string += (arr[k][j] + ' ')
                k -= 1
                j += 1
print(string)