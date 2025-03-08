basesSuportadas = [2, 3, 8, 10, 16]

def conjuntoRestos(n,div):
    casasOrdenadas = []
    while n >= 1:
        casasOrdenadas.append(n % div)
        n //= div
    return casasOrdenadas

def inverterHex(sequencia):
    x = []
    for elemento in sequencia:
        if isinstance(elemento, int) and elemento < 10: 
            x.append(elemento)
        else:
            match elemento:
                case 10: x.append('A')
                case 11: x.append('B')
                case 12: x.append('C')
                case 13: x.append('D')
                case 14: x.append('E')
                case 15: x.append('F')
                case 'A': x.append(10)
                case 'B': x.append(11)
                case 'C': x.append(12)
                case 'D': x.append(13)
                case 'E': x.append(14)
                case 'F': x.append(15)
                case _: x.append(int(elemento))
    return x

def pegarBase(prompt):
    while True:
        base = 0
        try:
            base = int(input(prompt))
            if base not in basesSuportadas:
                print('Insira uma base válida.')
            else:
                return int(base)
        except ValueError:
            print('Insira uma base válida.')

def pegarValor(prompt):
    while True:
        try:
            if baseEntrada == basesSuportadas[4]:
                valor = (input(prompt))
                valorChars = []
                for char in valor:
                    valorChars.append(char.upper())
                valor = inverterHex(valorChars)
                return valor[::-1]
            else:
                valor = int(input(prompt))
                valorOrdenado = conjuntoRestos(valor, 10)
                i = 0
                while i < len(valorOrdenado):
                    if valorOrdenado[i] >= baseEntrada:
                        raise ValueError
                    i += 1
            return valor
        except ValueError:
            print('Insira um valor válido.')

# Pega os valores iniciais e a base da saída
print('-==--====Conversor de bases===--==-','\nBases suportadas:',basesSuportadas,'\n')
# pegar os 3
baseSaida = pegarBase('Base de saída: ')
baseEntrada = pegarBase('Base de entrada: ')
valorEntrada = pegarValor('Valor de entrada: ')
valorEntradaB = valorEntrada

# Checa se a base é 10 e converte pra ela se não for
if baseEntrada != basesSuportadas[3]: # base 10
    if type(valorEntrada) != list:
        decOrdem = conjuntoRestos(valorEntrada,10)
    else:
        decOrdem = valorEntrada
    valorDec = 0
    i = 0
    while i < len(decOrdem):
        valorDec += (decOrdem[i]*(baseEntrada**i))
        i += 1
    valorEntrada = valorDec

# Bota todos os restos em um conjunto e inverte ele pra printar
valorSaida = conjuntoRestos(valorEntrada,baseSaida)
if baseSaida == basesSuportadas[4]:
    valorSaida = inverterHex(valorSaida)
valorSaida = valorSaida[::-1]

saidaFormatada = ""
for i in valorSaida:
    saidaFormatada += str(i) 
print('\nO número',valorEntradaB,'da base',baseEntrada,'na base',baseSaida,'é:',saidaFormatada)        
input('\nAperte enter para sair... ')