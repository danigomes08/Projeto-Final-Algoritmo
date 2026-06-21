# Sistema Acadêmico Completo

Projeto final da disciplina de Algoritmo e Lógica. Sistema de linha de comando em Python
para gerenciar alunos e notas, utilizando listas, matrizes, busca e ordenação.

## Funcionalidades

- Cadastro de alunos (matrícula gerada automaticamente no formato `AAAANNNN`, ex: `20260001`)
- Listagem de alunos
- Busca por nome ou matrícula, com escolha entre busca linear ou busca binária
- Ordenação por nome (alfabética) ou por nota (média)
- Cadastro de notas por aluno
- Cálculo de média individual e relatório de médias de todos os alunos

## Estrutura do projeto

```
projeto/
├── main.py        # Menu interativo, ponto de entrada do programa
├── aluno.py        # Cadastro e listagem de alunos
├── notas.py        # Cadastro de notas e cálculo de médias
├── busca.py        # Busca linear e busca binária
├── ordenacao.py    # Ordenação por nome e por nota (bubble sort)
└── utils.py        # Funções auxiliares (leitura segura de entrada)
```

## Como executar

```bash
cd projeto
python main.py
```

## Algoritmos implementados

- **Busca linear**: percorre a lista item a item, O(n).
- **Busca binária**: requer lista ordenada pelo campo buscado; o menu ordena a lista
  automaticamente antes de buscar quando essa opção é escolhida, O(log n).
- **Ordenação**: implementada manualmente com bubble sort, O(n²).

## Estrutura de dados

Cada aluno é representado como um dicionário:

```python
{
    "nome": "Maria Silva",
    "matricula": "20260001",
    "notas": [7.5, 8.0]
}
```

Os alunos são armazenados em uma lista (`lista_alunos`), e a lista de `notas` de cada
aluno funciona como a "matriz" de notas do sistema (uma linha por aluno).
