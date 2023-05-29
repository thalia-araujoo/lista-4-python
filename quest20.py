# Escreva uma função que receba uma lista de dicionários, onde cada dicionário representa
# um aluno com as chaves "nome" e "nota". A função deve retornar o nome do aluno com a maior nota.


def aluno_maior_nota(lista_alunos):
    maior_nota = 0 
    nomeAluno = ''  
    for dic in lista_alunos:  #lista de alunos percorre dentro do dicionario, e la tem notas e nomes
        notas = dic["Nota"]
        nomes = dic["Nome"]
        if notas > maior_nota: # qual nota vai ser maior q 0.
            maior_nota = notas #toda nota q vim vai ser maior
            nomeAluno = nomes 
    return nomeAluno, maior_nota

def main():
    alunos = []
    dicio = {}
    print("Digite o nome do aluno e sua nota: ")
    for i in range(0, 5):
        nome = input(f'Digite o nome do aluno {i+1}: ')
        nota = int(input("Nota: "))
        dicio = {"Nome": nome, "Nota": nota}
        alunos.append(dicio)
    print("Lista dos dicionários dos alunos: ")
    print(alunos)

    res = aluno_maior_nota(alunos)
    print("O aluno com a maior nota é:", res)


if __name__ == "__main__":
    main()