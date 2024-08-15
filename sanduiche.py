def fatorial(num):
    resultado = 1
    for i in range(1, num+1):
        resultado *= i
    return resultado
        

n, m = [int(i) for i in input().split()]
combinacoes = []

for i in range(m):
    combinacao = [int(j) for j in input().split()]
    combinacoes.append(combinacao)

soma = 0
for i in range(1, n+1):
    soma += fatorial(n) / (fatorial(i) * fatorial(n-i))

print(int(soma) - len(combinacoes)-1)