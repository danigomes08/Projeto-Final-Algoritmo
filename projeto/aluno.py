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
    print(f"{'Matrícula':<10} {'Nome':<25} {'Notas'}")
    print("-" * 55)
    for aluno in lista_alunos:
        print(f"{aluno['matricula']:<10} {aluno['nome']:<25} {aluno['notas']}")
    return True