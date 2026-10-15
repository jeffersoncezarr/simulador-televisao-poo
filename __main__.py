from televisao import Televisao
from  pilha import  Pilha
from controle_remoto import ControleRemoto
from rich import print

def leia_int(txt):
   while True:
       try:
           num = str(input(txt))
           num = int(num)
       except (TypeError, ValueError):
           print('Digite um número válido!')
       else:
           return num


def main():
    try:
        tv = Televisao()
        pilha_1 = Pilha()
        controle = ControleRemoto(tv, pilha_1)

        while True:
            print(tv.mostra_tv())
            opcoes = str(input('+ VOL - | < CH > | [ @ ] [ = ]  '))
            match opcoes:
                case '@':
                    controle.botao_power()
                case '+':
                    controle.volume_mais()
                case '-':
                    controle.volume_menos()
                case '<':
                    controle.canal_menos()
                case '>':
                    controle.canal_mais()
                case '=':
                    try:
                        c = leia_int('CANAL: ')
                        controle.input_canal(c)
                    except Exception as err:
                        print(f'[red]{err.__class__.__name__}: {err}[/]')

                case '0':
                    break
                case _:
                    print('OPÇÃO INVALIDA!')

    except Exception as err:
        print(f'{err.__class__.__name__}: {err}')

if __name__ == '__main__':
    main()