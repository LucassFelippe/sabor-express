import os

restaurantes = [{'nome':'Mokai', 'categoria':'Japonesa', 'ativo':True},
                {'nome':'Formaggios', 'categoria':'Pizzaria', 'ativo':True},
                {'nome':'Primavera', 'categoria':'Churrascaria', 'ativo':False}]

                              

     

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado restaurante')
    print('4. Sair\n')

def finalizar_app():
  exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
     input('\nDigite uma tecla para voltar ao menu ! ')
     main()

def opcao_invalida():
     print('Opção Invalida !\n')
     voltar_ao_menu_principal()

def exibir_subtitulo(texto):
     os.system('cls')
     linha = '*' * (len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurantes = input('Digite o nome do restaurantes que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurantes}: ')
    dados_do_restaurante = {'nome':nome_do_restaurantes, 'categoria':categoria_restaurante,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurantes}, foi cadastrado com sucesso ! ')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurante')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}\n')
    for restaurante in restaurantes:
         nome_restaurante = restaurante['nome']
         categoria = restaurante['categoria']
         ativo =  'Ativado' if restaurante['ativo'] else 'Desativado'
         print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')

    for restaurante in restaurantes:
         if nome_restaurante == restaurante['nome']:
              restaurante_encontrado = True 
              restaurante ['ativo'] = not restaurante['ativo']
              mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso! ' if restaurante['ativo'] else  f'O {nome_restaurante} foi desativado com sucesso! '
              print(mensagem)
    if not restaurante_encontrado:
         print('O restaurante não foi encontrado')
         
         
    
    
    
    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
                cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
                listar_restaurantes()
        elif opcao_escolhida == 3:
             alternar_estado_restaurante()
        elif opcao_escolhida == 4:
                finalizar_app()
        else:
            opcao_invalida()
    except:
         opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()