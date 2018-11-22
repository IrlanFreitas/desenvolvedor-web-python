

def busca_linear_autores(_autor):
    print("Busca Linear:\n")

    resposta = "NOT-FOUND"

    autores = ["Jhonathan", "Smith", "Paul", "Vincent", "Freire", "Lucca"]

    for index, autor in enumerate(autores):
        if _autor == autor:
            resposta = index
            break

    return resposta



