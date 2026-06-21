# notas.py
# Responsável pelo CADASTRO DE NOTAS (matriz: alunos x notas) e CÁLCULO DE MÉDIA.


def cadastrar_notas(aluno, nota):
    if nota < 0 or nota > 10:
        print("Erro: Nota deve ser entre 0 e 10.")
        return False
    aluno['notas'].append(nota)
    print(f"Nota {nota} cadastrada para aluno {aluno['nome']}.")
    return True


def calcular_media(notas):
    if not notas:
        print("Nenhuma nota cadastrada para este aluno.")
        return None
    media = sum(notas) / len(notas)
    return media


def calcular_media_todos(lista_alunos):
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return False
    resultados = []
    for aluno in lista_alunos:
        media = calcular_media(aluno['notas'])
        resultados.append((aluno['nome'], aluno['matricula'], media))
    return resultados