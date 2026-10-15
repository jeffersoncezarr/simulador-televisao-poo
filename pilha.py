class Pilha:
    """
    Classe responsavel por Criar Pilhas(Baterias) que fornecem energia a dispositivos eletronicos...
    """
    def __init__(self, energia: int=100):
        self.__energia = energia


    def consumir_energia(self, qtd=1):
        if self.__energia > 0:
            self.__energia -= qtd
            return True
        return False