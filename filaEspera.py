#Entrada
quant = int(input())
string = input()
array = [int(num) for num in string.split()]

cont=0

for i in range(quant):
    if i != 0:
        if array[i] >=65:
            if array[i-1] <65:
                if array[i] > array[i-1]:
                    cont+=1
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue

#Saída
if cont > 0:
    print('N')
else:
    print('S')