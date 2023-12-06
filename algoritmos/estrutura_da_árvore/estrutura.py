
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
        confere = False
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
                print("Elemento Já foi incluído. Coloque outro, por gentileza!")
                confere = True
            else:
                novo = no()
                novo.valor = chave 
                novo.esq = None 
                novo.dir = None 
                if f==2:
                    pont.esq = novo 
                else:
                    pont.dir = novo 
        return self.raiz,confere
    def Exclusao(self, chave):
        confere = True
        pont, f, pai = Busca(self.raiz,chave)
        if f==1:
            if pont.esq == None:
                if pont == self.raiz:
                    self.raiz = self.raiz.dir
                else:
                    if pont == pai.esq:
                        pai.esq = pont.dir
                    else:
                        pai.dir = pont.dir
            else:
                if pont.dir == None:
                    if pont == self.raiz:
                        self.raiz = self.raiz.esq
                    else:
                        if pont == pai.esq:
                            pai.esq = pont.esq
                        else:
                            pai.dir = pont.esq
                else:
                    pont2 = pont.dir 
                    pai2 = pont
                    while pont2.esq!=None:
                        pai2 = pont2
                        pont2 = pont2.esq
                    if pai2 != pont:
                        pai2.esq = pont2.dir
                        pont2.dir = pont.dir
                    pont2.esq = pont.esq
                    if pont == self.raiz:
                        self.raiz = pont2
                    else:
                        if pai.esq == pont:
                            pai.esq = pont2
                        else:
                            pai.dir = pont2
        else:
            confere = False
            print(" Não é possível excluir um elemento que não existe na árvore")
        del pont 
        return confere
    def Pre_Ordem(self):
        pont = self.raiz
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