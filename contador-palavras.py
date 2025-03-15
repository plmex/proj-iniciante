
print("Por favor, informe em uma frase algo em que você pensou hoje.")
frase = str(input("Frase: "))

palavras = frase.split() 

tamanho = len(palavras)

print(f"Legal! Você acabou de me dizer no que pensou em {tamanho} palavras!")