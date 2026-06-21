# utils.py
# Funções auxiliares/genéricas usadas em vários módulos.

import os


def limpar_tela():
    """Limpa o terminal (Windows: cls, Linux/Mac: clear)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa a execução até o usuário apertar Enter, para dar tempo de ler o resultado."""
    input("\nPressione Enter para continuar...")


def ler_float_seguro(mensagem):
    """
    Pede um número ao usuário repetidamente até que uma entrada válida
    seja digitada. Evita que o programa quebre com ValueError.
    """
    while True:
        valor = input(mensagem)
        try:
            return float(valor)
        except ValueError:
            print("Erro: digite um número válido (ex: 7.5).")


def ler_nome_valido(mensagem):
    """
    Pede um nome ao usuário repetidamente até que algo não-vazio
    (ignorando espaços) seja digitado.
    """
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        print("Erro: o nome não pode ser vazio.")


def validar_campo_busca(campo):
    """
    Confirma se o campo informado é um dos campos pesquisáveis do aluno.
    """
    return campo in ['nome', 'matricula']
