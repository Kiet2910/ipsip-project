##Symmetric Difference
#Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
a,b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')

##Set .add()
#pick the stamps one by one from a stack of  country stamps. Find the total number of distinct country stamps.
print(len(set([str(input()) for x in range(int(input()))])))

##Set .symmetric_difference() Operation
#You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.
n,s1=int(input()),set(map(int,input().split()))
b,s2=int(input()),set(map(int,input().split()))
print(len((s1.difference(s2)).union(s2.difference(s1))))


##Set Mutations
#given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set. Your task is to execute those operations and print the sum of elements from set A.
if __name__ == '__main__':
    (_, A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)

    print (sum(A))

##Check Subset
#Task: given two sets, A and B. Your job is to find whether set A is a subset of set B.
for i in range(int(input())):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    print(a.issubset(b))

##Check Strict Superset
#Task: given a set  and  other sets. Your job is to find whether set A is a strict superset of each of the N sets.
#Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
#A strict superset has at least one element that does not exist in its subset.
a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))

##
