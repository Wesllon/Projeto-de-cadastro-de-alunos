#AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.
alunos = {}

def Adicionar_Aluno():
    nome = input('Digite o nome do aluno: ')
    while True:
        matricula = input('Digite o número de matrícula do aluno (somente números): ')
        if matricula.isdigit():
            alunos[matricula] = nome
            print('Aluno adicionado com sucesso!')
            break
        else:
            print('Por favor, digite apenas números para a matrícula.')
        

# RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.

def Remover_Aluno():
    while True:
        matricula = input('Digite o número de matrícula do aluno a ser removido (somente números): ')
        if matricula.isdigit():
            if matricula in alunos:
                del alunos[matricula]
                print('Aluno removido com sucesso!')
                break
            else:
                print('Aluno não encontrado.')
                break
        else:
            print('Por favor, digite apenas números para a matrícula.')

#AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário.

def Atualizar_Aluno():
    while True:
        matricula = input('Digite o número de matrícula do aluno a ser atualizado (somente números): ')
        if matricula.isdigit():
            if matricula in alunos:
                novo_nome = input('Digite o novo nome do aluno: ')
                alunos[matricula] = novo_nome
                print('Nome do aluno atualizado com sucesso!')
                break
            else:
                print('Aluno não encontrado.')
                break
        else:
            print('Por favor, digite apenas números para a matrícula.')

# VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.

def Ver_Alunos():
    print('Lista de Alunos(as) cadastrados(as):')
    for matricula, nome in alunos.items():
        print('Matrícula:', matricula, '- Nome:', nome)
