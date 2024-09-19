import os

alunas = []


def mostra_titulo():
    print('''
            
        ██╗░░░██╗███████╗  ░██████╗████████╗██╗░░░██╗██████╗░██╗░█████╗░
        ██║░░░██║╚════██║  ██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██║██╔══██╗
        ╚██╗░██╔╝░░███╔═╝  ╚█████╗░░░░██║░░░██║░░░██║██║░░██║██║██║░░██║
        ░╚████╔╝░██╔══╝░░  ░╚═══██╗░░░██║░░░██║░░░██║██║░░██║██║██║░░██║
        ░░╚██╔╝░░███████╗  ██████╔╝░░░██║░░░╚██████╔╝██████╔╝██║╚█████╔╝
        ░░░╚═╝░░░╚══════╝  ╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚═╝░╚════╝░
            
     ''')
    
def mostra_escolha():
    print('1. Cadastro de alunas curso de auto maquiagem')
    print('2. Listar alunas')
    print('3. Ativar alunas')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Voce escolheu a opção: ' , opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_alunas()
        elif opcao_escolhida == 2:
            print('Listar alunas')
        elif opcao_escolhida == 3:
            print('Ativar alunas')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
      opcao_invalida()

def cadastrar_alunas():
      os.system('cls')
      print('cadastrando alunas')
      nome_aluna = input('digite o nome da aluna')
      alunas.append(nome_aluna)
      print(f'{nome_aluna} foi adicionada as alunas do curso' )
      input('digite qualquer tecla para voltar')
      main()

def mostrar_alunas():
    os.system('cls')
    print('lista de alunas')
    for aluna in alunas:
        print(f' - (nome_alunas)')



def finalizar_programa():
    os.system('cls')
    print('finalizando_programa')
    
def opcao_invalida():
    print('Esse carter nao e permitido')
    input('digite qualquer tecla')
       

def main():
    mostra_titulo()  
    mostra_escolha()
    escolhe_opcao()

if __name__ == '__main__':
    main()
