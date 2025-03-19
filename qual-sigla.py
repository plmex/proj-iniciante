
conceito = input("Insira um conceito ou nome de alguma organização: ")

conceito = conceito.split()

vetados = ['as', 'os', 'a', 'o', 'da', 'do', 'das', 'dos', 'de', 'na', 'no', 'nos', 'nas', 'e', 'é']

acronimo = []

for palavra in conceito:
    if palavra not in vetados:
        acronimo.append(str.capitalize(palavra[0:1]))


print(''.join(acronimo))