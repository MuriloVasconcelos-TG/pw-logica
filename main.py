import random

print("=" * 35)
print(" PEDRA, PAPEL OU TESOURA")
print( "=" * 35)

opcoes = ["pedra", "papel", "tesoura"]
computador = random.choice(opcoes)

jogador = input("\nEscolha (pedra/papel/tesoura): ").lower()

print(f"\nVocê: {jogador}")
print(f"Computador: {computador}")

if jogador == computador: 
    print ("\nEmpate!")
elif jogador == "pedra" and computador == "tesoura"
    print("\nVocê ganhou!")
elif jogador == "papel" and computador == "pedra"
    print("\nVocê ganhou!")
elif jogador == "tesoura" and computador == "papel"
    print("\nVocê ganhou!")
else
    print("\nVocê perdeu!")


print("=== PAR OU ÍMPAR ===")
nome1 = input("Nome do jogador 1: ")
nome2 = input("Nome do jogador 2: ")
escolha = int(input(f"{nome1}, seu número: "))