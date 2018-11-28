import os



def exibir_palavra(_formacao_palavra, _forca):

    for _letra in _formacao_palavra:

        if _letra == None:
            _forca += " - "
        else:
            _forca += " " + _letra + " "

    return _forca

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def jogar():

    #clear = lambda: os.system('cls')

    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "python"

    formacao_palavra = [None] * len(palavra_secreta)

    forca = ""

    tentativas = 6

    count = 0

    while count < tentativas:

        #cls()
        letra = input("Qual letra?").lower().strip()

        if len(letra) > 1:
            letra = list(letra)[0]

        indice_letra_encontrado = [ pos for pos, char in enumerate(palavra_secreta) if char == letra]

        if len(indice_letra_encontrado) == 0:

            count += 1

        else:

            for index in sorted(indice_letra_encontrado, reverse=True):
                formacao_palavra[index] = letra

        forca = exibir_palavra(formacao_palavra, forca)

        terminou = True

        for _letra in formacao_palavra:

            if _letra == None:
                terminou = False


        if terminou == True:
            print(forca)
            print("Você finalizou o jogo")
            break;

        print(forca)
        forca = ""

    if count == tentativas:
        print("\nVocê não conseguiu encontrar a palavra, tente novamente.\n")

    print("\n*********************************")
    print("***         Fim do jogo!      ***")
    print("*********************************")


if __name__ == "__main__":
    jogar()