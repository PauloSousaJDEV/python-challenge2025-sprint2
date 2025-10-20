lista_pessoas = []

def ServicoCadastrarPessoa():
    print("\n---------- CADASTRANDO PESSOA ----------\n")
    nome_pessoa = str(input("Digite o nome: "))
    idade_pessoa = int(input("Digite a idade: "))
    CadastrarPessoas(nome_pessoa, idade_pessoa)
    print(f"\nCadastro realizado com sucesso! Agora você tem um total de {len(lista_pessoas)} pessoa(s) cadastradas.\n")
    lista_opcoes = MostrarOpcoesDeVoltarAoMenu(1)
    opcao_esperada = int(input("Selecione o número da opção: "))
    opcao_selecionada = ValidaOpcaoSelecionadoMenu(1, lista_opcoes, opcao_esperada)
    
    match opcao_selecionada:
        case 1:
            ServicoCadastrarPessoa()
        case 2:
            print(f"\nVoltando ao menu de opções...\n")
            InteracaoMenu()

def CadastrarPessoas(nome_pessoa: str, idade_pessoa: int):
    id_pessoa = len(lista_pessoas) + 1
    pessoa = [id_pessoa, nome_pessoa, idade_pessoa]
    lista_pessoas.append(pessoa)

def ListarPessoas():
    if len(lista_pessoas) > 0:
        for c in lista_pessoas:
            print(f"ID: {c[0]}, Nome: {c[1]}, Idade: {c[2]}")
    else:
        print("Não há pessoas cadastradas.")
    
def EditarPessoa(id_pessoa: int):
    print("Lista de pessoas: ")

def InteracaoMenu():
    print("\n---------- MENU DE OPÇÕES ----------\n")
    print("1 - Cadastrar pessoa")
    print("2 - Listas pessoas cadastradas")
    print(f"0 - Sair do sistema\n")
    opcao_selecionada = int(input("Digite uma opção do menu: "))
    return opcao_selecionada

def ValidaOpcaoSelecionadoMenu(menu: int, lista_menu: list, opcao_selecionada: int):
    while not opcao_selecionada in lista_menu:
        print("\nOpção inválida. Digite um número entre as opções disponíveis.\n")
        MostrarOpcoesDeVoltarAoMenu(menu)
        opcao_selecionada = int(input("Selecione o número da opção: "))
    return opcao_selecionada

def MostrarOpcoesDeVoltarAoMenu(menu: int):
    match menu:
        case 1:
            lista_opcoes = [1,2]
            print(f"O que deseja fazer?\n")
            print(f"1 - Cadastrar outra pessoa")
            print(f"2 - Voltar ao menu\n")
            return lista_opcoes

def IniciarSistema():
    opcao_menu = 1
    while opcao_menu != 0:
        opcao_menu = InteracaoMenu()
        match opcao_menu:
            case 0:
                print("\nSaindo do sistema...\n")
            case 1:
                ServicoCadastrarPessoa()
            case 2:
                print("\n-- LISTA DE PESSOAS CADASTRADAS --\n")
                ListarPessoas()
                print(f"\nVoltando ao menu de opções...\n")

            case 3:
                print("\n---------- EDITANDO PESSOA ----------\n")
                ListarPessoas()

            case _:
                print("Opção inválida. Tente novamente")

IniciarSistema()
print("Sistema encerrado")