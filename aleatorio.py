import random

aleatorio = random

alunos = ['Joao', 'Pedro', 'Rafael', 'Diego', 'Miguel']
random.shuffle(alunos)
alunos.sort(reverse=True)
print(f'A lista invertida é: {alunos}')

print(f"Lista aleatoria: {alunos}")

sorteada = random.choice(alunos)
print(f'O aluno sorteado é: {sorteada}')
