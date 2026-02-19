aluno = ['Michele Oliveira', 4, 9.5, True]
print(f"Nome: {aluno[0]}")
print(f"Faltas: {aluno[1]}")
print(f"Média: {aluno[2]}")

if aluno[3] == True:
    print(f"Aprovado: Sim")
else:
    print(f"Aprovado: Não")

alunos = ['Michele Oliveira']
alunos.append ('João Silva')
while True:
    nome = input("Digite o nome do aluno\n--> ")
    alunos.append(nome)
    resposta = input("Deseja adicionar mais um aluno? S/N\n--> ")
    if resposta == 'N':
        print(f"Alunos cadastrados {alunos}")
        break
        