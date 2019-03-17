#If-Else
n = int(raw_input())
if (n%2 == 1):
    print("Weird")
elif 1 < n < 6:
    print("Not Weird")
elif 6 < n < 21:
    print("Weird")
else:
    print("Not Weird")
#Arithmetic Operators
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a + b)
    print(a - b)
    print(a * b)
#Python: Division
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    c = a/b
    print("%d" % c)
    print("%f" % c)
#Loops
if __name__ == '__main__':
    n = int(raw_input())
    i = 0
    while i < n:
        print i**2
        i += 1
#Funtion and print Function
def is_leap(year):

    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

for x in range(1,n+1):
    print(x, end='')
