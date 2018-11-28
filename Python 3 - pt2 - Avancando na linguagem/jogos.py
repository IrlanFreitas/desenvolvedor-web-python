import forca
import adivinhacao
import forca_feito_por_mim

def escolhe_jogo():
    print("*********************************")
    print("***     Escolha seu jogo!     ***")
    print("*********************************")

    print("(1) Forca (Alura Version)  (2) Forca (Irlan Version)  (3) Adivinhacao")
    jogo_escolhido = int(input("Qual jogo ?"))

    if jogo_escolhido == 1:
        print("\nJogando Forca (Alura Version) \n")
        forca.jogar()

    elif jogo_escolhido == 2:
        print("\nJogando Forca (Irlan Version)\n")
        forca_feito_por_mim.jogar()

    elif jogo_escolhido == 3:
        print("\nJogando Adivinhação\n")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
