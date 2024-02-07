t = input()
n = int(input())

for i in range(0, n):
    a = input()

    if a == 'burrito':
        t = 'foguento'
    elif a == 'alface':
        t = 'pranta'
    elif a == 'cerveja':
        t = 'aguado'

print(t)
