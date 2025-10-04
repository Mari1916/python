import pandas as pd
import matplotlib as plt

import streamlit as st 
# pip install streamlit

st.title("Vizualização de dados")

# Upload de Arquivo CSV
arquivo = st.file_uploader("Envie seu arquivo CSV", type=["csv"])

# Verificar se o arquivo existe
if arquivo is not None:
    # Ler o arquivo
    df = pd.read_csv(arquivo)

    st.write("Dados carregados: ")
    st.dataframe(df)

    # Selectbox - para tipo de grafico
    opcao = st.selectbox(
        "Escolha o tipo de gráfico:",
        ["Barras", "Pizza", "Linha"]
    )

    # Grafico de barras
    if opcao == "Barras":
        st.bar_chart(df.set_index("Nome")["Quantidade"])

    # Grafico de linhas
    elif opcao == "Linha":
        st.line_chart(df.set_index("Nome")["Quantidade"])

    # Grafico de pizza
    elif opcao == "Pizza":
        st.pyplot(df.set_index("Nome").plot.pie(y="Quantidade").figure)

else:
    st.info("ENvie um arquivo CSV com as colunas Nome e Quantidade...")

# python -m streamlite run graficos_steam.py