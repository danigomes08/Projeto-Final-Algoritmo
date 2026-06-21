from notas import calcular_media

def ordenar_por_nome(lista_alunos):
    copia = lista_alunos[:]
    for i in range(len(copia)):
        for j in range(0, len(copia) - i - 1):
            if copia[j]['nome'].lower() > copia[j + 1]['nome'].lower():
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
    return copia


def ordenar_por_nota(lista_alunos):
    copia = lista_alunos[:]
    for i in range(len(copia)):
        for j in range(0, len(copia) - i - 1):
            media_j = calcular_media(copia[j]['notas']) or 0
            media_j1 = calcular_media(copia[j + 1]['notas']) or 0
            if media_j > media_j1:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
    return copia