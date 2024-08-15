num1, num2 = [int(i) for i in input().split()]

if num1 > num2:
    menor = num2
else:
    menor = num1

num3 = 3 * menor - num1 - num2

print(num3)