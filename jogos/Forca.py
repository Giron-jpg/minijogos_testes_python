import random
def jogar():
    texto1 = "*"
    texto2 = "** Bem vindo ao jogo da Forca **"
    print("\n",len(texto2)*texto1,"\n",texto2,"\n",len(texto2)*texto1,"\n")
    #print("** Bem vindo ao jogo da Forca **")
    #print(len(texto2)*texto1)
    #condições de vitória
    enforcou = False
    ganhou = False

    erros: int = 0 #chances
    palavras = [] #arranjo de palavras
    arquivo = open("frutas.txt", "r") #vinculo com arquivo
    for linha in arquivo: #conjunto palavras vai receber um novo elemento para cada linha no arquivo
        linha = linha.strip().lower()
        palavras.append(linha)
    arquivo.close() #fechar arquivo pra não ocupar espaço
    #print(palavras) imprime as palavras

    x = random.randrange(0, len(palavras)) #seleciona um numero aleatorio de acordo com o tamanho do conjunto
    palavra_secreta = palavras[x]   #seleciona o elemento do cunjunto aleatorio
    #print(palavra_secreta) imprime a resposta

    letras_acertadas = ["_" for letra in palavra_secreta]


    #enquanto não se enforcou e não ganhou o jogo roda
    while(not enforcou and not ganhou):
        #para evitar entradas que não sejam os caracteres corretos usamos lower(tudo minusculo) strip(tira espaços)
        tentativa = input("Escolha uma letra: ").lower().strip()
        i = 0

        #laço if para testar a entrada
        if (tentativa in palavra_secreta):
            #laço for para testar as letras da palavra
            for letra in palavra_secreta:
                #laço if pra se a entrada corresponder a alguma letra da palavra
                if (tentativa == letra):
                    letras_acertadas[i] = letra
                i = i + 1 #faz a contagem da posição para testar a letra
                letras_faltando = int(letras_acertadas.count("_")) #faz a contagem de espaços vazios
        else:
            erros += 1 #encremento de erros por entrada errada
            print("Você possui {} tentativas".format(7-erros))
            desenha_forca(erros)


        print(letras_acertadas) #imprime na tela a lista

        #Outro jeito de escrever algumas linhas
        #if (letras_faltando == 0):
            #ganhou = True
            #print("Você venceu")
        #ganhou = n == 0

        ganhou = "_" not in letras_acertadas #sai do laço while se completa
        enforcou = erros == 7 #sai do laço while se excede as tentativas
    if (ganhou):
        print("Parabéns")
        imprime_mensagem_vencedor()
    else:
        print("Você perdeu a palavra era {}".format(palavra_secreta))


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if(__name__ == "__main__"):
    jogar()