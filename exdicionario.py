import os
import time

def fechar_sistema():
    print('\nFechando sistema...')
    time.sleep(2)
    print('O sistema foi fechado com sucesso 🖐')
    exit()

def adicionar_aluno(dic: dict):
    if len(dic) >= 10:
        print('\n❌  Os 10 registros já estão preenchidos')
        return

    nome = input('\nDigite o nome do aluno: ').strip().title()
    if not nome:
        print('\n❌  Nome inválido! Por favor, insira um nome válido.')
        return

    if not nome.replace(" ", "").isalpha():
        print('\n❌  O nome deve conter apenas letras!')
        return

    if nome in dic:
        print('\n❌  Aluno já inserido.')
        return

    try:
        nota = float(input('Digite a nota do aluno: '))
    except ValueError:
        print('\n❌  Por favor, insira apenas números.')
        return
    
    if nota < 0 or nota > 10:
        print('\n❌  Nota inválida! A nota deve estar entre 0 e 10.')
        return

    dic[nome] = nota
    print('\nAluno adicionado com sucesso 👍')

def editar_aluno(dic: dict):
    if not dic: 
        print('\nA lista está vazia 🚫, preencha os nomes e notas dos alunos.')
        return

    nome_antigo = input('\nDigite o nome do aluno que deseja alterar: ').strip().title()
    if nome_antigo not in dic:
        print('\nAluno não encontrado 🚫')
        return

    nome_novo = input('Digite o novo nome: ').strip().title()
    if not nome_novo:
        print('\n❌  Nome inválido! Por favor, insira um nome válido.')
        return

    try:
        nota = float(input('Digite a nova nota do aluno: '))
    except ValueError:
        print('\n❌  Valor inválido! Por favor, insira uma nota numérica.')
        return

    if nota < 0 or nota > 10:
        print('\n❌  Nota inválida! A nota deve estar entre 0 e 10.')
        return

    dic[nome_novo] = dic.pop(nome_antigo)
    dic[nome_novo] = nota
    print('\nAlterado com sucesso')

def listar_alunos(dic: dict):
    if not dic: 
        print('\nA lista está vazia 🚫')
        return
    
    print(f'{"Nome":<15} Nota')
    print('-' * 20)
    for chave, valor in dic.items():
        print(f'{chave:<15} {valor}')

def apagar_aluno(dic: dict):
    if not dic:  
        print('\nA lista está vazia 🚫')
        return

    nome = input('\nDigite o nome do aluno que deseja excluir: ').strip().title()
    if nome in dic:
        dic.pop(nome)
        print('\nAluno removido com sucesso')
    else:
        print('\nAluno não encontrado 🚫')

def media_nota(dic: dict):
    if not dic:  
        print('\nA lista está vazia 🚫')
        return

    media = sum(dic.values()) / len(dic)
    print(f'\nMédia da turma = {media:.2f}')

def consultar1_aluno(dic: dict):
    if not dic:  
        print('\nA lista está vazia 🚫')
        return

    nome = input('\nDigite o nome do aluno: ').strip().title()
    if nome in dic:
        print(f'{"Nome":<15} Nota')
        print('-' * 20)
        print(f'{nome:<15} {dic[nome]}')
    else:
        print('\nAluno não encontrado 🚫')

def apagar_todos(dic: dict):
    if not dic:  
        print('\nA lista está vazia 🚫')
        return

    dic.clear()
    print('\nTodos os alunos foram removidos. ✔')

# ------------------------------------------------------------------------------#
#                                      Menu                                     #

dicionario = {}

while True:
    os.system('cls')

    opcao = input(
        '''
        0 - Sair :)
        1 - Adicionar novo Aluno | Nota (limite 10 alunos)
        2 - Editar Aluno | Nota
        3 - Listar os Alunos
        4 - Excluir um Aluno
        5 - Calcular a média da turma
        6 - Consultar um aluno
        7 - Apagar todos os alunos da sala
        
    Escolha: ''')

    match opcao:
        case '0':
            fechar_sistema()
        case '1':
            adicionar_aluno(dicionario)
        case '2':
            editar_aluno(dicionario)
        case '3':
            listar_alunos(dicionario)
        case '4':
            apagar_aluno(dicionario)
        case '5':
            media_nota(dicionario)
        case '6':
            consultar1_aluno(dicionario)
        case '7':
            apagar_todos(dicionario)
        case _:
            print('\nPor favor selecione apenas uma das opções do menu.')

    input('\nAperte ENTER para continuar ')
