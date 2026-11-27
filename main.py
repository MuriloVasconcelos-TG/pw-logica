notas = []
soma = 0
for contador in range(5):
    nota = float(input(f"Digite a {contador + 1}ª nota: "))
    notas.append(nota)
    soma += nota

media = soma / len(notas)

print("Vocês vão criar os prints para esse exercício conforme o resultado")

print("Maior nota: ", max(notas))
print("Menor nota: ", min(notas))