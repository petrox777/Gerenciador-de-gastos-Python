# * cadastrar gastos;
# * consultar gastos já registrados;
# * organizar despesas por categoria;
# * calcular totais;
# * gerar um resumo financeiro;
# * identificar padrões básicos de consumo.

### 1. Cadastro de gastos

# O sistema deverá permitir o cadastro de uma nova despesa.

# Para cada gasto, deverão ser armazenadas, no mínimo, as seguintes informações:

# * descrição do gasto;
# * valor;
# * categoria;
# # * data.
# Descrição: Almoço
# Valor: 35.90
# Categoria: Alimentação
# Data: 27/09/2026

# gastos
#  ├── gasto 1 (dicionário)
#  │    ├── descrição
#  │    ├── valor
#  │    ├── categoria
#  │    └── data
#  │
#  ├── gasto 2
#  │    ├── descrição
#  │    ├── valor
#  │    ├── categoria
#  │    └── data



# 4. Filtros
# O sistema deverá permitir consultar os gastos de acordo com determinados critérios.
# Implemente pelo menos dois filtros, como:
# categoria;
# período;
# valor mínimo ou máximo.
# Exemplo:
# Digite a categoria: Alimentação

# O sistema deverá apresentar apenas os gastos pertencentes à categoria informada.



# 5. Resumo financeiro
# O programa deverá gerar um resumo dos gastos cadastrados.
# O resumo deverá apresentar, no mínimo:
# valor total gasto;
# quantidade de despesas;
# gasto médio;
# categoria com maior valor acumulado;
# maior despesa individual.
# Exemplo:
# ========== RESUMO FINANCEIRO ==========

# Total gasto: R$ 1.245,80
# Quantidade de gastos: 34
# Média por gasto: R$ 36,64

# Categoria com maior gasto:
# Alimentação - R$ 520,30

# Maior despesa:
# Supermercado - R$ 280,00
quantidade_gastos = 0
valor_total = 0
itens_cadastrados = []
gastos_gerais = []

import json

def carregar_dados():
    try:
        with open("dados_financeiros.json", "r") as arquivo:
            dados = json.load(arquivo)
            global gastos_gerais, valor_total, quantidade_gastos, itens_cadastrados
            gastos_gerais = dados.get("gastos", [])
            valor_total = dados.get("valor_total", 0)
            quantidade_gastos = dados.get("quantidade_gastos", 0)
            itens_cadastrados = dados.get("itens_cadastrados", [])
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Iniciando com dados vazios.")

carregar_dados()

def salvar_dados():
    dados = {
        "gastos": gastos_gerais,
        "valor_total": valor_total,
        "quantidade_gastos": quantidade_gastos,
        "itens_cadastrados": itens_cadastrados
    }
    with open("dados_financeiros.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

alimentacao = []
transporte = []
lazer = []
estudos = []
saude = []
moradia = []
outros = []

gavetas = {
    1: alimentacao,
    2: transporte,
    3: lazer,
    4: estudos,
    5: saude,
    6: moradia,
    7: outros,
}


# o que devo fazer:
#pegar o valor de cada categoria e somar em cada lista e dps adicionar a lista de valor total
# criar lista com cada categoria e quando a categoria for selecionada o valor vai para essa lista

# valor_total = [alimentacao, transporte, lazer, estudos, saude, moradia, outros]

def gaveta(gasto):
    """Coloca um gasto na lista da categoria e indica se a categoria e valida."""
    lista_categoria = gavetas.get(gasto.get("categoria"))
    if lista_categoria is None:
        return False
    lista_categoria.append(gasto)
    return True


for gasto_salvo in gastos_gerais:
    gaveta(gasto_salvo)


while True:
    descricao = input("Digite a descrição do gasto. ex: almoço, skin, roupa, etc: ")
    valor = float(input("Digite o valor do gasto anteriormente apresentado: "))
    while True:
        try:
            categoria = int(input("Selecione a categoria (1 a 7), sendo 1-Alimentação 2-Transporte 3-Lazer 4-Estudos 5-Saúde 6-Moradia 7-Outros: "))
        except ValueError:
            print("Digite um numero de 1 a 7. Sendo 1-Alimentação 2-Transporte 3-Lazer 4-Estudos 5-Saúde 6-Moradia 7-Outros.")
            continue
        if categoria in gavetas:
            break
        print("Categoria invalida. Escolha um numero de 1 a 7.")
    data = str(input("Data da compra: DD/MM/AAAA: "))
    quantidade_gastos += 1
    gastos = {
    "descricao": descricao, "valor": valor, "categoria": categoria, "data": data
} 
    gastos_gerais.append(gastos)
    gaveta(gastos)
    valor_total += valor
    itens_cadastrados.append(descricao)

    fim = input("Deseja cadastrar outro gasto? (s/n): ")
    if fim == "n":
        break



def filtros():
    filtro_categoria = (input("Digite a categoria que deseja filtrar: Alimentação, Transporte, Lazer, Estudos, Saúde, Moradia, Outros: ")).lower()
    print(filtro_categoria)
    if filtro_categoria == "alimentacao":
        print("o relatorio de alimentacao é:")
        print(alimentacao)
    elif filtro_categoria == "transporte" :
        print("o relatorio de transporte é:")
        print(transporte)
    elif filtro_categoria == "lazer":
        print("o relatorio de lazer é:")
        print(lazer)
    elif filtro_categoria == "estudos":
        print("o relatorio de estudos é:")
        print(estudos)
    elif filtro_categoria == "saude":
        print("o relatorio de saude é:")
        print(saude)
    elif filtro_categoria == "moradia":
        print("o relatorio de moradia é:")
        print(moradia)
    elif filtro_categoria == "outros":
        print("o relatorio de outros é:")
        print(outros)

def resumo_financeiro():
    media_gasto = valor_total / quantidade_gastos if quantidade_gastos > 0 else 0

    categorias = {
        "Alimentação": sum(gasto["valor"] for gasto in alimentacao),
        "Transporte": sum(gasto["valor"] for gasto in transporte),
        "Lazer": sum(gasto["valor"] for gasto in lazer),
        "Estudos": sum(gasto["valor"] for gasto in estudos),
        "Saúde": sum(gasto["valor"] for gasto in saude),
        "Moradia": sum(gasto["valor"] for gasto in moradia),
        "Outros": sum(gasto["valor"] for gasto in outros)
    }

    categoria_maior_gasto = max(categorias, key=categorias.get)
    maior_despesa = max(gastos_gerais, key=lambda x: x["valor"], default={"descricao": "Nenhuma", "valor": 0})

    print("========== RESUMO FINANCEIRO ==========")
    print(f"Total gasto: R$ {valor_total:.2f}")
    print(f"Quantidade de gastos: {quantidade_gastos}")
    print(f"Média por gasto: R$ {media_gasto:.2f}")
    print(f"Categoria com maior gasto: {categoria_maior_gasto} - R$ {categorias[categoria_maior_gasto]:.2f}")
    print(f"Maior despesa: {maior_despesa['descricao']} - R$ {maior_despesa['valor']:.2f}")
    print(f"Itens cadastrados: {itens_cadastrados}")


salvar_dados()
filtros()
resumo_financeiro()

def salvar_dados():
    dados = {
        "gastos": gastos_gerais,
        "valor_total": valor_total,
        "quantidade_gastos": quantidade_gastos,
        "itens_cadastrados": itens_cadastrados
    }
    with open("dados_financeiros.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

salvar_dados()
