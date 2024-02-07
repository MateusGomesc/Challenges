questoes = []

while True:
    n = int(input())

    if n == 0:
        break
    
    cont = 0

    for i in range(0, n):
        linha = input()
        linha.split()
        int(linha)

        for j in range(0, len(linha)):
            if linha[j] <= 127:
                cont += 1
                index = j
        
        if cont > 1:
            if index == 0:
                questoes.append('A')
            if index == 1:
                questoes.append('B')
            if index == 2:
                questoes.append('C')
            if index == 3:
                questoes.append('D')
            if index == 4:
                questoes.append('E')
        else:
            questoes.append('*')

print(questoes)
for i in range(0, len(questoes)):
    print(f'${questoes[i]}\n')