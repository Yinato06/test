result = str()
n = int(input('Введите число от 3 до 20: '))

if 3 <= n <= 20:
    while len(result) < n:
        for i in range(1, n):
            for j in range(i + 1, n):
                if i != j and ((i + j) % n == 0):
                    result += str(i) + str(j)
        break
else:
    print('Неверное число!')

print(result)
