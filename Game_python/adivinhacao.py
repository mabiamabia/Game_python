import random

def jogar():

        print("**********************************")
        print("Bem vindo ao jogo de adivinhação!")
        print("**********************************")

        numero_secreto = round(random.randrange(1, 101)) # gera numero entre 1 e 100
        total_de_tentativas = 0
        pontos = 1000

        print("Qual nível de dificuldade você quer escolher? ")
        nivel = int(input("(1)facil (2)medio (3)dificil: "))

        if(nivel == 1):
            total_de_tentativas = 20
        elif(nivel == 2):
            total_de_tentativas = 10
        else:
            total_de_tentativas = 5

        print(numero_secreto)

        for rodada in range(1, total_de_tentativas + 1):
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))
            chute   = int(input("Digite um número entre 1 e 100: "))
            print("você digitou", chute)

            if(chute < 1 or chute > 100):
                print("Você deve digitar um numero entre 1 e 100!")
                continue

            acertou = numero_secreto == chute
            maior   = chute > numero_secreto
            menor   = chute < numero_secreto

            if (acertou):
                print("Parabens, você acertou o número secreto e fez {} pontos!".format(pontos))
                break;
            else:
                if(maior):
                    print("Você errou o numero secreto, seu chute foi maior que o numero...")
                elif(menor):
                    print("Você errou o numero secreto, seu chute foi menor que o numero...")
                
                pontos_perdidos = abs(numero_secreto - chute) 
                pontos = pontos - pontos_perdidos

        print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()
