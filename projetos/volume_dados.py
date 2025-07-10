import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta

caminho_datasets = "datasets"
df_compras = pd.read_csv(
    f"{caminho_datasets}/lj_compras.csv", sep=";", decimal=",", index_col=0, parse_dates=True)

df_lojas = pd.read_csv(
    f"{caminho_datasets}/lj_lojas.csv", sep=";", decimal=",", index_col=0)

df_produtos = pd.read_csv(
    f"{caminho_datasets}/lj_produtos.csv", sep=";", decimal=",", index_col=0)

df_produtos = df_produtos.rename(columns={"nome": "produto"})

df_compras = df_compras.reset_index()
df_compras = pd.merge(left=df_compras, right=df_produtos[[
                      "preco", "produto"]], on="produto", how="left")

df_compras = df_compras.set_index("data")
df_compras["comissao"] = df_compras["preco_x"] * 0.5

data_default = df_compras.index.date.max()
data_inicio = st.sidebar.date_input(
    "Data Inicial", data_default - timedelta(days=6))
data_final = st.sidebar.date_input(
    "Data Final", data_default)
