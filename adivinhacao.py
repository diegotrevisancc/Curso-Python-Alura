import time
import random

def jogar():

    relogio = time.localtime()
    print("Data: {:02d}/{:02d}/{:4d}" .format(relogio[2], relogio[1], relogio[0]))
    print("Horário Local: {:02d}:{:02d}:{:02d}" .format(relogio[3], relogio[4], relogio[5]))



    print("*******************")
    print("Jogo de Adivinhação", sep ="-", end = "\n")
    print("*******************")

    numero_secreto = round(random.random()*100)


    nome = input("Insira o seu nome: ")
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print(" (1) Fácil\n (2) Médio \n (3) Difícil")
    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 3

    for rodada in range (1,total_de_tentativas+1):


        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        chute = int(input("Insira um número entre 1 e 100: "))

        if (chute<1 or chute>100):
            print("Você deve digitar um número entre 1 e 100!\n")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns {}, você acertou" .format(nome))
            break

        elif (maior):
            print("Droga! {}, você errou e o número chutado é maior que o número que você deve acertar." .format(nome))
            pontos = pontos - abs(chute - numero_secreto)
        else:
            print("Droga! {}, você errou e o número chutado é menor que o número que você deve acertar.".format(nome))
            pontos = pontos - abs(numero_secreto - chute)
    print("Fim de jogo.")
    print("O número secreto é: {}" .format(numero_secreto))
    print("Sua pontuação é de {:.2f}" .format(pontos))

if(__name__ == "__main__"):
    jogar()