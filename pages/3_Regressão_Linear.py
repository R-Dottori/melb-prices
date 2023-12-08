
import streamlit as st
import pandas as pd


st.title('Regressão Linear')
st.write('Na etapa final do projeto, montamos nosso modelo de regressão linear.')
st.write('Separamos a variável alvo (preço) e usamos as demais variáveis para tentar prever os preços dos imóveis.')

melb_previsoes = pd.read_csv('melb_previsoes.csv')
melb_previsoes[['Price', 'PredictedPrice']]

st.write('')
st.write('')
st.write('Podemos avaliar o modelo com as seguintes métricas:')
st.write('MAE = ', melb_previsoes.iloc[0]['MAE'])
st.write('MSE = ', melb_previsoes.iloc[0]['MSE'])
st.write('RMSE = ', melb_previsoes.iloc[0]['RMSE'])
