''' Maquina de café com opções de escolha de café, leite e chocolate '''
MENU = {
    "expresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "custo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leite": 150,
            "cafe": 24,
        },
        "custo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leite": 100,
            "cafe": 24,
        },
        "custo": 3.0,
    }
}

carteira = 0
recursos = {
    "agua": 300,
    "leite": 200,
    "cafe": 100,
}


def recursos_suficentes(ingredientes_ordenados):
    """Retorna se os recursos são suficientes para a preparação do café."""
    for item in ingredientes_ordenados:
        if ingredientes_ordenados[item] > recursos[item]:
            print(f"​Desculpa não temos ingredientes para fazer {item}.")
            return False
    return True


def moedas():
    """Retorna o valor da moeda inserida pelo usuário."""
    print("Insira as moedas.")
    total = int(input("25 centavos?: ")) * 0.25
    total += int(input("10 centavos?: ")) * 0.1
    total += int(input("5 centavos?: ")) * 0.05
    total += int(input("1 centavos?: ")) * 0.01
    return total


def pagamento_efetuado(dinheiro_recebido, custo_do_cafe):
    """Retorna se possui valor suficiente para compra o cafe e devolve o troco."""
    if dinheiro_recebido >= custo_do_cafe:
        troco = round(dinheiro_recebido - custo_do_cafe, 2)
        print(f"Aqui está seu troco R${troco}.")
        global carteira
        carteira += custo_do_cafe
        return True
    else:
        print("Desculpa, dinheiro insuficiente.")
        return False


def faz_cafe(nome_bebida, ingredientes_ordenados):
    """Dedução de recursos e pagamento."""
    for item in ingredientes_ordenados:
        recursos[item] -= ingredientes_ordenados[item]
    print(f"Aqui está a sua {nome_bebida} ☕️. Aproveite!")


continua = True

while continua:
    escolha = input("​O que você quer? (expresso/latte/cappuccino): ")
    if escolha == "desligar":
        continua = False
    elif escolha == "relatorio":
        print(f"agua: {recursos['agua']}ml")
        print(f"leite: {recursos['leite']}ml")
        print(f"cafe: {recursos['cafe']}g")
        print(f"Dinheiro: ${carteira}")
    else:
        bebida = MENU[escolha]
        if recursos_suficentes(bebida["ingredientes"]):
            pagamento = moedas()
            if pagamento_efetuado(pagamento, bebida["custo"]):
                faz_cafe(escolha, bebida["ingredientes"])
