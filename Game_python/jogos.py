import adivinhacao
import forca


def escolhe_jogo():
    print(50 * "*")
    print(15 * "*", "Escolha o seu jogo", 15 * "*")
    print(50 * "*")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o número do seu jogo? "))

    if(jogo == 1):
        print("Você escolheu o jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Você escolheu o jogo da Adivinhação")
        adivinhacao.jogar()
if(__name__ == "__main__"):
    escolhe_jogo()