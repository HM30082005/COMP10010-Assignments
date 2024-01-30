
def eratothenes_sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    pnum1 = []
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for i in range(2, n+1):
        if prime[i]:
            pnum1.append(i)
            print(i, end=" ")
    return pnum1

def square_sum(pnum):
    sum = 0
    for i in range(len(pnum)):
        sum += pnum[i] * pnum[i]
    return sum

    
while True:
    n = int(input('Give me a number N: '))
    pnum = eratothenes_sieve(n)
    print()
    # print(pnum)
    print(square_sum(pnum))
    message = input('Do u want to compute a new square sum?\n(Type "yes" to continue, or any other key to exit)')
    if message.lower() != 'yes':
        break