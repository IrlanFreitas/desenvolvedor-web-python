import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("***     Escolha seu jogo!     ***")
    print("*********************************")

    print("(1) Forca (2) Adivinhacao")
    jogo_escolhido = int(input("Qual jogo ?"))

    if jogo_escolhido == 1:
        print("\nJogando Forca\n")
        forca.jogar()

    elif jogo_escolhido == 2:
        print("\nJogando Adivinhação\n")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
