from televisao import  Televisao
from pilha import Pilha

class ControleRemoto:
    def __init__(self, televisao, pilha):
        self.__televisao = televisao
        self.__pilha = pilha


    def botao_power(self):
        if self.__pilha.consumir_energia():
            self.__televisao.liga_desliga()


    def canal_mais(self):
        if self.__pilha.consumir_energia():
            self.__televisao.passa_canal()


    def canal_menos(self):
        if self.__pilha.consumir_energia():
            self.__televisao.volta_canal()



    def volume_mais(self):
        if self.__pilha.consumir_energia():
            self.__televisao.aumenta_volume()


    def volume_menos(self):
        if self.__pilha.consumir_energia():
            self.__televisao.diminui_volume()


    def input_canal(self, canal):
        if self.__pilha.consumir_energia():
            self.__televisao.canal = canal