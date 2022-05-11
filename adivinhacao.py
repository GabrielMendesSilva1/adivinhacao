import random

print("O programa sorteará um número de 1 a 100, tente adivinhar!\n Boa sorte. ")
restart = 1
while restart == 1:

    tentativa = 1
    palpite = 0
    y = random.randint(1, 100)

    while palpite != y:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except:
            print("Apenas números são aceitos.")
            continue

        if palpite > y:
            print("O palpite está acima da resposta correta.")
            tentativa += 1
        elif palpite < y:
            print("O palpite está abaixo da resposta correta.")
            tentativa += 1

    else:
        print(" Parabéns, você acertou! \n Número de tentativas: {}".format(tentativa))

    restart = int(input("Para reinicicar o jogo, digite 1.\n Para sair, aperte qualquer caractere: "))
else:
    exit(0)
