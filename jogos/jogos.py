
import Forca
import adivinhacao
print("Escolha uma jogo: \n (1)Forca \n (2)Advinhação \n(3)Teste \n")
jogo = int(input("Qual? "))

if (jogo == 1):
    print("Jogando Forca")
    Forca.jogar()
elif (jogo == 2):
    print("Jogando Advinhação")
    adivinhacao.jogar()