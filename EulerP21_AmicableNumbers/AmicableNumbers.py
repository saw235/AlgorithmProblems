import itertools
import math

def primes_sieve(limit):

    if limit < 3:
        a = [True] * 2
    else:
        a = [True] * limit

    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i

            for n in range(i*i, limit, i):
                a[n] = False


#find all of N's prime divisor
def GetPrimeDivisor(N):
    prime_divisor = []
    #print(int(math.sqrt(N)))
    for prime in primes_sieve(N+1):
        
        while True:
            if N % prime == 0:
                N = N/prime
                prime_divisor.append(prime)
            else:
                break

    return prime_divisor


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def GenerateProperDivisor(Num):
    if Num == 1:
        return [1]
    prime_divisor = GetPrimeDivisor(Num)
    a = powerset(prime_divisor)
    divisor = {}
    divisor[1] = ()
    for i in a:
        if not i:
            continue
        d = 1
        for j in i:
            d *= j

        if d != Num:
            divisor[d] = i

    return divisor.keys()


i = 3
memo = {}
amicable = []
while i < 10000:

    if i in memo:
        d_2 = sum(GenerateProperDivisor(i))
        if d_2 == memo[i]:
            amicable.append(d_2)
            amicable.append(i)

    d_1 = sum(GenerateProperDivisor(i)) #d(a) = N1
    memo[d_1] = i

    i+= 1
print(amicable)
print(sum(amicable))