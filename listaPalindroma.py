tamanho = int(input())
lista = [int(i) for i in input().split()]

left = 0
right = len(lista) - 1
maneiras = 0

while left < right:
    if lista[left] == lista[right]:
        left += 1
        right -= 1
    elif lista[left] > lista[right]:
        lista[right-1] += lista[right] # Soma no próximo elemento
        right -= 1 # Passa index para o próximo elemento
        maneiras += 1
    elif lista[left] < lista[right]:
        lista[left+1] += lista[left]
        left += 1
        maneiras += 1

print(maneiras)