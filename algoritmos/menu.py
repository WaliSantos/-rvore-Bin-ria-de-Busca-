from inclusao import Inclusao
from pre_ordem import Pre_Ordem
from busca import Busca
from estrutura_da_árvore.estrutura import ArvoreBinariaBusca


def Exclusao(raiz, chave): 
    pont, f, pai = Busca(raiz,chave)
    if f==1:
        if pont.esq == None:
            if pont == raiz:
                raiz = raiz.dir
            else:
                if pont == pai.esq:
                    pai.esq = pont.dir
                else:
                    pai.dir = pont.dir
        else:
            if pont.dir == None:
                if pont == raiz:
                    raiz = raiz.esq
                else:
                    if pont == pai.esq:
                        pai.esq = pont.esq
                    else:
                        pai.dir = pont.esq
            else:
                pont2 = pont.dir 
                pai2 = pont
                while pont2.esq!=None:
                    pai = pont2
                    pont2 = pont2.esq
                if pai2!=pont:
                    pai2.esq = pont2.dir
                    pont2.dir = pont.dir
                pont2.esq = pont.esq
                if pont == raiz:
                    raiz = pont2
                else:
                    if pai.esq == pont:
                        pai.esq = pont2
                    else:
                        pai.dir = pont2
    del pont


# Criando uma instância da árvore binária de busca
arvore = ArvoreBinariaBusca()

arvore.Inclusao(45)
arvore.Inclusao(30)
arvore.Inclusao(15)
arvore.Inclusao(70)
arvore.Inclusao(60)
arvore.Inclusao(20)
arvore.Inclusao(40)
arvore.Inclusao(65)
arvore.Inclusao(100)
arvore.Inclusao(90)
arvore.Inclusao(35)


# Exibindo a árvore para verificar os valores incluídos
print("Árvore Binária de Busca:")

arvore.imprimir_arvore(arvore.raiz)
