def somaArray(v):
    soma=0
    for i in range(len(v)):
        soma += v[i]
    
    return soma



array = []
quant = int(input())

for i in range(quant):
    num = int(input())

    if num != 0:
        array.append(num)
    elif i != 0:
        array.pop()


print(somaArray(array))