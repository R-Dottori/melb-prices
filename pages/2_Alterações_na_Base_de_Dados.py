
# Importações
import streamlit as st
import pandas as pd

st.title('Alterações na Base de Dados')

melb_bruto = pd.read_csv('melb_data.csv')
melb_final = pd.read_csv('melb_final.csv')

st.write('Vamos apresentar algumas mudanças que realizamos na base de dados.')



# Valores nulos
st.write('Eliminamos valores nulos.')
col_nulos_bruto, col_nulos_final = st.columns(2)
with col_nulos_bruto:
    st.write('Base original:')
    st.write(melb_bruto.isna().sum().sort_values(ascending=False))
with col_nulos_final:
    st.write('Base alterada:')
    st.write(melb_final.isna().sum())



# Valores discrepantes
st.write('Avaliamos que alguns dados não se encaixavam com a realidade do problema.')
col_anos, col_area = st.columns(2)
with col_anos:
    st.write('Encontramos um imóvel construído no ano de 1196.')
    st.write(melb_bruto[['YearBuilt', 'Price']][melb_bruto['YearBuilt'] < 1800])
with col_area:
    st.write('E vários imóveis registrados com 0 m², embora tivessem 2 ou mais quartos.')
    st.write(melb_bruto[['BuildingArea', 'Rooms', 'Bathroom', 'Car']][melb_bruto['BuildingArea'] == 0])



# LabelEncoder
st.write('Convertemos algumas variáveis categóricas que consideramos pertinentes para o modelo em índices numéricos.')
st.write(melb_final[['Type', 'TypeIndex', 'Regionname', 'RegionIndex']])
