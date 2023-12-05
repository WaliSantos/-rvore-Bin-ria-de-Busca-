
class no:
    def __init__(self):
        self.valor = 0
        self.esq = None
        self.dir = None
        self.prox = None 
        self.ant = None

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

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
    
    def Inclusao(self, chave):
        if self.raiz == None:
            novo = no()
            novo.valor = chave 
            novo.esq = None 
            novo.dir = None 
            self.raiz = novo 
        else:
            pont = self.raiz 
            pont, f,pai = Busca(pont,chave)
            if f==1:
                print("Elemento existe")
            else:
                novo = no()
                novo.valor = chave 
                novo.esq = None 
                novo.dir = None 
                if f==2:
                    pont.esq = novo 
                else:
                    pont.dir = novo 
        return self.raiz 
    def Busca(pont, chave, pai=None):
        if pont.valor == chave:
            f = 1
        else:
            if chave<pont.valor:
                if pont.esq == None:
                    f = 2
                else:
                    pai = pont
                    pont = pont.esq
                    pont,f, pai = Busca(pont, chave,pai)
            else:
                if pont.dir == None:
                    f = 3
                else:
                    pai = pont
                    pont = pont.dir
                    pont,f, pai = Busca(pont,chave,pai)
        return pont, f, pai
    
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

    def imprimir_arvore(self, no, nivel=0, lado=None):
        if no != None:
            self.imprimir_arvore(no.esq, nivel + 1, 'E')
            print(' ' * 7 * nivel + f'{no.valor} ({lado})')
            self.imprimir_arvore(no.dir, nivel + 1, 'D')

def Busca(pont, chave, pai=None):
    if pont.valor == chave:
        f = 1
    else:
        if chave<pont.valor:
            if pont.esq == None:
                f = 2
            else:
                pai = pont
                pont = pont.esq
                pont,f, pai = Busca(pont, chave,pai)
        else:
            if pont.dir == None:
                f = 3
            else:
                pai = pont
                pont = pont.dir
                pont,f, pai = Busca(pont,chave,pai)
    return pont, f, pai