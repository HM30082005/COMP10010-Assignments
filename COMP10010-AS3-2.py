while True:
    n = int(input('Give me a number N: '))
    square_sum = 0
    for i in range(2, n+1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                # print(i, j)
                isPrime = False    
        if isPrime:
            print(i, end=" ")
            square_sum += i * i
    print()
    print("Square sum is", square_sum)
    answer = input('Do u want to compute a new square sum?\n(Type "yes" to continue, or any other key to exit)')
    if answer.lower() != 'yes':
        break