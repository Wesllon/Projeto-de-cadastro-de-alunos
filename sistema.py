import Funcoes
import time

print('Inicializando o sistema...')
time.sleep(0.5)

while True:
        print('''
                \nEscolha uma opção:
                1 -> Adicionar aluno
                2 -> Remover aluno
                3 -> Atualizar aluno
                4 -> Ver alunos
                5 -> Sair ''')
        opcao = input('Escolha a Opção que deseja: ')

        if opcao == '1':
            Funcoes.Adicionar_Aluno()
            time.sleep(1)
        elif opcao == '2':
            Funcoes.Remover_Aluno()
            time.sleep(1)
        elif opcao == '3':
           Funcoes.Atualizar_Aluno()
           time.sleep(1)
        elif opcao == '4':
            Funcoes.Ver_Alunos()
            time.sleep(1)
        elif opcao == '5':
            print('Finalizando o programa...')
            break
        else:
            print('Opção inválida. Por favor, Tente novamente.')
