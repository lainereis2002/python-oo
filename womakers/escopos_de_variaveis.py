bebida = 'refrigerante' #variavel global

def cardapio():
    global bebida #para alteral a variavel global pela variavel local
    comida = 'hamburguer'
    bebida = 'suco' #nova variavel local -> variavel que altera a global
    print('comida:', comida)
    print('bebida:', bebida) #printa suco

cardapio()  
#cardapio(comida) -> esse print dá errado, pois comida só está declarado dentro do cardapio
print('bebida:', bebida) #printa refrigerante -> printa suco

