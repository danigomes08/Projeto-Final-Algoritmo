from aluno import criar_aluno, listar_alunos
from notas import cadastrar_notas, calcular_media, calcular_media_todos
from busca import busca_linear, busca_binaria
from ordenacao import ordenar_por_nome, ordenar_por_nota
from utils import ler_float_seguro, ler_nome_valido


def main():
    lista_alunos = []

    while True:
        print("\nMenu:")
        print("1. Listar alunos")
        print("2. Cadastrar aluno")
        print("3. Buscar aluno")
        print("4. Ordenar alunos")
        print("5. Cadastrar notas")
        print("6. Calcular média")
        print("7. Relatórios")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_alunos(lista_alunos)
        elif opcao == "2":
            nome = ler_nome_valido("Digite o nome do aluno: ")
            sobre_nome = ler_nome_valido("Digite o sobrenome do aluno: ")
            nome_completo = f"{nome} {sobre_nome}"
            criar_aluno(lista_alunos, nome_completo)
        elif opcao == "3":
            chave = input("Digite a matrícula ou nome do aluno para buscar: ")
            campo = input("Digite o campo de busca (nome/matricula): ")
            tipo_busca = input("Tipo de busca (linear/binaria): ").strip().lower()
            if tipo_busca == "binaria":
                if campo == "nome":
                    lista_para_busca = ordenar_por_nome(lista_alunos)
                else:
                    lista_para_busca = sorted(lista_alunos, key=lambda a: a[campo])
                aluno_encontrado = busca_binaria(lista_para_busca, chave, campo)
            elif tipo_busca == "linear":
                aluno_encontrado = busca_linear(lista_alunos, chave, campo)
            else:
                print("Tipo de busca inválido.")
                aluno_encontrado = None
            if aluno_encontrado:
                print(f"Aluno encontrado: {aluno_encontrado}")
            elif tipo_busca in ("linear", "binaria"):
                print("Aluno não encontrado.")
        elif opcao == "4":
            criterio = input("Ordenar por (nome/nota): ")
            if criterio == "nome":
                lista_ordenada = ordenar_por_nome(lista_alunos)
                listar_alunos(lista_ordenada)
            elif criterio == "nota":
                lista_ordenada = ordenar_por_nota(lista_alunos)
                listar_alunos(lista_ordenada)
            else:
                print("Critério inválido.")
        elif opcao == "5":
            matricula = input("Digite a matrícula do aluno para cadastrar nota: ")
            aluno_encontrado = busca_linear(lista_alunos, matricula, 'matricula')
            if aluno_encontrado:
                nota = ler_float_seguro(f"Digite a nota para {aluno_encontrado['nome']}: ")
                cadastrar_notas(aluno_encontrado, nota)
            else:
                print("Aluno não encontrado.")
        elif opcao == "6":
            matricula = input("Digite a matrícula do aluno para calcular média: ")
            aluno_encontrado = busca_linear(lista_alunos, matricula, 'matricula')
            if aluno_encontrado:
                media = calcular_media(aluno_encontrado['notas'])
                if media is not None:
                    print(f"Média do aluno {aluno_encontrado['nome']}: {media:.2f}")
            else:
                print("Aluno não encontrado.")
        elif opcao == "7":
            resultados = calcular_media_todos(lista_alunos)
            if resultados:
                print("Relatório de médias:")
                for nome, matricula, media in resultados:
                    if media is not None:
                        print(f"Nome: {nome}, Matrícula: {matricula}, Média: {media:.2f}")
                    else:
                        print(f"Nome: {nome}, Matrícula: {matricula}, Média: sem notas cadastradas")
            else:
                print("Nenhum aluno cadastrado.")
        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
