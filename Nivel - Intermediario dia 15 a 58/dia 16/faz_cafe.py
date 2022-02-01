''' Faz o cafe da maquina '''

class FazCafe:
    """Modelo de pedido da maquian de cafe"""
    def __init__(self):
        self.recursos = {
            "agua": 300,
            "leite": 200,
            "cafe": 100,
        }

    def relatorio(self):
        """Imprimi os recuros disponiveis na maquina."""
        print(f"agua: {self.recursos['agua']}ml")
        print(f"leite: {self.recursos['leite']}ml")
        print(f"cafe: {self.recursos['cafe']}g")

    def ingredientes_suficientes(self, bebida):
        """Verifica se tem ingredientes suficientes"""
        pode_fazer = True
        for item in bebida.ingredientes:
            if bebida.ingredientes[item] > self.recursos[item]:
                print(f"Desculpa não temos recursos para fazer: {item}.")
                pode_fazer = False
        return pode_fazer

    def faz_cafe(self, pedido):
        """Faz o cafe e reduz a quantidade de recursos"""
        for item in pedido.ingredientes:
            self.recursos[item] -= pedido.ingredientes[item]
        print(f"Aqui está o seu {pedido.nome} ☕️. Aproveite!")
