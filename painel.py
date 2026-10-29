import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Dashboard Vale", layout="wide")


@st.cache_data
def carregar(arquivo):
    return pd.read_excel(arquivo)


st.title("Dashboard da empresa Vale")

tab1, tab2 = st.tabs(["Vale (VALE3)", "Empresas da B3"])

with tab1:
    df = carregar("VALE3_evolucao.xlsx")

    # Gráfico do lucro por trimestre
    dados = df.loc[df["conta"] == "lucro", ["trimestre", "valor"]]
    fig, ax = plt.subplots()
    sns.lineplot(data=dados, x="trimestre", y="valor", ax=ax)
    ax.set_title("Gráfico do lucro")
    plt.setp(ax.get_xticklabels(), rotation=45)
    fig.tight_layout()

    st.pyplot(fig)
    st.dataframe(df)

with tab2:
    df_b3 = carregar("planilhao_b3.xlsx")
    st.dataframe(df_b3)

    df_size = df_b3.groupby("setor").size()
    fig2, ax2 = plt.subplots()
    sns.barplot(x=df_size.values, y=df_size.index, ax=ax2)
    ax2.set_title("Número de empresas por setor")
    ax2.set_xlabel("Quantidade de empresas")
    ax2.set_ylabel("Setor")
    fig2.tight_layout()

    st.pyplot(fig2)
