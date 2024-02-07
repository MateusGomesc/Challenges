#Entrada
stringInput = input()
inputs = [int(num) for num in stringInput.split()]
matriz = []
arrayFinal = []

for i in range(inputs[0]):
    stringMatriz = input()
    matriz.append([int(num) for num in stringMatriz.split()])

for i in range(inputs[2]):
    stringCoord = input()
    coord = [int(num) for num in stringCoord.split()]
    somaLinha = 0
    somaColuna = 0

    for j in range(inputs[1]):
        somaLinha += matriz[coord[0]-1][j]

    for k in range(inputs[0]):
        somaColuna += matriz[k][coord[1]-1]
    
    somaFinal = somaLinha + somaColuna - matriz[coord[0]-1][coord[1]-1]
    arrayFinal.append(somaFinal)

#Saída
for i in range(len(arrayFinal)):
    print(arrayFinal[i])