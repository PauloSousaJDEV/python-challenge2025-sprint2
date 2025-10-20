lista_pessoas = []

def CadastrarPessoas():
    nome_pessoa = str(input("Digite o nome: "))
    idade_pessoa = str(input("Digite a idade: "))    
    pessoa = [nome_pessoa, idade_pessoa]
    lista_pessoas.append(pessoa)

def ListasPessoas():
    for c in lista_pessoas:
        print(f"Nome: {lista_pessoas[c][c]}, idade: {lista_pessoas[c][c]}")

def InteracaoMenu():
    print("Escolha uma opção do menu: ")
    print("1 - Cadastrar pessoa")
    print("2 - Listas pessoas cadastradas")
    print("0 - Sair do sistema")
    opcao_selecionada = int(input("Digite uma opção do menu: "))
    return opcao_selecionada

def IniciarSistema():
    opcao_menu = 1
    while opcao_menu != 0:
        opcao_menu = InteracaoMenu()
        match opcao_menu:
            case 1:
                CadastrarPessoas()
            case 2:
                ListasPessoas()
            case _:
                print("Opção inválida. Tente novamente")

IniciarSistema()
print("Sistema encerrado")