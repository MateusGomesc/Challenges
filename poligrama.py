tam = int(input())
palavra = input()

veri = 0
cont = 0
for i in range(len(palavra)):
    for char1 in palavra[:i]:
        for char2 in palavra[i:]:
            if char1 == char2:
                cont += 1
        
        if not cont:
            print("*")
            break
        else:
            veri += 1
    
    print('Verifica: ', veri)
    if veri == i+1:
        print(palavra[:i])
        break
    else:
        veri = 0



