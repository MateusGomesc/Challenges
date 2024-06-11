quant = int(input())
array = []
amigos = []
tempos = dict()

for i in range(quant):
    array.append(input().split())

for k in range(len(array)):
    if array[k][0] == 'R':
        tempo = 0

        if array[k][1] not in amigos:
            amigos.append(array[k][1])
        
        novoArray = array[k+1:]
        
        for key, item in enumerate(novoArray):
            if item[0] == 'E' and item[1] == array[k][1]:
                break

            if item[1] != array[k][1] and key == len(novoArray) - 1:
                tempo = -1

            if item[0] == 'T':
                tempo += int(item[1])
            else:
                tempo += 1
        
        if array[k][1] in tempos and tempo != -1:
            tempos[array[k][1]] += tempo
        else:
            tempos[array[k][1]] = tempo

for key in tempos:
    print(f'{int(key)} {tempos[key]}')