def busca_linear(lista_alunos, chave, campo):
    if campo not in ['nome', 'matricula']:
        print("Erro: Campo de busca deve ser 'nome' ou 'matricula'.")
        return None
    for aluno in lista_alunos:
        if aluno[campo] == chave:
            return aluno
    return None

def busca_binaria(lista_alunos, chave, campo):
    if campo not in ['nome', 'matricula']:
        print("Erro: Campo de busca deve ser 'nome' ou 'matricula'.")
        return None

    esquerda, direita = 0, len(lista_alunos) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista_alunos[meio][campo] == chave:
            return lista_alunos[meio]
        elif lista_alunos[meio][campo] < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None