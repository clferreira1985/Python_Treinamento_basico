import os

carros = [
    ("Chervrolet Tracker", 120),
    ("Chervrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130),
]
alugados = []


def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia. ".format(i, car[0], car[1]))


while True:
    os.system("Clear")
    print("===========================")
    print("Bem vindo à locadora de carros!")
    print("==========================")
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    op = int(input())

    os.system("Clear")
    if op == 0:
        mostrar_lista_de_carros(carros)

    elif op == 1:
        mostrar_lista_de_carros(carros)
        print("=========")
        print("Escolha o código do carro:")
        cod_car = int(input())
        print("Por quantos dias você deseja alugar este carro?")
        dias = int(input())
        os.system("clear")

        print("Você escolheu {} por {} dias.".format(carros[cod_car][0], dias)),
        print(
            "O aluguel totalizaria R$ {}. Deseja alugar?".format(
                dias * carros[cod_car][1]
            )
        )

        print("0 - SIM | 1 - Não")
        conf = int(input())
        if conf == 0:
            print(
                "Parabéns você alugou o {} por {} dias.".format(
                    carros[cod_car][0], dias
                )
            )
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0:
            print("Não há carros ara devolver.")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            mostrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            cod = int(input())
            if cond == 0:
                print("Obrigado por devolveu o {}.".format(alugados[cod][0]))
                carros.append(alugados.pop(cod_car))

    print("")
    print("=========")
    print("0 para CONTINUR | 1 para SAIR")
    if int(input()) == 1:
        break
