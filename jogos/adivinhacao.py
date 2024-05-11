import random
def jogar():
    texto1 = "*"
    vezes = 38
    print(vezes*texto1)
    print("** Bem vindo ao jogo da Adivinhação **")
    print(vezes*texto1)

    #escolhendo uma dificuldade ocm base no numero de tentativas
    print("Escolha uma dificuldade: \n(1)Fácil \n(2)Médio \n(3)Difícil \n")
    nivel = int(input("Dificuldade: "))
    chance = 0
    if (nivel == 1):
        chance = 20
    elif (nivel == 2):
        chance = 10
    elif (nivel == 3):
        chance =5

    points = 1000

    #definindo o numero secreto aleatóriamente
    numero_secreto = random.randrange(1,101)

    #laço de repetição
    for rodada in range(1,chance+1):
        print("Você esta na rodada {:02} de {}".format(rodada, chance))

        #Inserindo tentativas de números
        tentativa = input("Digite um número entre 1 e 100: ")

        #Convertendo a str em int após a tentativa
        numero = int(tentativa)

        if (numero < 1 or numero > 100):
            print("Esse valor não está dentro do permitido, tente novamente")
            continue

        print("Você digitou ", numero)

        #Possiveis combinações de respostas
        acertou = numero == numero_secreto
        maior   = numero > numero_secreto
        menor   = numero < numero_secreto



        #verificações dos valores
        if(acertou):
            print("Parabéns, você acertou")
            break
        else:
            x = abs(numero_secreto - numero)
            points = points - x
            if (maior):
                print("Sua tentativa foi maior que o número secreto")
            elif (menor):
                print("Sua tentativa foi menor que o numero secreto")


    print("Fim do jogo, o número secreto era: {} \n e sua pontuação foi {}".format(numero_secreto,points))

if (__name__ == "__main__"):
    jogar()