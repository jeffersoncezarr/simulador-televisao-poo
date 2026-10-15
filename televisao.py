from rich import print
from rich.panel import Panel

class Televisao:
    """
    Classe responsavel por criar uma televisão e suas funcoes...
    """
    canal_max = 5
    canal_min = 1

    vol_max = 5
    vol_min = 1

    @staticmethod
    def mensagem_desligada()-> str:
        return 'TELEVISÃO DESLIGADA!'

    @classmethod
    def mostra_canais(cls)-> None:
        todos_canais = [f'{canais:^5}' for canais in list(range(cls.canal_min, cls.canal_max + 1))]
        print('Canais mapeados:')
        print(' '.join(todos_canais))


    def __init__(self):
        self.__ligada = False
        self.__canal_atual = 2
        self.__vol_atual = 2


    def liga_desliga(self):
        self.__ligada = not self.__ligada

    @property
    def canal(self)-> int:
        return self.__canal_atual


    @canal.setter
    def canal(self, canal: int) -> None:
        if self.__ligada:
            if Televisao.canal_min <= canal <= Televisao.canal_max:
                self.__canal_atual = canal
            else:
                raise IndexError('Canal não encontrado!')
        else:
            Televisao.mensagem_desligada()


    def passa_canal(self)-> None:
        if self.__ligada:
            if self.__canal_atual == Televisao.canal_max:
                self.__canal_atual = Televisao.canal_min
            else:
                self.__canal_atual += 1
        else:
            Televisao.mensagem_desligada()


    def volta_canal(self)-> None:
        if self.__ligada:
            if self.__canal_atual == Televisao.canal_min:
                self.__canal_atual = Televisao.canal_max
            else:
                self.__canal_atual -= 1
        else:
            Televisao.mensagem_desligada()


    @property
    def volume(self)-> int:
        return self.__vol_atual


    @volume.setter
    def volume(self, vol):
        pass


    def aumenta_volume(self)-> None:
        if self.__ligada:
            if self.__vol_atual < Televisao.vol_max:
                self.__vol_atual += 1
        else:
            Televisao.mensagem_desligada()


    def diminui_volume(self):
        if self.__ligada:
            if self.__vol_atual > Televisao.vol_min:
                self.__vol_atual -= 1
        else:
            Televisao.mensagem_desligada()


    def mostra_tv(self):
        if self.__ligada:
            conteudo = f'{" ".join([f"[on blue]{canal:^5}[/]" if canal == self.__canal_atual else f"{canal:^5}" for canal in
                            range(Televisao.canal_min, Televisao.canal_max + 1)])}'

            conteudo += f'\n{"".join(["[red on red]   [/]" if volume <= self.__vol_atual else '[white on white]   [/]' for volume in range(Televisao.vol_min, Televisao.vol_max+1)])}'
            
        else:
            conteudo = f'[red]{Televisao.mensagem_desligada()}[/]'

        return Panel(conteudo, title='TELEVISÃO', title_align="center", width=60)
