# Jogo da Palavra Secreta

import os

palavra = 'saturno' # Palavra que terá que ser adivinhada pelo usuario
letras_acertadas = '' # Variável para letras acertadas
tentativa = 0 # Variável para contar as tentativas

while True:
    letra_digitada = input('Digite uma letra: ') # Entrada para o usuário digitar uma letra
    tentativa += 1 # Contador de tentativas

    if len(letra_digitada) > 1: # Verifica se o usuário digitou mais de uma letra
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra: # Verifica se a letra digitada está na palavra secreta
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra: # Loop para ficar mostrando ao usuário quantas letras ele acertou

        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra: # Mostra o resultado final após o usuário ter acertado a palavra
        os.system('cls') # Limpa a tela
        print('VOCÊ ACERTOU!')
        print(f'Palavra secreta: {palavra}')
        print(f'Tentativas: {tentativa}')
        letras_acertadas = ''
        tentativa = 0
        