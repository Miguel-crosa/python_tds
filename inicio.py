from datetime import datetime

ano_atual = datetime.now().year

clube = "SPFC"

campeonato_mundial = 3

ano_fundacao = 1930

print(f"{clube} possui {campeonato_mundial} títulos mundiais.")
print(f"São {ano_atual - ano_fundacao} anos de existencia.\n")


escola = "Senai"
curso = ("Técnico em desenvolvimento de sistemas")
uc = "Lógica de Programação e Algoritmos"

print(f"\nEscola: {escola} \n"
      f"Curso: {curso}\n"
      f"Unidade Curricular: {uc}\n"
      )

print(f"Programa de empréstimos."
      f"Reposta: (0- Não ou 1- Sim)"
      )

nome_negativado = int(input("Possui Nome Negativado? "))

if nome_negativado == 1:
    print("Não pode realizar emprestimo")
else:
    carteira_assinada = int(input("Possui Carteira Assinada? "))
    if carteira_assinada == 0:
        print("Não pode realizar emprestimo")
    else:
        possui_casa_propria = int(input("Possui casa própria? "))
        if possui_casa_propria == 0:
            print("Não pode realizar emprestimo")
        else:
            print("Conceder Emprestimo")