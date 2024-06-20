class Restaurante:
    restaurantes = []
    #p deixa como privado basta colocar um _
    def __init__(self, nome, categoria): #self == this == objeto
        self._nome = nome.title() #deixa a primeira letra de cada palavra maiúscula
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self): #isso aqui serve para transformar o endereço do obj em string
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alternar_status(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_status()
restaurante_pizza = Restaurante('pizzaiolo', 'Italiana')

Restaurante.listar_restaurantes()