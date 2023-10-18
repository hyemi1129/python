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

""" n = int(input())
for i in range(1, 10):
    print(n, '*', i, '=', n*i) """

""" t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(a+b) """

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i

print(sum)