
# Importações
import streamlit as st
import pandas as pd

# Configuração e título
st.set_page_config(
    page_title='Apresentação - Imóveis em Melbourne'
)

st.title('Análise de Imóveis em Melbourne')

st.write('Vamos avaliar os preços de alguns imóveis na cidade de Melbourne, na Austrália.')
st.write('Usaremos visualizações para nos auxiliar nessas análises.')
st.write('Faremos ajustes e mudanças na base de dados, como limpar valores nulos ou duplicados.')
st.write('Ao final, montaremos um modelo de regressão linear multivariada para tentar prever os preços desses imóveis.')

st.write('Aqui está a base original de dados:')
melb = pd.read_csv('melb_data.csv')
st.write(melb)
