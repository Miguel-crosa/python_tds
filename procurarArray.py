alunos = ['jose', 'miguel', 'rafael', 'pedro']

pessoa = 'miguel'

if pessoa in alunos:
    print(f"O aluno: {pessoa} está na posição: {alunos.index(pessoa)} do array, ou na posição {alunos.index(pessoa) + 1}.")
    pergunta = input("Voce gostaria que deixasse a pessoa em alguma posição especifica? S/N?\n--> ")
    if pergunta == 'S':
        posicaoPergunta = int(input("Digite a posição desejada"))
        if posicaoPergunta > len(alunos):
            print(f"A posição é invalida")
        else:
            posicao_desejada = alunos[posicaoPergunta]
            if pessoa not in posicao_desejada:
                alunos[0].replace(alunos[0], 'miguel')
                print(f"O aluno: {pessoa} agora está na posição do {posicao_desejada}")
                print(f"Lista nova: {alunos}")

if pessoa not in alunos:
    print(f"O aluno: {pessoa} não esta na lista. Gostaria de adicionar?")
    pergunta = input("Sim/Não\n--> ")
    if pergunta == 'Sim':
        alunos.append(f'{pessoa}')
        print(f"O aluno {pessoa} foi adicionado na lista alunos.\nLista nova: {alunos}")
        
for indice, aluno in enumerate(alunos):
    print(f"{indice}")
    if alunos[indice] == 'miguel':
        print(f"Aluno desejado encontrado na posição {indice + 1}.")
        break