class ContaBancaria:
    contas = []
    
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo)
        self._ativo = False
        ContaBancaria.contas.append(self)
    
    def __str__(self):
        return f'{self.titular} | R$ {self.saldo}'
    
    @classmethod
    def listar_contas(cls):
        print(f'{"Nome do Titular".ljust(20)} | {"Saldo em R$".ljust(23)} | Status')
        for conta in ContaBancaria.contas:
            saldo_formatado = f"{conta.saldo:.2f}"
            saldo_alinhado = saldo_formatado.ljust(20)
            print(f'{conta.titular.ljust(20)} | R$ {saldo_alinhado} | {conta.ativo}')

    def ativar_conta(self):
        self._ativo = not self._ativo
    
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta
        
    
conta1 = ContaBancaria('Gislaine Reis', 2000.56)
conta2 = ContaBancaria('Gilmara Brandao', 200000.65)
conta3 = ContaBancaria('Franklin Reis', 1000000.76)

ContaBancaria.listar_contas()
conta3.ativar_conta()
print()
ContaBancaria.listar_contas()

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

