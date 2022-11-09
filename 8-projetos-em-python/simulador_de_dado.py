import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor?'

    def Iniciar(self):
        resposta = input(self.mensagem)   
        if resposta == 'Sim' or 'S':
            self.GerarValorDoDado()
        elif resposta == 'Não' or 'N':
            print('O usuário decidiu não digitar, encerrando programa.')
        else:
            print('Por favor, digite apenas SIM ou NÃO.')    

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))    

simulador = SimuladorDeDado()
simulador.Iniciar()