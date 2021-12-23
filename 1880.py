
N_first = int(input())
first_list = []
sec_list = []
thrid_list = []

#for i in range(N_first):
my_str = input()
first_list = my_str.split()

N_sec = int(input())
    
#for i in range(N_sec):
my_str = input()
sec_list = my_str.split()

N_third = int(input())

#for i in range(N_third):
my_str = input()
thrid_list = my_str.split()

c = list(set(first_list) & set(sec_list) & set(thrid_list))

print(len(c))