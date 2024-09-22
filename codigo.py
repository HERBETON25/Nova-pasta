livros = [
    {"codigo": 1, "autor": "Robert", "titulo": "Arquitetura Limpa", "preco": 100, "estoque": 3, "disponivel": True},
]

clientes = [
    # {"codigo": 1, "nome": "Herbeton", "telefone": 85900001111}
]
carrinho_de_compras = []
compras_finalizadas = []

codigo_livro = 1

codigo_cliente = 0

codigo_pedido = 0



# Funções para os livros
def cadastrar_livro():
    global codigo_livro
    nome_livro = input("Digite o nome do livro: ")
    autor_livro = input("Digite o nome do autor do livro: ").lower()
    preco_livro = float(input("Digite o preço do livro: "))
    estoque_livro = int(input("Digite o estoque do livro: "))
    codigo_livro += 1
    livro_novo = {"codigo": codigo_livro, "autor": autor_livro, "titulo": nome_livro, "preco": preco_livro, "estoque": estoque_livro, "disponivel": True}
    livros.append(livro_novo)
    print("Livro Cadastrado com sucesso")
    print('-'*50)


def exibir_livro():
    global livros
    for livro in livros:
        print(f"Codigo: {livro['codigo']}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Preço: {livro['preco']}")
        print(f"Estoque: {livro['estoque']}")
        print(f"Disponibilidade: {livro['disponivel']}")
        print('-'*50)


def editar_livro():
    global livros
    codigo = int(input("Informe o codigo do livro: "))
    for livro in livros:
        if livro['codigo'] == codigo:
            livro['titulo'] = input("Digite o nome do livro: ")
            livro['autor'] = input("Digite o nome do autor do livro: ")
            livro['preco'] = float(input("Digite o preço do livro: "))
            print("Dados alterados com sucesso")
            print('-'*50)
            break


def editar_estoque_livro():
    global livros
    codigo = int(input("Informe o codigo do livro: "))
    for livro in livros:
        if livro['codigo'] == codigo:
            livro['estoque'] = int(input("Digite a quantidade atual do livro em estoque: "))
            print(f'Você adicionou mais {codigo} ao seu Estoque!')
            print('-'*50)
            break


def pesquisar_livro():
    global livros
    codigo = int(input("Informe o codigo do livro: "))
    for livro in livros:
        if livro['codigo'] == codigo:
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Preço: {livro['preco']}")
            print(f"Estoque: {livro['estoque']}")
            print(f"Disponibilidade: {livro['disponivel']}")
            print('-'*50)


def mudar_disponibilidade_livro():
    global livros
    codigo = int(input("Informe o codigo do livro: "))
    for livro in livros:
        if livro['codigo'] == codigo:
            livro['disponivel'] = not livro['disponivel']
        break


def desconto_livro():
    global livros
    codigo = int(input("Informe o codigo do livro: "))
    desconto = int(input("Qual a porcentagem de desconto no livro: "))
    for livro in livros:
        if livro['codigo'] == codigo:
            livro['preco'] = livro['preco'] - (livro['preco'] * (desconto/100))
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Preço: {livro['preco']}")
            print(f"Estoque: {livro['estoque']}")
            print(f"Disponibilidade: {livro['disponivel']}")
            print('-'*50)
        break


def buscar_autor():
    global livros
    autor = input("Informe o autor do livro: ").lower()
    for livro in livros:
        if livro['autor'] == autor:
            print(f"Codigo: {livro['codigo']}")
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Preço: {livro['preco']}")
            print(f"Estoque: {livro['estoque']}")
            print(f"Disponibilidade: {livro['disponivel']}")
            print('-'*50)


def filtrar_preco():
    global livros
    filtro_preco = float(input("Qual o preço que deseja filtrar: "))
    escala = input(f"Filtrar por preços 'mais' ou 'menos' que {filtro_preco}: ").lower()
    if escala == "mais":
        for livro in livros:
            if livro['preco'] >= filtro_preco:
                print(f"Código: {livro['codigo']}")
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Preço: {livro['preco']}")
                print(f"Estoque: {livro['estoque']}")
                print(f"Disponibilidade: {livro['disponivel']}")
                print('-' * 50)
            else:
                print("Livro não encontrado nesses parametros")
                print('-' * 50)

    elif escala == "menos":
        for livro in livros:
            if livro['preco'] <= filtro_preco:
                print(f"Código: {livro['codigo']}")
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Preço: {livro['preco']}")
                print(f"Estoque: {livro['estoque']}")
                print(f"Disponibilidade: {livro['disponivel']}")
                print('-' * 50)
            else:
                print("Livro não encontrado nesses parametros")
                print('-' * 50)
    else:
        print("Opção invalida, tente novamente")


# Funções para os clientes
def cadastrar_cliente():
    global codigo_cliente
    nome_cliente = input("Digite o nome do cliente: ")
    telefone_cliente = int(input("Digite o telefone do cliente: "))
    codigo_cliente += 1
    cliente_novo = {"codigo": codigo_cliente, "nome": nome_cliente, "telefone": telefone_cliente}
    clientes.append(cliente_novo)
    print("Cliente Cadastrado com sucesso")
    print('-'*50)


def listar_clientes():
    global clientes
    for cliente in clientes:
        print(f"Codigo: {cliente['codigo']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Telefone: {cliente['telefone']}")
        print('-'*50)


def realizar_venda():
    global livros
    global clientes
    venda_livro = int(input("Informe o codigo do livro: "))
    for livro in livros:
        if livro['codigo'] == venda_livro and livro['disponivel']:
            venda_qnt = int(input("Informe a quantos livros deseja comprar: "))
            if livro['estoque'] >= venda_qnt:
                
                venda_cliente = int(input("Informe o codigo do cliente: "))
                for cliente in clientes:
                    #visualizar erro no print abaixo

                    if  cliente['codigo'] == venda_cliente :
                        while True:
                            print('1 - colocar item no carrinho: ')
                            print('2 - Finalizar a compra: ')
                            escolha = int(input('Escolha uma opcao: '))
                            if escolha == 1:
                                carrinho = {"codigo": codigo_cliente, "nome": cliente['nome'], "telefone": cliente['telefone'],"quantidade": venda_qnt,"livro": livro['titulo'],"preco_total": venda_qnt * livro['preco']}
                                carrinho_de_compras.append(carrinho)
                                print("Item inserido no carrinho com sucesso")
                                print('-' * 50)
                                break
                            elif escolha == 2:
                                print(f"Livro: {livro['titulo']}")
                                print(f"Cliente: {cliente['nome']}")
                                print(f"Quantidade: {venda_qnt}")
                                print(f"Preço total: {venda_qnt * livro['preco']}")
                                livro['estoque'] -= venda_qnt # efetuado a compra
                                vendaFinalizada = {"codigo": codigo_cliente, "nome": cliente['nome'], "telefone": cliente['telefone'],"quantidade": venda_qnt,"livro": livro['titulo'],"preco_total": venda_qnt * livro['preco']}
                                compras_finalizadas.append(vendaFinalizada)
                                print("Venda realizada com sucesso")
                                print('-' * 50)
                                break
                            else:
                                print('Opção invalida!')
                    else:
                        

                        print("Cliente não encontrado")
                        print("A compra foi cancelada!")
                        print('-' * 50)
                        break
            else:
                print("Não há estoque suficiente para essa venda")
                print('-' * 50)
                break
        else:
            print("Livro não encontrado")
            print('-' * 50)

# ------------------------------------------------------------------------------------------------
# Função para voltar para o menu inicial ( BETO )
def voltar_menu():
    print("Voltando ao menu inicial...")
    print('-' * 50)
    main()

# MENU PRINCIPAL ( BETO )
def main():
    while True:
        print("--- Bem-vindo a Biblioteca ---")
        print("1 - Livros")
        print("2 - Clientes")
        print("3 - Carrinho de compras")
        print("4 - Historico de Compras")
        print("0 - Encerrar Progama")
        print('-' * 50)
        opcao = input("Selecione uma opção: ")
        opcoes = {
            "1": biblioteca,
            "2": vendas,
            "3": carrinho,
            "4": historico,
            
            
        }
        if opcao == "0":
            break
        elif opcao in opcoes:
            opcoes[opcao]()
        else:
            print("Opção invalida,tente novamente")

# AREA DE CADASTRO DE LIVROS ( BETO )
def biblioteca():
    while True:
        print("--- BIBLIOTECA ----")
        print("1 - Cadastrar Livro")
        print("2 - Exibir todos os  Livros")
        print("3 - Editar Livro")
        print("4 - Alterar estoque do Livro")
        print("5 - Pesquisar Livro por codigo")
        print("6 - Alterar a disponibilidade do Livro")
        print("7 - Aplique desconto no valor do Livro")
        print("8 - Busque o Livro pelo autor")
        print("9 - Filtrar por preços")
        print("0 - Voltar ao Menu Inicial")
        print('-' * 50)
        opcao = input("Selecione uma opção: ")
        opcoes = {
            "1": cadastrar_livro,
            "2": exibir_livro,
            "3": editar_livro,
            "4": editar_estoque_livro,
            "5": pesquisar_livro,
            "6": mudar_disponibilidade_livro,
            "7": desconto_livro,
            "8": buscar_autor,
            "9": filtrar_preco,
            "0": voltar_menu,
        }
        if opcao in opcoes:
            opcoes[opcao]()
        else:
            print("Opção invalidada,tente novamente")

# area do cliente ( BETO )
def vendas():
    while True:
        print(" ----- MENU DO CLIENTE ----- ")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Realizar Venda")
        print("0 - Voltar ao Menu Inicial")
        print('-' * 50)
        opcao = input("Selecione uma opção: ")
        opcoes = {
            "1": cadastrar_cliente,
            "2": listar_clientes,
            "3": realizar_venda,
            "0": voltar_menu,
        }
        if opcao in opcoes:
            opcoes[opcao]()
        else:
            print("Opção invalidada,tente novamente")

# area carrinho
def carrinho():
    global carrinho_de_compras
    print("---------carrinho de compras-----")
    for listaC in carrinho_de_compras:
        
        print(f"Codigo: {listaC['codigo']}")
        print(f"Nome: {listaC['nome']}")
        print(f"Telefone: {listaC['telefone']}")
        print(f"Quantidade: {listaC['quantidade']}")
        print(f"Livro: {listaC['livro']}")
        print(f"Preço Total R$:{listaC['preco_total']}")
        print('-'*50)
    while True:
        print("1 - finalizar uma compra: ")
        print("2 - voltar ao menu principra")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            codigo = int(input("Digite o codigo do cliente: "))
            for lista in carrinho_de_compras:
                if lista['codigo'] == codigo:
                    re_enviar = lista
                    carrinho_de_compras.remove(lista)
                    compras_finalizadas.append(re_enviar)
                    print("Compra do carrinho finalizada Com sucesso!")
                    print('-'*50)
                    break
                else:
                    print("Livro não encontrado")
                    break
        elif opcao == 2:
            voltar_menu()
# def historico():
def historico():
    global compras_finalizadas
    print("---------HISTORICO DE COMPRAS REALIZADAS-----")
    for lista in compras_finalizadas:
        
        print(f"Codigo: {lista['codigo']}")
        print(f"Nome: {lista['nome']}")
        print(f"Telefone: {lista['telefone']}")
        print(f"Quantidade: {lista['quantidade']}")
        print(f"Livro: {lista['livro']}")
        print(f"Preço Total R$:{lista['preco_total']}")
        print('-'*50)
   


#VOLTAR AO MENU ( BETO )
main()