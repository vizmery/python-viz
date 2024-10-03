import os

alunas = [{'nome':'vizmery', 'categoria':'estetica', 'ativo':True},
             {'nome':'romildo', 'categoria':'saude','ativo':True},
             {'nome':'geovana', 'categoria':'aluna','ativo':False},
             {'nome':'bixa', 'categoria':'Livre', 'ativo':True}]

def exbir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('')

def retorna_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()


def mostra_titulo():
    print('''
           
        ██╗░░░██╗███████╗  ░██████╗████████╗██╗░░░██╗██████╗░██╗░█████╗░
        ██║░░░██║╚════██║  ██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██║██╔══██╗
        ╚██╗░██╔╝░░███╔═╝  ╚█████╗░░░░██║░░░██║░░░██║██║░░██║██║██║░░██║
        ░╚████╔╝░██╔══╝░░  ░╚═══██╗░░░██║░░░██║░░░██║██║░░██║██║██║░░██║
        ░░╚██╔╝░░███████╗  ██████╔╝░░░██║░░░╚██████╔╝██████╔╝██║╚█████╔╝
        ░░░╚═╝░░░╚══════╝  ╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚═╝░╚════╝░
           
     ''')




def mostra_escolhas():
    print('1. Cadastro de aluna')
    print('2. Listar aluna')
    print('3. Ativar aluna')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_aluna()
        elif opcao_escolhida == 2:
            mostrar_aluna()
        elif  opcao_escolhida == 3:
            print('Ativar/desativar aluna')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_aluna():
    exbir_subtitulo('Cadastrar aluna')

    nome_aluna = input('Digite o nome da aluna: ')
    categoria = input(f'qual o curso {nome_aluna} prefere')
    dados_aluna = {'nome': nome_aluna, 'categoria':categoria, 'ativo':True}
    alunas.append(dados_aluna)
    print(f'{nome_aluna} foi adicionada a aluna')

    retorna_menu_principal()

def mostrar_aluna():
    exbir_subtitulo('Listar aluna')

    for aluna in aluna:
        nome_aluna = aluna['nome']
        categoria = alunas ['categoria']
        ativo = aluna['ativo']
        print(f' - {nome_aluna} | {categoria} | {ativo}')
    
    
    retorna_menu_principal()


def finalizar_programa():
    os.system('cls')
    print('Finalizando programa')

def opcao_invalida():
    print('Esse caracter não é permitido')
    retorna_menu_principal()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()