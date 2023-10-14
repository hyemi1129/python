""" n = input()
print(n+"??!") """

""" n, m = map(int, input().split())
if n>m:
    print('>')
elif n<m:
    print('<')
elif n==m:
    print('==') """

""" n = int(input())
if n%400==0 or n%4==0 and n%100!=0:
    print(1)
else:
    print(0) """

n = int(input())
for i in range(1, 10):
    print(n, '*', i, '=', n*i)
