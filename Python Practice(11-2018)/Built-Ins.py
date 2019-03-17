##Zipped
#This function returns a list of tuples. The th tuple contains the th element from each of the argument sequences or iterables.
#If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.

#Task: compute the average scores of each student.
n, x = map(int, input().split())

sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) )

for i in zip(*sheet):
    print( sum(i)/len(i) )

##Input()
#Task: You are given a polynomial P of a single indeterminate (or variable), x.You are also given the values of x and k. Your task is to verify if P(x)=k .
x,k = map(int,raw_input().split())
print input()==k

##Python Evaluation
#Task given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var).
eval(input())
##Athlete Sort
#The first line contains N and M separated by a space.
# The next N lines each contain M elements.
#The last line contains K.
N,M = map(int,raw_input().split())
lines = []
for i in xrange(N):
    lines.append(map(int,raw_input().split()))
K = int(raw_input())
lines = sorted(lines,key = lambda x: x[K])
for line in lines:
    print ' '.join(str(k) for k in line)
##Any or all
#Task:You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
def is_pal(n):
    S=str(n)
    return all((s==t for s,t in zip(S,reversed(S))))
def meets_conditions(L):
    if not all((l>0 for l in L)):
        return False
    return bool(any((is_pal(l) for l in L)))

N=int(raw_input())
L=map(int, raw_input().split())
print meets_conditions(L)
##Sorting
#Task: sort out a single line of input contains the string S.
S = input()


print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
