def isConsoante(letra):
    consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z"]

    if letra in consoantes:
        return True
    else:
        return False

def isVogal(letra):
    vogais = ['a', 'e', 'i', 'o', 'u']

    if letra in vogais:
        return True
    else:
        return False
    
def vogalMaisProxima(letra):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
    index = None

    for key, c in enumerate(alfabeto):
        if c == letra:
            index = key
    
    antes = alfabeto[:index]
    antes.reverse()
    depois = alfabeto[index+1:]
    indexVogais = [0, 0]

    for i in range(len(antes)):
        if isVogal(antes[i]):
            indexVogais[0] = i
            break
    
    for j in range(len(depois)):
        if isVogal(depois[j]):
            indexVogais[1] = j
            break
    
    if indexVogais[0] > indexVogais[1]:
        return depois[indexVogais[1]]
    elif indexVogais[1] > indexVogais[0]:
        return antes[indexVogais[0]]
    else:
        return antes[indexVogais[0]]

def consoanteMaisProxima(letra):
    consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z"]
    index = None

    if letra == 'z':
        return 'z'

    for key, c in enumerate(consoantes):
        if letra == c:
            index = key

    depois = consoantes[index+1:]

    for i in range(len(depois)):
        if isConsoante(depois[i]):
            return depois[i]




palavra = input()
novaPalavra = []

for i in range(len(palavra)):
    novaPalavra.append(palavra[i])
    if isConsoante(palavra[i]):
        novaPalavra.append(vogalMaisProxima(palavra[i]))
        novaPalavra.append(consoanteMaisProxima(palavra[i]))

print(''.join(novaPalavra))