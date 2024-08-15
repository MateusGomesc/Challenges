s = int(input())
a = int(input())
b = int(input())
contador = 0

for i in range(a, b+1):
    num = str(i)

    soma = 0
    for i in range(len(num)):
        soma += int(num[i])

    if soma == s:
        contador += 1

print(contador)