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