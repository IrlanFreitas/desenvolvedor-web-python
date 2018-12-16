def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".lower()
    # List Comprehensions - Explicando, para cara item da lista (string, tupla, range, string)
    # que chamamos de letra vamos colocar um caractere "_", essa lista é a palavra_secreta
    letras_acertadas = ["_" for letra in palavra_secreta]

    # formacao_palavra = [None] * len(palavra_secreta)

    enforcou = False
    acertou = False
    # tentativas = 3;
    erros = 0
    quantidade_tentativas = 6;

    print(letras_acertadas)

    while not acertou and not enforcou:

        chute = input("Qual letra ?").lower().strip()

        # Feito por mim caso tenha mais de uma letra inserida
        if len(chute) > 1:
            chute = list(chute)[0]

        # achou = False
        #
        # for idx, _letra in enumerate(palavra_secreta):
        #
        #     if _letra == chute:
        #         achou = True
        #         formacao_palavra[idx] = chute

        if chute in palavra_secreta:

            index = 0
            for _letra in palavra_secreta:

                if chute == _letra:
                    letras_acertadas[index] = _letra
                index += 1
        else:
            erros += 1
            print("Você usou {} tentativas de {}.".format(erros, quantidade_tentativas))

        enforcou = erros == quantidade_tentativas

        acertou = "_" not in letras_acertadas

        # if achou == False:
        #     tentativas -= 1
        #
        # if tentativas == 0:
        #     enforcou = True

        # print(formacao_palavra)
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
