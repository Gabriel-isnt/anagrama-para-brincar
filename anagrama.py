from random import randrange

palavras = [
    'banana', 'cadeira', 'maçã', 'relógio', 'laranja',
    'mesa', 'abacaxi', 'sofá', 'uva', 'televisão',
    'morango', 'computador', 'pera', 'lâmpada', 'melancia',
    'cadeado', 'pêssego', 'geladeira', 'melão', 'espelho',
    'sanduíche', 'escrivaninha', 'cenoura', 'vaso', 'pão',
    'estante', 'alface', 'teclado', 'berinjela', 'cadeira',
]


# função
def reorganizar_palavras(palavra) -> tuple:
    rearranja = 0
    lista_palavra = list(palavra)

    while rearranja < 7:
        # pegando os indices que vão trocar
        # esses indices são aleatórios
        num1 = randrange(0, len(palavra))
        num2 = randrange(0, len(palavra))

        while num1 == num2:  # caso os indices sejam o mesmo
            num1 = randrange(0, len(palavra))

        # pegando as letras
        letra1 = lista_palavra[num1]
        letra2 = lista_palavra[num2]

        # fazendo a troca
        lista_palavra[num1] = letra2
        lista_palavra[num2] = letra1

        rearranja += 1

    nova_palavra = ''.join(lista_palavra)
    return nova_palavra, palavra


# programa rodando
tentativas = 7
print('acerte qual palavra esse anagrama forma')
print(f'você tem {tentativas} chances para acertar')
print()  # para ficar melhor para o usuário ler as coisas

while True:
    a = reorganizar_palavras(palavras[randrange(0, len(palavras))])
    baguncado = a[0]
    arrumado = a[1]

    while tentativas > 0:
        print(f'\033[96m{baguncado}\033[0m')
        chute  = str(input('\033[93mqual palavra forma? \n: \033[0m').strip().lower())
        if chute == arrumado:
            print('você acertou')
            print(f'\033[94managrama: {baguncado} | palavra certa: {arrumado}\033[0m')
            break

        else:
            tentativas -= 1
            if tentativas != 0:
                print('\033[91mERRADO, tente outra vez\033[0m')
                print(f'\033[95mvocê tem {tentativas} tentativas restantes\033[0m')
                print()  # para organização :)

            else:
                print()  # c já sabe né ? :P
                print('você perdeu o jogo :(')
                print(f'\033[94managrama: {baguncado} | palavra certa: {arrumado}\033[0m')
                break

    jogar_novamente = str(input('quer jogar de novo? [s / n] \n>> ').strip().lower())
    if jogar_novamente not in ('s', 'sim'):
        break
