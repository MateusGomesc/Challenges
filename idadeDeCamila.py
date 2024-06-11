idades = []

for i in range(3):
    idades.append(int(input()))

    if i == 2:
        idades.sort()
        print(idades[1])