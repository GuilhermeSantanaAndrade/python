# classe Dominó
class Domino:
    ponta1 = 0
    ponta2 = 0
    def __init__(self, ponta1, ponta2):
        self.ponta1 = ponta1
        self.ponta2 = ponta2
 
    def encaixa(self, outro):
        return (self.ponta2 == outro.ponta1) or (self.ponta2 == outro.ponta2) 
   
    def duplo(self):
        return (self.ponta1 == self.ponta2)
    
    def valida(self):
        rg = range(0,6)
        if (self.ponta1 not in rg):
            raise ValueError('Valor inválido para Ponta1')
        if (self.ponta2 not in rg):
            raise ValueError('Valor inválido para Ponta2')
 
    def mostra(self):
        return '{ponta1: '+ str(self.ponta1) +', ponta2: '+ str(self.ponta2) +'}'

    def gira(self):
        aux = self.ponta1
        self.ponta1 = self.ponta2
        self.ponta2 = aux
    
peca_1 = Domino(0,5)
peca_1.valida()

peca_2 = Domino(3,5)
peca_2.valida()

print('Peça 1 e 2 encaixam? ----->', peca_1.encaixa(peca_2))
print('Peça 1 é dupla? ----->', peca_1.duplo())
print('Peça 2 é dupla? ----->', peca_2.duplo())
