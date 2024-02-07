# Ler 8 bits, retornar 'S' para sucesso de leitura e 'F' para falha.
str = input().replace(' ', '')
cont = 0

for i in range(8):
    if str[i] != '0' and str[i] != '1':
        cont += 1

if cont > 0:
    print('F')
else:
    print('S')