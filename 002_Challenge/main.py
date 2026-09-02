import csv


dados = [
    ["nome", "idade", "cidade"],
    ["João", 25, "São Paulo"],
    ["Maria", 30, "Rio de Janeiro"],
] 

def criar_arquivo_csv(): 
    with open("dados.csv", "w", newline="") as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(dados)

    return "Arquivo CSV criado com sucesso!"

# with open("dados.csv", "r") as arquivo_csv:
    