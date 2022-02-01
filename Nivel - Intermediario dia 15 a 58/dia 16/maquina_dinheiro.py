''' Processo de validação e troco da maquina de cafe'''

class MaquinaDinheiro:
    ''' Classe que representa a maquina de dinheiro'''

    moeda = "R$"

    valores_moeda = {
        "25 centavos": 0.25,
        "10 centavos": 0.10,
        "5 centavos": 0.05,
        "1 centavo": 0.01
    }

    def __init__(self):
        self.carteira = 0
        self.dinheiro_recebido = 0

    def relatorio(self):
        """Imprimir o valor em carteira"""
        print(f"Dinheiro: {self.moeda}{self.carteira}")

    def processo_moeda(self):
        """Retorna o valor total de moedas recebidas"""
        print("Inserir o dinheiro.")
        for moeda in self.valores_moeda:
            self.dinheiro_recebido += int(input(f"Quantas {moeda}?: ")) * self.valores_moeda[moeda]
        return self.dinheiro_recebido

    def pagamento(self, custo):
        """ Retorna o se o pagamento é suficiente ou não e sim retorna o troco"""
        self.processo_moeda()
        if self.dinheiro_recebido >= custo:
            troco = round(self.dinheiro_recebido - custo, 2)
            print(f"Aqui está o seu troco {self.moeda} {troco}")
            self.carteira += custo
            self.dinheiro_recebido = 0
            return True
        else:
            print("Desculpe, valor insuficiente, aqui está seu dinheiro"
                    +f"{self.moeda}{self.dinheiro_recebido}.")
            self.dinheiro_recebido = 0
            return False
