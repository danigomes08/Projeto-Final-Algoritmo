from datetime import datetime

def criar_aluno(lista_alunos, nome):
    if not nome.strip():
        print("Erro: Nome do aluno não pode ser vazio.")
        return False
    ano = datetime.now().year
    matricula = f"{ano}{len(lista_alunos) + 1:04d}"
    aluno = {
        'nome': nome,
        'matricula': matricula,
        'notas': []
    }
    lista_alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso.")
    return True

def listar_alunos(lista_alunos):
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return False
    for aluno in lista_alunos:
        print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Notas: {aluno['notas']}")