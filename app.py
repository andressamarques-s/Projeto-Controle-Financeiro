import streamlit as st
from storage import carregar_gastos, salvar_gastos, limites, registra_gastos, deletar_gasto
import plotly.express as px
import pandas as pd

gastos = carregar_gastos()

st.title("💰 Método 50/30/20")
st.write("Organize seu salário de forma inteligente.")

renda = st.number_input("Digite sua renda líquida (R$):", min_value=0.0)

if renda > 0:
    necessidades = renda * 0.50
    desejos = renda * 0.30
    poupanca = renda * 0.20
    total_necessidade = 0
    total_desejo = 0
    total_poupança = 0
    for gasto in gastos:
        if gasto["Categoria"] == "necessidade":
            total_necessidade += gasto["Valor"]
        elif gasto["Categoria"] == "desejo":
            total_desejo += gasto["Valor"]
        elif gasto["Categoria"] == "poupança":
            total_poupança += gasto["Valor"]
    st.write(f"🏠 Necessidades: R$ {total_necessidade:.2f} de R$ {necessidades:.2f}")
    st.progress(total_necessidade / necessidades)
    st.write(f"🎉 Desejos: R$ {total_desejo:.2f} de R$ {desejos:.2f}")
    st.progress(total_desejo / desejos)
    st.write(f"💎 Poupanças: R$ {total_poupança:.2f} de R${poupanca:.2f}")
    st.progress(total_poupança / poupanca)
    if total_necessidade > necessidades:
        st.warning("⚠️ Você ultrapassou o limite de Necessidades!")
    if total_desejo > desejos:
        st.warning("⚠️ Você ultrapassou o limite de Desejos!")
    if total_poupança > poupanca:
        st.warning("⚠️ Você ultrapassou o limite de Poupança! ")

    st.subheader("Sua divisão:")
    col1, col2, col3 = st.columns(3)
    col1.metric("🏠 Necessidades (50%)", f"R$ {necessidades:.2f}")
    col2.metric("🎉 Desejos (30%)", f"R$ {desejos:.2f}")
    col3.metric("💎 Poupança (20%)", f"R$ {poupanca:.2f}")

st.subheader("Registrar gasto")
Descricao = st.text_input("Descrição do gasto: ")
Valor = st.number_input("Digite o valor gasto: ")
Categoria = st.text_input("Informe a categora (necessidade/desejo/poupança): ")
if st.button("Salvar Gasto"):
    dic = {
        "Descricao" : Descricao,
        "Valor" : Valor, 
        "Categoria" : Categoria}
    salvar_gastos(dic)
    st.success("Gastos registrados com suscesso!")

desc_deletar = st.text_input("Descrição do gasto a ser deletado: ")
if st.button("Deletar Gasto"):
    deletar_gasto(desc_deletar)
    st.success("Gasto removido com sucesso!")

st.subheader("Gastos Registrados")
if st.button("Visualizar Gastos"):
    carregar = carregar_gastos()
    st.dataframe(carregar)

st.subheader("Distribuição dos gastos")
gastos = carregar_gastos()
if gastos:
    df = pd.DataFrame(gastos)
    fig = px.pie(df, values="Valor", names="Categoria", title="Distribuição dos gastos")
    st.plotly_chart(fig)
    

