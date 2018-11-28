def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    formacao_palavra = [None] * len(palavra_secreta)

    enforcou = False
    acertou = False
    tentativas = 3;

    while(not acertou and not enforcou):

        letra = input("Qual letra ?").lower().strip()

        achou = False

        for idx, _letra in enumerate(palavra_secreta):

            if _letra == letra:
                achou = True
                formacao_palavra[idx] = letra

        if achou == False:
            tentativas -= 1

        if tentativas == 0:
            enforcou = True

        print(formacao_palavra)


    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()