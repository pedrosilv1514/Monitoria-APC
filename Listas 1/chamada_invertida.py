quantidade_alunos = int(input())
lista_alunos = []


for i in range(quantidade_alunos):
    nome_do_aluno = input()
    lista_alunos.append(nome_do_aluno)


lista_alunos.sort(reverse=True)

for i in lista_alunos:
    print(i)
