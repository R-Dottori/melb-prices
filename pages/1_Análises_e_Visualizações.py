
# Importações
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Análises e Visualizações')
melb = pd.read_csv('melb_final.csv')

# Gráfico 1
st.write('Primeiro, observamos a distribuição de preços dos imóveis analisados.')

graf_1 = plt.figure()
plt.hist(melb['Price'], bins=50)
plt.xlabel('Preço (em milhões)')
plt.axvline(np.mean(melb['Price']), color='red')
plt.axvline(np.median(melb['Price']), color='green')
plt.title('Distribuição de Preços dos Imóveis', fontsize=15)
st.pyplot(graf_1)



# Gráfico 2
st.write('')
st.write('')
st.write('')
st.write('Em sequência, estudamos a correlação entre as variáveis usadas no modelo.')

melb_heat = melb[['Price', 'Rooms', 'Distance', 'Bathroom', 'Car', 'Landsize', 
            'BuildingArea', 'YearBuilt', 'Propertycount', 'TypeIndex', 'RegionIndex', 'MethodIndex']]
graf_2 = plt.figure(figsize=(15,15))
mask = np.triu(melb_heat.corr())
sns.heatmap(melb_heat.corr(), cmap = 'coolwarm', annot=True, vmax=1, vmin=-1, mask=mask, linewidths=1)
plt.title('Mapa de Calor', fontsize=20)
st.pyplot(graf_2)



# Gráfico 3
st.write('')
st.write('')
st.write('')
st.write('Para cada variável numérica, examinamos as dispersões ao comparar com os preços.')

graf_3, axes = plt.subplots(4, 2, figsize=(15,30))
sns.scatterplot(data=melb, x='Rooms', y='Price', ax=axes[0,0])
axes[0,0].set_ylabel('Preço (em milhões)')
axes[0,0].set_title('Por Número de Quartos')
sns.scatterplot(data=melb, x='Distance', y='Price', ax=axes[0,1])
axes[0,1].set_ylabel('Preço (em milhões)')
axes[0,1].set_title('Por Distância do Centro')
sns.scatterplot(data=melb, x='Bathroom', y='Price', ax=axes[1,0])
axes[1,0].set_ylabel('Preço (em milhões)')
axes[1,0].set_title('Por Número de Banheiros')
sns.scatterplot(data=melb, x='Car', y='Price', ax=axes[1,1])
axes[1,1].set_ylabel('Preço (em milhões)')
axes[1,1].set_title('Por Vagas na Garagem')
sns.scatterplot(data=melb, x='Landsize', y='Price', ax=axes[2,0])
axes[2,0].set_ylabel('Preço (em milhões)')
axes[2,0].set_title('Pela Área do Terreno')
sns.scatterplot(data=melb, x='BuildingArea', y='Price', ax=axes[2,1])
axes[2,1].set_ylabel('Preço (em milhões)')
axes[2,1].set_title('Pela Área do Imóvel')
sns.scatterplot(data=melb, x='YearBuilt', y='Price', ax=axes[3,0])
axes[3,0].set_ylabel('Preço (em milhões)')
axes[3,0].set_title('Por Ano de Construção')
sns.scatterplot(data=melb, x='Propertycount', y='Price', ax=axes[3,1])
axes[3,1].set_ylabel('Preço (em milhões)')
axes[3,1].set_title('Pelo número de Imóveis no Bairro')
graf_3.suptitle('Dispersão de Preços', fontsize=20)
st.pyplot(graf_3)



# Gráfico 4
st.write('')
st.write('')
st.write('')
st.write('Por último, investigamos as distribuições de preço para as variáveis categóricas.')

graf_4, axes = plt.subplots(2, 2, figsize=(15,15))
sns.boxplot(data=melb, x='Type', y='Price', ax=axes[0,0])
axes[0,0].set_xlabel('Tipo de Imóvel')
axes[0,0].set_ylabel('Preço (em milhões)')
axes[0,0].set_title('Por Tipo de Imóvel')
sns.boxplot(data=melb, x='Regionname', y='Price', ax=axes[0,1])
axes[0,1].set_xlabel('Região')
axes[0,1].set_ylabel('Preço (em milhões)')
axes[0,1].set_title('Por Região')
axes[0,1].set_xticklabels(axes[0,1].get_xticklabels(), rotation=90)
sns.boxplot(data=melb, x='Method', y='Price', ax=axes[1,0])
axes[1,0].set_xlabel('Método de Venda')
axes[1,0].set_ylabel('Preço (em milhões)')
axes[1,0].set_title('Por Método de Venda')
graf_4.delaxes(axes[1,1])
graf_4.suptitle('Distribuições de Preço nas Variáveis Categóricas', fontsize=20)
st.pyplot(graf_4)
