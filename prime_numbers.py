#program to find the prime numbers using Sieve of Eratosthenes
n = 100
# create numerical variables to symbolically represent deco values
plain = 0
circled = 1
crossed = 2

deco = [ plain for i in range(n+1) ]    # List comprehension method
deco[0] = crossed     # Algo starts from 2, but Python list index is from 0
deco[1] = crossed     # so 0,and 1 are created as dummy, but never proessed

for roundnum in range(2, n):
    for i in range(2,n):
        if deco[i] == plain:  # first i that is plain to be circled
            deco[i] = circled  # circling done, let’s start crossing out its multiples
            for k in range(2*i,n, i): # this range supplies, 2i,3i,4i etc upto n
                deco[k] = crossed
                
### all rounds completed, time for results
print("Prime numbers are: ")
for i in range(n):
    if deco[i] == circled:
        print (i, end =",")
print ("\n Sieve of Eratosthenes done.")