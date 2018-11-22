
import random #importando um modulo que não é buildin function https://docs.python.org/3/library/functions.html

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")


# Gerado pseudo - aleatoriamente
# numero_secreto = round(random.random(1, 100) * 100) # Usando snake_case

numero_secreto = random.randrange(1, 101) # Melhorando a forma de gerar número aletórios

# chute = input("Digite o seu numero:") # O valor é passado por str é necessária a conversão

chute = ""
total_tentativas = 3
rodada = 1
count_tentativas = total_tentativas
eh_valor_permitido = False


#Só aceita o valor se for int
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

for total_tentativas_for in range( 1, total_tentativas + 1): # Usando for!

    #print("\nTentativa ", rodada, " de ", count_tentativas)
    print("\nTentativa {} de {}".format(total_tentativas_for, total_tentativas)) #String Interpolation
    print("total_tentativas_for - {}".format(total_tentativas_for)) #Aprender mais sobre formatação - https://pyformat.info/
    print("numero_secreto - ", numero_secreto)

    while chute.isdigit() == False :
        chute = input("Digite um número entre 1 e 100:")

    if (int(chute) < 1 or int(chute) > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue # Pulando uma iteração

    #acertou = int(chute) == numero_secreto
    #eh_maior = int(chute) > numero_secreto
    #eh_menor = int(chute) < numero_secreto

    if int(chute) == numero_secreto:
        print("Você acertou o numero")
        break
    else:
        if int(chute) > numero_secreto:
            print("Você deu um chute maior que o número secreto")

        else:
            print("Você deu um chute menor que o número secreto")

            #total_tentativas -= 1

    #rodada += 1
    chute = "" #Reinicia a obtenção de valores


print("\nFim do jogo!")

