##Map and Lambda Function
#Task: A list on a single line containing the cubes of the first N fibonacci numbers.
cube = lambda x: pow(x,3)# complete the lambda function
def fibonacci(n):
     # return a list of fibonacci numbers
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis[0:n])
##Validating Email Addresses With a Filter
#Task: Output a list containing the valid email addresses in lexicographical order. If the list is empty, just output an empty list, [].
def check_valid(email):
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False

    if not username.replace("-", "").replace("_", "").isalnum():
         return False
    if not website.isalnum():
        return False
    if len(extension) < 1 or len(extension) > 3:
        return False
    return True

    n = int(input())
    emails = [input() for email in range(n)]

    valid = list(filter(check_valid, emails))
    print(sorted(valid))
##Reduce Funtion
#Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than 1.
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator
