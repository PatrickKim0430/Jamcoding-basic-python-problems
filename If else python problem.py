# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/31
# Problem: if, else statement practice problem 


n=int(input())
if n < 10 :
    for i in range(n):
        print('Paa~')
else :
    for i in range(9):
        print("Paa~")
    print("Yee~")
    for i in range(n-10):
        print("Paa~")
