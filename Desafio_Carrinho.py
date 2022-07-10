def carrinho():
    continuar = 1

    while continuar:
        continuar = int(input("comprar mais produtos? 1- Sim | 2- Finalizar Compra "))
        if continuar == 1:
            inserir()
        elif continuar == 2:
            finalizar()
        else:
            print("Opcao Inválida, digite novamente")


def inserir():
    if len(produtos) >= 10:
        print("Número máximo de 10 itens")
        finalizar()

    nome = input("Nome do produto: ")
    valor = int(input("Valor: "))

    if produtos.get(nome):
        print("Já existe o produto", nome)
    else:
        produtos[nome] = valor


def finalizar():
    total = 0
    print("Produtos do carrinho:")
    for nome in produtos.keys():
        total = total + produtos[nome]
        print(nome)
    print(f"Valor total : \n{total}\nDeve ser no mínimo em:")

    if total >= 100:
        contador = 0
        while total >= 100:
            contador = contador + 1
            total = total - 100
        if contador == 1:
            print(f"{contador} nota de 100 reais")
        else:
            print(f"{contador} notas de 100 reais")

    if total >= 50:
        contador = 0
        while total >= 50:
            contador = contador + 1
            total = total - 50
        if contador == 1:
            print(f"{contador} nota de 50 reais")
        else:
            print(f"{contador} notas de 50 reais")

    if total >= 20:
        contador = 0
        while total >= 20:
            contador = contador + 1
            total = total - 20
        if contador == 1:
            print(f"{contador} nota de 20 reais")
        else:
            print(f"{contador} notas de 20 reais")

    if total >= 10:
        contador = 0
        while total >= 10:
            contador = contador + 1
            total = total - 10
        if contador == 1:
            print(f"{contador} nota de 10 reais")
        else:
            print(f"{contador} notas de 10 reais")

    if total >= 5:
        contador = 0
        while total >= 5:
            contador = contador + 1
            total = total - 5
        if contador == 1:
            print(f"{contador} nota de 5 reais")
        else:
            print(f"{contador} notas de 5 reais")

    if total >= 2:
        contador = 0
        while total >= 2:
            contador = contador + 1
            total = total - 2
        if contador == 1:
            print(f"{contador} nota de 2 reais")
        else:
            print(f"{contador} notas de 2 reais")

    if total >= 1:
        contador = 0
        while total >= 1:
            contador = contador + 1
            total = total - 1
            if contador == 1:
                print(f"{contador} nota de 1 real")
            else:
                print(f"{contador} notas de 1 real")

    exit()


produtos = {}
inserir()
carrinho()

