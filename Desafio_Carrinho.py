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
    print(f"Valor total : \n {total}")

    if total >= 100:
        contador = 0
        while total >= 100:
            contador = contador + 1
            total = total - 100
        if contador == 1:
            print(f"{contador} nota de 100")
        else:
            print(f"{contador} notas de 100")

    if total >= 50:
        contador = 0
        while total >= 50:
            contador = contador + 1
            total = total - 50
        if contador == 1:
            print(f"{contador} nota de 50")
        else:
            print(f"{contador} notas de 50")

    if total >= 20:
        contador = 0
        while total >= 20:
            contador = contador + 1
            total = total - 20
        if contador == 1:
            print(f"{contador} nota de 20")
        else:
            print(f"{contador} notas de 20")

    if total >= 10:
        contador = 0
        while total >= 10:
            contador = contador + 1
            total = total - 10
        if contador == 1:
            print(f"{contador} nota de 10")
        else:
            print(f"{contador} notas de 10")

    if total >= 5:
        contador = 0
        while total >= 5:
            contador = contador + 1
            total = total - 5
        if contador == 1:
            print(f"{contador} nota de 5")
        else:
            print(f"{contador} notas de 5")

    if total >= 2:
        contador = 0
        while total >= 2:
            contador = contador + 1
            total = total - 2
        if contador == 1:
            print(f"{contador} nota de 2")
        else:
            print(f"{contador} notas de 2")

    if total >= 1:
        contador = 0
        while total >= 1:
            contador = contador + 1
            total = total - 1
            if contador == 1:
                print(f"{contador} nota de 1")
            else:
                print(f"{contador} notas de 1")

    exit()


produtos = {}
inserir()
carrinho()

