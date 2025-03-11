basesSuportadas = [2, 3, 8, 10, 16]
dictHex = { 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F', 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15 }

def conjuntoRestos(n,div):
    casasOrdenadas = []
    while n >= 1:
        casasOrdenadas.append(n % div)
        n //= div
    return casasOrdenadas

def inverterHex(sequencia):
    x = []
    for elemento in sequencia:
        if elemento not in dictHex:
            x.append(elemento)
            continue
        x.append(dictHex[elemento])
    return x

def pegarBase(prompt):
    while True:
        try:
            base = int(input(prompt))
            if base not in basesSuportadas:
                raise ValueError
            return int(base)
        except ValueError:
            print('Insira uma base válida.')

def pegarValor(prompt):
    while True:
        try:
            valor = (input(prompt))
            if baseEntrada != basesSuportadas[4]:
                valor = int(valor)
                valorOrdenado = conjuntoRestos(valor, 10)
                i = 0
                while i < len(valorOrdenado):
                    if valorOrdenado[i] >= baseEntrada:
                        raise ValueError
                    i += 1
                return valor
            valorChars = []
            for char in valor:
                if char.upper() not in dictHex:
                    raise ValueError
                valorChars.append(char.upper())
            valor = inverterHex(valorChars)
            return valor[::-1]
        except ValueError:
            print('Insira um valor válido.')

# Pega os valores iniciais e a base da saída
print('-==--====Conversor de bases===--==-','\nBases suportadas:',basesSuportadas,)
print('Insira a base de saída, a base de entrada e um valor positivo na base de entrada escolhida.\n')
baseSaida = pegarBase('Base de saída: ')
baseEntrada = pegarBase('Base de entrada: ')
valorEntrada = pegarValor('Valor de entrada: ')

# Garante que o número na saída volta pra hexadecimal se ele entrou como decimal
entradaFormatada = ""
if baseEntrada == basesSuportadas[4]: # base 16
    valorEntradaB = inverterHex(valorEntrada[::-1])
    for i in valorEntradaB:
        entradaFormatada += str(i) 
else:
    entradaFormatada = valorEntrada

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

# Bota a saída numa string bonitinha e se a base for 2 ou 16 inclui um espaço a cada 4 caracteres 
saidaFormatada = ""
for i in valorSaida:
    saidaFormatada += str(i)
if baseSaida == basesSuportadas [0] or baseSaida == basesSuportadas[4]: # base 2 ou 16
    saidaFormatada= " ".join(saidaFormatada[i : i + 4] for i in range(0, len(saidaFormatada), 4))
print('\nO número',entradaFormatada,'da base',baseEntrada,'na base',baseSaida,'é:',saidaFormatada)        
input('\nAperte enter para sair... ')