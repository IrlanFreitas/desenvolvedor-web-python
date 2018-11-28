import random  # importando um modulo que não é buildin function https://docs.python.org/3/library/functions.html


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # Gerado pseudo - aleatoriamente
    # numero_secreto = round(random.random(1, 100) * 100) # Usando snake_case

    numero_secreto = random.randrange(1, 101)  # Melhorando a forma de gerar número aletórios

    # chute = input("Digite o seu numero:") # O valor é passado por str é necessária a conversão

    [nivel, chute] = [0, ""]
    total_tentativas = 0
    rodada = 1
    count_tentativas = total_tentativas
    eh_valor_permitido = False
    pontos_perdidos_por_rodada = 1000
    pontos_perdidos_por_distancia = 1000
    quantidade_pontos_perdidos_rodada = 0  # Balanceamento de pontos perdidos por difículdade

    while nivel < 1 or nivel > 3:
        nivel = int(input("\nDigite o nível de dificuldade:\n 1 - Fácil, 2 - Médio, 3 - Difícil\nDefina o nível:"))

    if nivel == 1:
        total_tentativas = 20

    elif nivel == 2:
        total_tentativas = 10

    elif nivel == 3:
        total_tentativas = 5

    quantidade_pontos_perdidos_rodada = pontos_perdidos_por_rodada / total_tentativas

    # Só aceita o valor se for int
    # while total_tentativas != 0:
    #
    #     #print("\nTentativa ", rodada, " de ", count_tentativas)
    #     print("\nTentativa {} de {}".format(rodada, count_tentativas)) #String Interpolation
    #
    #     while chute.isdigit() == False:
    #         chute = input("Digite o seu numero:")
    #
    #     #acertou = int(chute) == numero_secreto
    #     #eh_maior = int(chute) > numero_secreto
    #     #eh_menor = int(chute) < numero_secreto
    #
    #     if int(chute) == numero_secreto:
    #         print("Você acertou o numero")
    #         break
    #     else:
    #         if int(chute) > numero_secreto:
    #             print("Você deu um chute maior que o número secreto")
    #
    #         else:
    #             print("Você deu um chute menor que o número secreto")
    #
    #         total_tentativas -= 1
    #
    #     rodada += 1
    #     chute = "" #Reinicia a obtenção de valores

    for total_tentativas_for in range(1, total_tentativas + 1):  # Usando for!

        # print("\nTentativa ", rodada, " de ", count_tentativas)
        print("\nTentativa {} de {}".format(total_tentativas_for, total_tentativas))  # String Interpolation
        # print("total_tentativas_for - {}".format(total_tentativas_for)) #Aprender mais sobre formatação - https://pyformat.info/
        # print("numero_secreto - ", numero_secreto)
        print("Pontos perdidos por rodada = ", quantidade_pontos_perdidos_rodada)

        while chute.isdigit() == False:
            chute = input("Digite um número entre 1 e 100:")

        if (int(chute) < 1 or int(chute) > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue  # Pulando uma iteração

        # acertou = int(chute) == numero_secreto
        # eh_maior = int(chute) > numero_secreto
        # eh_menor = int(chute) < numero_secreto

        if int(chute) == numero_secreto:
            print("\nVocê acertou o numero! O numero é ", numero_secreto)
            break
        else:
            if int(chute) > numero_secreto:
                print("\nVocê deu um chute maior que o número secreto!")
                pontos_perdidos_por_distancia -= (
                            int(chute) - numero_secreto)  # poderia fazer com abs() numero absoluto.

            else:
                print("\nVocê deu um chute menor que o número secreto!")
                pontos_perdidos_por_distancia -= (numero_secreto - int(chute))

                # total_tentativas -= 1
            # Feito com número absoluto.
            # pontos_perdidos_por_distancia -= abs(int(chute) - numero_secreto)
            pontos_perdidos_por_rodada -= quantidade_pontos_perdidos_rodada;

        # rodada += 1
        chute = ""  # Reinicia a obtenção de valores

    print("\n*********************************")
    print("Fim do jogo! ")
    print("Você finalizou com ", pontos_perdidos_por_rodada, " pontos de rodada")
    print("Você finalizou com ", pontos_perdidos_por_distancia, " pontos de distância")
    print("*********************************")

# Pra ser utilizado quando o arquivo for chamado diretamente
# Se for acessado pelo terminar a variavel __name__ que é do python
# terá o valor __main__, caso não seja isso o arquivo está
# apenas sendo importado.
if __name__== "__main__":
    jogar()