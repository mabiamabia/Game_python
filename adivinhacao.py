print("**********************************")
print("Bem vindo ao jogo de adivinhação!")
print("**********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1


while(rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute   = int(input("Digite o seu número: "))
    print("você digitou", chute)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Parabens, você acertou o número secreto!")
    else:
        if(maior):
            print("Você errou o numero secreto, seu chute foi maior que o numero...")
        elif(menor):
            print("Você errou o numero secreto, seu chute foi menor que o numero...")

    rodada = rodada + 1

    print("Fim do jogo")