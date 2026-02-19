print(list(range(10, 16)))
print(list(range(10, 16, 2)))
print(list(range(16, 10, -1)))
print(list(range(16, 10, -2)))

for i in range(4):
    print(f"\n- {i} - ")  # método de array
    if i == 3:
        print("\nFim do primeiro loop\n")
        for j in range(4):
            print(f"- - {j+1} - -")  # método para mostrar o 'real valor'
            if j + 1 == 4:
                print("\nFim do segundo loop\n")
