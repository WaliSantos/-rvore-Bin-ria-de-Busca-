from estrutura_da_árvore.estrutura import ArvoreBinariaBusca, no
from busca import Busca 


def Inclusao(chave, raiz):
    if raiz == None:
        novo = no()
        novo.valor = chave 
        novo.esq = None 
        novo.dir = None 
        raiz = novo 
    else:
        pont = raiz 
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
    return raiz 






