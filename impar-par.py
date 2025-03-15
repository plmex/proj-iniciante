import time
import sys



print("=" * 37)
print("Olá! Seja bem-vind@ ao Par ou Ímpar!")
print("=" * 37)

print("\n\nCarregando", end="")
for i in range(3):
    for j in range(3):
        print(".", end="")
        sys.stdout.flush()
        time.sleep(1)
    print(" " * 10, end="\r")
    time.sleep(0.5)
    print("Carregando", end="") 
     
print("\n")

nome_jogador = input(str("Por favor, insira o seu nome de jogador: "))
print(f"\nÓtimo! Vamos começar,",nome_jogador, "!\n")

numero = int(input("Em qual número você pensou? \nNúmero: "))

res = numero % 2

if res == 0:
    print(f"\033[7;36m{numero} é par!\033[m")
else: 
    print(f"\033[7;35m{numero} é ímpar!\033[m")



