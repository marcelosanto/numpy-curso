import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

pasta_datasets = Path(__file__).parent / "../datasets"

# past_datasets.mkdir(parents=True, exist_ok=True)

LOJAS = [
    {"estado": "SP", "cidade": "São Paulo", "vendedores": [
        "Luiza Trajano", "Abigail Nordeste"]},
    {"estado": "ES", "cidade": "Vitória", "vendedores": [
        "Gergogia valentina", "Noberto Silva"]},
    {"estado": "MG", "cidade": "Belo Horizonte",
        "vendedores": ["Luana Rezende", "Vera lucia"]},
    {"estado": "RJ", "cidade": "Rio de Janeiro",
        "vendedores": ["Augusto cleber", "Ludimila lilas"]},
]

PRODUTOS = [
    {"nome": "Smartphone Samsung Galaxy", "id": 0, "preco": 1000},
    {"nome": "Notebook Dell Inspiron", "id": 1, "preco": 2000},
    {"nome": "Tablet Apple iPad", "id": 2, "preco": 1500},
    {"nome": "Câmera Canon EOS", "id": 3, "preco": 3000},
]

FORMA_PAGTO = ["dinheiro", "cartão de crédito", "cartão de débito", "pix"]

GENERO_CLIENTES = ["male", "female"]

compras = []

for _ in range(2000):
    loja = random.choice(LOJAS)
    vendedor = random.choice(loja["vendedores"])
    produto = random.choice(PRODUTOS)
    forma_pagto = random.choice(FORMA_PAGTO)
    data_compra = datetime.now() - timedelta(days=random.randint(1, 365),
                                             hours=random.randint(0, 23),
                                             minutes=random.randint(0, 59),
                                             seconds=random.randint(0, 59))
    genero_cliente = random.choice(GENERO_CLIENTES)
    nome_cliente = names.get_full_name(gender=genero_cliente)

    compras.append(
        {
            "data": data_compra,
            "id_compra": 0,
            "loja": loja["cidade"],
            "vendedor": vendedor,
            "produto": produto["nome"],
            "forma_pagto": forma_pagto,
            "nome_cliente": nome_cliente,
            "genero_cliente": genero_cliente.replace("female", "feminino").replace("male", "masculino"),
            "preco": produto["preco"]
        }
    )

df_compras = pd.DataFrame(compras).set_index("data").sort_index()

df_compras["id_compra"] = [i for i in range(len(df_compras))]

df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(PRODUTOS)

# Exportando dataframes
df_compras.to_csv(pasta_datasets / "lj_compras.csv", decimal=",", sep=";")
df_lojas.to_csv(pasta_datasets / "lj_lojas.csv", decimal=",", sep=";")
df_produtos.to_csv(pasta_datasets / "lj_produtos.csv", decimal=",", sep=";")

df_compras.to_excel(pasta_datasets / "lj_compras.xlsx")
df_lojas.to_excel(pasta_datasets / "lj_lojas.xlsx")
df_produtos.to_excel(pasta_datasets / "lj_produtos.xlsx")
