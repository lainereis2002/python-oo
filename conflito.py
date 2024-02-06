from funcoes_do_log import *

imprimir_no_log(f'Bem vinda, {nome_de_usuario}') #aqui possui o [INFO]
print()

def imprimir_no_log(texto):
    print(texto)

imprimir_no_log(f'Bem vinda, {nome_de_usuario}') #aqui não possui [INFO]