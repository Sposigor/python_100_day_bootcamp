''' Menu da maquina de cafe '''


class MenuItem:
    """Modelo menu"""
    def __init__(self, nome, agua, leite, cafe, custo):
        self.nome = nome
        self.custo = custo
        self.ingredientes = {
            "agua": agua,
            "leite": leite,
            "cafe": cafe
        }


class Menu:
    """Modelo dos items do menu"""
    def __init__(self):
        self.menu = [
            MenuItem(nome="latte", agua=200, leite=150, cafe=24, custo=2.5),
            MenuItem(nome="expresso", agua=50, leite=0, cafe=18, custo=1.5),
            MenuItem(nome="cappuccino", agua=250, leite=50, cafe=24, custo=3),
        ]

    def get_item(self):
        """Retorna o nome dos items do menu"""
        opcoes = ""
        for item in self.menu:
            opcoes += f"{item.nome}/"
        return opcoes

    def encontrar_bebida(self, ordem_nome):
        """Procura o item no menu"""
        for item in self.menu:
            if item.nome == ordem_nome:
                return item
        print("Desculpe não temos esse item no menu")
