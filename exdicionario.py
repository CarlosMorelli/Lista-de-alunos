import os
import time

    #fecha o sitema quando precionado 0 #
def fechar_sistema():
    print('\nFechando sistema...')
    time.sleep(2)
    print('O sistema foi fechado com sucesso 🖐')
    exit()


def adcaluno(dic: dict):
    # Confere se já tem 10 alunos cadastrados em seu sistema #
    if len(dic) >= 10:
        print('\n❌ Os 10 registros já estão preenchidos')
        return

    # Entrada de dados #
    nome = input('\nDigite o nome do aluno: ').strip().title()
    
    # Te "Obriga" a digitar algo #
    if not nome:
        print('\n❌ Nome inválido! Por favor, insira um nome válido.')
        return
    
    # Confere se os nomes contem apenas letras #
    if not nome.replace(" ", "").isalpha():
        print('\n❌ O nome deve conter apenas letras!.')
        return

    # Confere se tem alguma aluno já com aquele nome #
    if nome in dic:
        print('\n❌ Aluno já inserido.')
        return

    # Confere se as nota são apenas números #
    try:
        nota = float(input('Digite a nota do aluno: '))
    except ValueError:
        print('\n❌ Por favor, insira apenas números.')
        return
    
    # Confere se a nota está entre 0 e 10 #
    if nota < 0 or nota > 10:
        print('\n❌ Nota inválida! A nota deve estar entre 0 e 10.')
        return

    # Apenas avisa que o aluno foi adicionado com secesso #
    dic[nome] = nota
    print('\nAluno adicionado com sucesso 👍')

def editar_aluno(dic: dict):
    # Confere se a lista está preenchida #
    if not dic: 
        print('\nA lista está vazia 🚫, preencha os nomes e notas dos alunos.')
        return

    # Entrada de dados #
    nome_antigo = input('\nDigite o nome do aluno que deseja alterar: ').strip().title()

    # Confere se o aluno realmente existe #
    if nome_antigo not in dic:
        print('\nAluno não encontrado 🚫')
        return

    # Entrada de dados #
    nome_novo = input('Digite o novo nome: ').strip().title()
    
    # Confere se o aluno existe na lista para ser editado #
    if not nome_novo:
        print('\n❌ Nome inválido! Por favor, insira um nome válido.')
        return

    # Confere se a nota editada está em valores númericos #
    try:
        nota = float(input('Digite a nova nota do aluno: '))
    except ValueError:
        print('\n❌ Valor inválido! Por favor, insira uma nota numérica.')
        return

    # Confere se a nota edita está entre 0 e 10
    if nota < 0 or nota > 10:
        print('\n❌ Nota inválida! A nota deve estar entre 0 e 10.')
        return

    # Tira o nome antigo e coloca o novo
    dic[nome_novo] = dic.pop(nome_antigo)
    dic[nome_novo] = nota
    print('\nAlterado com sucesso')

def listar_alunos(dic: dict):
    # Confere se a lista está preenchida #
    if not dic: 
        print('\nA lista está vazia 🚫')
        return
    
    #
    print(f'{"Nome":<15} Nota')
    print('-' * 20)
    for chave, valor in dic.items():
        print(f'{chave:<15} {valor}')

def apagardaterra_aluno(dic: dict):
    # Confere se a lista está preenchida #
    if not dic:  
        print('\nA lista está vazia 🚫')
        return

    # Entrada de dados #
    nome = input('\nDigite o nome do aluno que deseja excluir: ').strip().title()

    # Mostra que o aluno foi removido com sucesso #
    if nome in dic:
        dic.pop(nome)
        print('\nAluno removido com sucesso')

    # Confere se o aluno está ou não na lista #
    else:
        print('\nAluno não encontrado 🚫')

def media_nota(dic: dict):
    # Confere se a lista está preenchida #
    if not dic:  
        print('\nA lista está vazia 🚫')
        return

    # Calcula a média #
    media = sum(dic.values()) / len(dic)
    print(f'\nMédia da turma = {media:.2f}')

def consutar1_aluno(dic: dict):
    # Confere se a lista está preenchida #
    if not dic:  
        print('\nA lista está vazia 🚫')
        return

    # Entrada de dados #
    nome = input('\nDigite o nome do aluno: ').strip().title()

    # Serve para ver um aluno separadamente #
    if nome in dic:
        print(f'{"Nome":<15} Nota')
        print('-' * 20)
        print(f'{nome:<15} {dic[nome]}')
    
    # Mostra se o aluno está na lista #
    else:
        print('\nAluno não encontrado 🚫')

def matar_todos(dic: dict):
    # Confere se a lista está preenchida # 
    if not dic:  
        print('\nA lista está vazia 🚫')
        return

    # Remove todos os alunos de uma vez só #
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
            adcaluno(dicionario)

        case '2':
            editar_aluno(dicionario)

        case '3':
            listar_alunos(dicionario)

        case '4':
            apagardaterra_aluno(dicionario)

        case '5':
            media_nota(dicionario)

        case '6':
            consutar1_aluno(dicionario)

        case '7':
            matar_todos(dicionario)

        case _:
            print('\nPor favor selecione apenas uma das opções do menu.')

    input('\nAperte ENTER para continuar ')