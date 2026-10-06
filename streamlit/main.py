import streamlit as st
import pandas as pd
import numpy as np

# Título da Aplicação
st.title("📊 Meu Dashboard com Streamlit")

# Entrada de Texto e Seleção
nome = st.text_input("Digite seu nome:", "Desenvolvedor")
opcao = st.selectbox("Escolha um número de dados:", [10, 50, 100])

st.write(f"Olá, **{nome}**! Exibindo {opcao} registros abaixo:")

# Gerando dados de exemplo
df = pd.DataFrame(
    np.random.randn(opcao, 2),
    columns=['Vendas', 'Acessos']
)

# Exibindo Tabela Interativa
st.dataframe(df)

# Gráfico Nativo
st.line_chart(df)

# Botão com Ação
if st.button("Clique Aqui"):
    st.success("Ação executada com sucesso!")