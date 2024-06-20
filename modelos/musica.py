class Musica:
    musicas = []
    
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = int(duracao)
        Musica.musicas.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao} segundos')
         
print('Musicas')   
musica1 = Musica('who do you love', '5 seconds of summer', 300)
musica2 = Musica('espresso', 'sabrina carpenter', 250)
musica3 = Musica('g5 boucing', 'chris brown', 289)

Musica.listar_musicas()

class Carro:
    carros = []
    
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = int(ano)
        Carro.carros.append(self)
        
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo} | {carro.cor} | {carro.ano}')


print('Carros')
carro1 = Carro('chevet', 'vermelho', 1987)
carro2 = Carro('camaro', 'amarelo', 2012)
carro3 = Carro('hailux', 'prata', 2023)
Carro.listar_carros()
