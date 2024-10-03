import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Título do painel
st.title('Dashboard Financeiro Interativo')

# Simulação de dados financeiros mensais (receitas e despesas)
# Aqui você pode substituir pelos seus próprios dados financeiros
np.random.seed(42)
meses = pd.date_range('2023-01-01', periods=12, freq='M').strftime('%b-%Y')
receitas = np.random.randint(2000, 8000, size=12)
despesas = np.random.randint(1500, 7000, size=12)
saldo = receitas - despesas

# Criar DataFrame
df_financeiro = pd.DataFrame({
    'Mês': meses,
    'Receitas': receitas,
    'Despesas': despesas,
    'Saldo': saldo
})

# Opção interativa para selecionar um período de meses
st.sidebar.subheader('Filtro de Período')
meses_selecionados = st.sidebar.multiselect(
    'Selecione os meses:',
    options=df_financeiro['Mês'],
    default=df_financeiro['Mês']
)

# Filtrar os dados com base na seleção do usuário
df_filtrado = df_financeiro[df_financeiro['Mês'].isin(meses_selecionados)]

# Gráfico de Receitas vs Despesas
st.subheader('Receitas vs Despesas')
fig_receitas_despesas = px.bar(df_filtrado, x='Mês', y=['Receitas', 'Despesas'],
                               barmode='group',
                               labels={'value': 'Valor (R$)', 'Mês': 'Meses'},
                               title='Comparação entre Receitas e Despesas')
st.plotly_chart(fig_receitas_despesas)

# Gráfico de Balanço Financeiro
st.subheader('Balanço Financeiro (Saldo)')
fig_saldo = px.line(df_filtrado, x='Mês', y='Saldo',
                    labels={'Saldo': 'Saldo (R$)', 'Mês': 'Meses'},
                    title='Saldo Acumulado por Mês',
                    markers=True)
fig_saldo.update_traces(line=dict(color='royalblue'))
st.plotly_chart(fig_saldo)

# Estatísticas financeiras
st.sidebar.subheader('Estatísticas Financeiras')
total_receitas = df_filtrado['Receitas'].sum()
total_despesas = df_filtrado['Despesas'].sum()
total_saldo = df_filtrado['Saldo'].sum()

st.sidebar.metric('Total de Receitas', f"R$ {total_receitas:,.2f}")
st.sidebar.metric('Total de Despesas', f"R$ {total_despesas:,.2f}")
st.sidebar.metric('Saldo Final', f"R$ {total_saldo:,.2f}")

# Download dos dados filtrados
st.subheader('Dados Filtrados')
st.dataframe(df_filtrado)

# Botão para download dos dados filtrados
def converter_para_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = converter_para_csv(df_filtrado)
st.download_button(
    label="Baixar dados filtrados em CSV",
    data=csv,
    file_name='dados_financeiros.csv',
    mime='text/csv',
)
