import time
import random

relogio = time.localtime()
print("Data: {:02d}/{:02d}/{:4d}" .format(relogio[2], relogio[1], relogio[0]))
print("Horário Local: {:02d}:{:02d}:{:02d}" .format(relogio[3], relogio[4], relogio[5]))

def imprime_mensagem_de_abertura():

    print("*******************")
    print("Jogo de Forca", sep="-", end = "\n")
    print("*******************")


def carrega_palavra_secreta():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))


    palavra_secreta = palavras[
        numero].upper()
    return palavra_secreta


def inicializa_letras_criadas(palavra):

    lista = ["_" for letra in palavra]
    return lista


def pede_chute(nome):
     chute = input("{}, insira uma letra: " .format(nome))
     chute = chute.strip().upper()
     return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0  # Variável que vai indicar o posicionamento das letras que são achadas
    for letra in palavra_secreta:  # Laço que vai procurar a letra na palavra secreta
        if (
                chute == letra):  # Dessa forma sempre estaremos comparando letras maiúsculas, independente da palavra escolhida e do chute do usuário
            letras_acertadas[index] = letra
        index += 1

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
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def jogar():

    imprime_mensagem_de_abertura()

    nome = input("Insira o seu nome: ")

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_criadas(palavra_secreta)

    print("A palavra tem {} letras.".format(len(palavra_secreta)))
    print(letras_acertadas)

    enforcou = False
    acertou = False



    erros = 0

    while(not enforcou and not acertou ):

        chute = pede_chute(nome)

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
        print("Você tem {} chances" .format(7 - erros))
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        desenha_forca(erros)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim de jogo.")
if(__name__ == "__main__"):
    jogar()
