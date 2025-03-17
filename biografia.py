from datetime import datetime
import requests
import json
import calendar
import locale

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8") 

# Nome
nome = str(input("Informe o nome: "))

especiais = "!@#$%^&*()-_+=~?/°ªº[]=§¬1234567890"

while any (especial in nome for especial in especiais):
    print(f"{nome} é um nome inválido! Tente novamente!")
    nome = str(input("Informe o nome: "))
#--------------------------------------------------------------------------------------------

# dia de nascimento
dia_nasc = int(input("Insira o dia de nascimento: "))
while dia_nasc <= 0 or dia_nasc > 32:
    print("Data inválida. Por favor, insira uma data válida!")
    dia_nasc = int(input("Insira o dia de nascimento: "))
#--------------------------------------------------------------------------------------------


# mês de nascimento    
mes_nasc = int(input("Insira o mês de nascimento: "))
nome_mes = calendar.month_name[mes_nasc]

while True: 
    if mes_nasc <= 0 or mes_nasc > 13:
        print(f"O mês de nascimento {mes_nasc} é inválido. Por favor, insira uma data válida.")
        mes_nasc = int(input("Insira o mês de nascimento: "))
        nome_mes = calendar.month_name[mes_nasc]
    elif mes_nasc in (4, 6, 9, 11) and dia_nasc > 30:
        print("Data inválida. Por favor, insira uma data válida!")
        dia_nasc = int(input("Insira o dia de nascimento: "))
    else:
        break
#--------------------------------------------------------------------------------------------



# ano de nascimento
ano_atual = datetime.today().year

ano_nasc = int(input("Insira o ano de nascimento: "))

while True:
    if ano_nasc > ano_atual:
        print(f"O ano de nascimento {ano_nasc} é inválido. Por favor, insira uma data válida.")
        ano_nasc = int(input("Insira o ano de nascimento: "))

    elif ano_nasc % 4 != 0 and mes_nasc == 2 and dia_nasc > 28:
        print("Data inválida. Por favor, insira uma data válida!")
        dia_nasc = int(input("Insira o dia de nascimento: "))
    else: 
        break

#-------------------------------------------------------------------------------------------- 




cep_info = input("Informe o cep (sem pontos): ")
url_cep = f'https://viacep.com.br/ws/{cep_info}/json/'
resposta = requests.get(url_cep)


while True:

    if resposta.status_code == 200 and not any(c in cep_info for c in ".-"):
        break

    print("CEP inválido. Digite o CEP novamente sem pontos ou barra.")
    cep_info = input("Informe o cep (sem pontos): ")
    url_cep = f'https://viacep.com.br/ws/{cep_info}/json/'
    resposta = requests.get(url_cep)

info = json.loads(resposta.content)
cep = info["cep"]
logradouro = info["logradouro"]
bairro = info["bairro"]
cidade = info["localidade"]
uf = info["uf"]
complemento = str(input("Complemento: "))
num_end = int(input("Nº: "))

objetivo = str(input("Insira o seu objetivo: "))



print(f"- Nome: {nome}")
print(f"- Data de nascimento: {dia_nasc} de {str.capitalize(nome_mes)} de {ano_nasc}")
print(f"- Endereço: {logradouro}, {num_end} - {bairro}, {cidade}-{uf}")
print(f"- Objetivo: {objetivo}")