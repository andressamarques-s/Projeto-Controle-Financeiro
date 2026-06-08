import json

def carregar_gastos():
    try:
        with open("dados.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_gastos(gasto):
    lista = carregar_gastos()
    lista.append(gasto)
    with open("dados.json", "w") as arquivo:
        json.dump(lista, arquivo)

def limites(renda_liquida):
    porc1 = (renda_liquida * 50) / 100
    porc2 = (renda_liquida * 20) / 100
    porc3 = (renda_liquida * 30) / 100
    return porc1, porc2, porc3

def registra_gastos():
    descricao = input("Qual é a descrição do gasto: ")
    valor = float(input("Informe o valor do gasto: "))
    categoria = input("Qual é a categoria do gasto (necessidade/poupança/pessoal): ").lower()
    listagem = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria
    }
    salvar_gastos(listagem)

def deletar_gasto(Descricao):
    lista = carregar_gastos()
    for gasto in lista:
        if Descricao == gasto["Descricao"]:
            lista.remove(gasto)
    with open("dados.json", "w") as arquivo:
        json.dump(lista, arquivo)

        
