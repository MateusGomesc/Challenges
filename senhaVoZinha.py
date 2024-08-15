n, m, k = [int(i) for i in input().split()]
senha = input()
palavras = []

for i in range(m):
    palavras.append(input())

s = int(input())
copiaK = k
resultados = []

for i in range(m-1):
    for j in range(k):
        for k in range(copiaK):
            lista_sub = [palavras[i][j], palavras[i+1][k]]

            # faz substituições na senha
            resultado = []
            index_sub = 0

            for char in senha:
                if char == "#":
                    resultado.append(lista_sub[index_sub])
                    index_sub += 1
                else:
                    resultado.append(char)
            
            resultados.append(''.join(resultado))

resultados.sort()
print(resultados[s-1])