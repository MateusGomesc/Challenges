def verificaPrimo(num):
    contador = 0

    for i in range(1, num+1):
        if num % i == 0:
            contador+=1
    
    if contador == 2:
        return True
    else:
        return False
    

n = int(input())
mdcs = []

for i in range(n):
    str = input()
    v = [int(num) for num in str.split()]
    cont = 2

    while True:
        temp=0
        res = []
        if verificaPrimo(cont):
            if v[0] % cont == 0:
                valor = v[0]
                v[0] = valor / cont
                temp+=1
            
            if v[1] % cont == 0:
                valor = v[1]
                v[1] = valor / cont
                temp+=1
            
            if temp == 2:
                res.append(cont)

            if v[0] == 1 and v[1] == 1:
                break

        cont+=1
        print(cont)
    
    mdc = 1

    for i in range(len(res)):
        mdc *= res[i]
    
    mdcs.append(mdc)

for i in range(len(mdcs)):
    print(mdcs[i])