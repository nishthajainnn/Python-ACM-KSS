# 1)
m = int(input("Enter the beginning no.: "))
n = int(input("Enter the ending no.: "))
s = 0
for i in range(m, n+1):
    s += i
print("sum of no.s from m to n: ", s)

#2)
a = int(input("Enter the dividend: "))
b = int(input("Enter the divisor: "))
if a%b == 0:
    print("b perfectly divides a")
else:
    print("b does NOT perfectly divides a")

from math import pi 

#3)
d = int(input("Enter the diameter: "))
print("area of the circle", pi*((d/2)**2))
print("perimeter of the circle", 2*pi*(d/2))

#4)
n = int(input("Enter the number for its factorial: "))
f = 1
for i in range(1,n+1):
    f = f*i
print(f'factorial of the {n} is {f}')

#5)

for i in range(2,7):
    k = 1
    for j in range(1, i):
        print(k,end = '')
        k = k + 1
    print()

