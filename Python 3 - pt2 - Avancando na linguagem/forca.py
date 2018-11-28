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

        chute = input("Qual letra ?").lower().strip()

        if len(chute) > 1:
            chute = list(chute)[0]

        achou = False

        for idx, _letra in enumerate(palavra_secreta):

            if _letra == chute:
                achou = True
                formacao_palavra[idx] = chute

        index = 0
        for _letra in palavra_secreta:

            if chute == _letra:
                print("Encontrei a letra {} na posição {}".format(_letra, index))
            index += 1


        if achou == False:
            tentativas -= 1

        if tentativas == 0:
            enforcou = True

        print(formacao_palavra)


    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()