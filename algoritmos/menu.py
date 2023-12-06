from estrutura_da_árvore.estrutura import ArvoreBinariaBusca

arvore = ArvoreBinariaBusca()
opcao = 0

print("Ual! Muito bom ter você por aqui! Vamos aprender sobre árvores binárias de busca?!")
while opcao != "5":
    
    print("\nMenu:")
    print("   Selecione uma das opções abaixo:")
    print("1. Inclusão")
    print("2. Exclusão")
    print("3. Caminhamento Pré-ordem")
    print("4. Mostrar Árvore")
    print("5. Fim")

    opcao = input("Digite uma das opções acima: ")

    if opcao == "1":
        valor = input("Insira o valor que deseja incluir: ")
        raiz, confere = arvore.Inclusao(int(valor))
        if confere == False:
            print("Seu valor foi incluído na árvore com sucesso!")
    elif opcao == "2":
        valor = input("Insira o valor que deseja excluir: ")
        confere = arvore.Exclusao(int(valor))
        if confere:
            print("Seu valor foi excluído na árvore com sucesso!")
    elif opcao == "3":
        print("Abaixo está o seu caminhamento pré-ordem: ")
        arvore.Pre_Ordem()
    elif opcao == "4":
        print("Abaixo está a estrutura da sua árvore: ")
        print(" ")
        arvore.imprimir_arvore(arvore.raiz)
        print(" ")
        print("Leia a árvore da esquerda para direita, conforme a seta -->.")
        print("Para cada nó, entre parênteses, está a corrêspondecia se o respectivo nó é filho direito (D) ou esquerdo (E).Ex.: 50 (E) é filho esquerdo de seu pai ")
        print(" Para cima, estão as sub-árvores esquerda. Para baixo, estão as sub-árvores direita. ")
    elif opcao == "5":
        print(" O seu programa foi encerrado! Que pena, gostaria de você aqui para continuarmos aprendendo. Até a próxima!")

