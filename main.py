import re

lista_pessoas = []

def ServicoCadastrarPessoa():
    print("\n---------- CADASTRANDO PESSOA ----------\n")
    nome_pessoa = str(input("Digite o nome: "))
    idade_pessoa = int(input("Digite a idade: "))
    cpf_pessoa = str(input("Digite o CPF: "))
    telefone_pessoa = str(input("Digite o telefone: "))

    if not ValidarCPF(cpf_pessoa):
        print("CPF inválido. Tente novamente.")
        return ServicoCadastrarPessoa()
    
    if not ValidarTelefone(telefone_pessoa):
        print("Telefone inválido. Tente novamente.")
        return ServicoCadastrarPessoa()
    
    CadastrarPessoas(nome_pessoa, idade_pessoa, cpf_pessoa, telefone_pessoa)
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

def ServicoListarPessoas():
    print("\n---- LISTA DE PESSOAS CADASTRADAS ----\n")
    ListarPessoas()
    print(f"\nVoltando ao menu de opções...\n")

def ServicoEditarPessoa():
    print("\n---------- EDITANDO PESSOA ----------\n")
    print("Lista de pessoas cadastradas: \n")
    ListarPessoas()
    id_selecionado = int(input("Digite o ID da pessoa a ser editada: "))
    valor_atual = ExibirPessoa(id_selecionado)

    novo_nome = str(input("Digite o novo nome: "))
    novo_idade = str(input("Digite a nova idade: "))
    novo_cpf = str(input("Digite o novo CPF: "))
    novo_telefone = str(input("Digite o novo telefone: "))
    pessoa_editada = EditarPessoa(id_selecionado, novo_nome, novo_idade, novo_cpf, novo_telefone)

    print("ANTES\n")
    print(f"ID: {valor_atual[0]}, Nome: {valor_atual[1]}, Idade: {valor_atual[2]}, CPF: {valor_atual[3]}, Telefone: {valor_atual[4]}\n")

    print("DEPOIS\n")
    print(f"ID: {pessoa_editada[0]}, Nome: {pessoa_editada[1]}, Idade: {pessoa_editada[2]}, CPF: {pessoa_editada[3]}, Telefone: {pessoa_editada[4]}")

    print(f"\Edição realizada com sucesso! Retornando ao menu de opções...\n")
    InteracaoMenu()

def CadastrarPessoas(nome_pessoa: str, idade_pessoa: int, cpf_pessoa: str, telefone_pessoa: str):
    id_pessoa = len(lista_pessoas) + 1
    pessoa = [id_pessoa, nome_pessoa, idade_pessoa, cpf_pessoa, telefone_pessoa]
    lista_pessoas.append(pessoa)

def ListarPessoas():
    if len(lista_pessoas) > 0:
        for c in lista_pessoas:
            print(f"ID: {c[0]}, Nome: {c[1]}, Idade: {c[2]}, CPF: {c[3]}, Telefone: {c[4]}")
    else:
        print("Não há pessoas cadastradas.")

def ValidarCPF(cpf: str) -> bool:
    return bool(re.fullmatch(r"\d{11}", cpf))

def ValidarTelefone(telefone: str) -> bool:
    return bool(re.fullmatch(r"\d{10,11}", telefone))

def ExibirPessoa(id_pessoa):
    indice_pessoa = id_pessoa - 1
    pessoa_selecionada = lista_pessoas[indice_pessoa]
    print(f"ID: {pessoa_selecionada[0]}, Nome: {pessoa_selecionada[1]}, Idade: {pessoa_selecionada[2]}")
    return pessoa_selecionada

def EditarPessoa(id_pessoa: int, nome: str, idade: int, cpf: str, telefone: str):
    indice_pessoa = id_pessoa - 1
    lista_pessoas[indice_pessoa][1] = nome
    lista_pessoas[indice_pessoa][2] = idade
    lista_pessoas[indice_pessoa][3] = cpf
    lista_pessoas[indice_pessoa][4] = telefone
    pessoa_selecionada = lista_pessoas[indice_pessoa]
    return pessoa_selecionada

def InteracaoMenu():
    print("\n---------- MENU DE OPÇÕES ----------\n")
    print("1 - Cadastrar pessoa")
    print("2 - Listas pessoas cadastradas")
    print("3 - Editar pessoa")
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
                break
            case 1:
                ServicoCadastrarPessoa()
            case 2:
                ServicoListarPessoas()
            case 3:
                ServicoEditarPessoa()
            case _:
                print("Opção inválida. Tente novamente")

IniciarSistema()

print("Sistema encerrado")