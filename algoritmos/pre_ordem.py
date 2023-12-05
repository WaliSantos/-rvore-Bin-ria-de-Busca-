from estrutura_da_árvore.estrutura import  no

class Pilha:
    def __init__(self):
        self.topo = None
    def empilhar(self, chave):
        novo = no()
        novo.valor = chave 
        novo.prox = self.topo
        self.topo = novo
        return self.topo

    def desempilhar(self):
        if self.topo != None:
            valor_desempilhado = self.topo.valor
            aux = self.topo
            self.topo = self.topo.prox
            del aux
        else:
            print("Pilha vazia")
        return valor_desempilhado
    
def Pre_Ordem(arvore):
    pont = arvore.raiz
    if pont.valor == 0:
        print("Árvore vazia")
    else:
        pilha = Pilha()
        pilha.empilhar(pont)
        while pilha.topo is not None:
            pont = pilha.desempilhar()
            print(pont.valor, end=" ")
            if pont.dir != None:
                pilha.empilhar(pont.dir)
            if pont.esq != None:
                pilha.empilhar(pont.esq)