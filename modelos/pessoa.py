class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = int(idade)
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e trabalha como {self.profissao}.'
    
    
    def aniversario(self):
        self.idade +=1
    
    @property
    def saudacao(self):
        return f'''Ooi pessoal, me chamo {self.nome} e tenho {self.idade}. Adoro escutar música e adoro sentir o cheiro de grama molhada!'''

pessoa1 = Pessoa('Gislaine', 22, 'estagiária')

print(pessoa1)
print()
print(pessoa1.saudacao)
pessoa1.aniversario()
print()
print(pessoa1)

    