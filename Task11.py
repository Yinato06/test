numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
notPrimes = []
for num in numbers:
    if num == 1:
        continue
    isPrime = True
    for divider in range(2, num):
        if num % divider == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(num)
    else:
        notPrimes.append(num)
print('Prime: ', primes)
print('Not prime: ', notPrimes)
