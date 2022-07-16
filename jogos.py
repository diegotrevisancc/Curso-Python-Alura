import forca_sem_organizacao
import adivinhacao
import time

def escolhe_jogo():
    relogio = time.localtime()
    print("Data: {:02d}/{:02d}/{:4d}" .format(relogio[2], relogio[1], relogio[0]))
    print("Horário Local: {:02d}:{:02d}:{:02d}" .format(relogio[3], relogio[4], relogio[5]))

    print("*******************")
    print("Escolha o seu jogo!", end = "\n")
    print("*******************")

    print("(1) Forca\n(2) Adivinhação")
    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo ==2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
if(__name__=="__main__"):
    escolhe_jogo()