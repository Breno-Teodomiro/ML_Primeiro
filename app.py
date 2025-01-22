import streamlit as st  # Importing the Streamlit library
import pandas as pd  # Importing the Pandas library for data manipulation 

# Importing the Linear Regression model from the Scikit-learn library
from sklearn.linear_model import LinearRegression 

# base de dados de pizzas
df = pd.read_csv('pizzas.csv')

# Criando um modelo de Regressão Linear
modelo = LinearRegression()    

x = df[['diametro']]     # Atribui a variável x o diâmetro da pizza
y = df[['preco']]         # Atribui a variável y o preço da pizza

modelo.fit(x, y)         # Treina o modelo

st.title('Predição de Preços de Pizzas')  # Título da aplicação
st.divider()  # Adiciona uma linha horizontal   

diametro = st.number_input('Digite o diâmetro da pizza em cm: ')  # Input do diâmetro da pizza

if diametro:  # Se o diâmetro for informado
    preco_previsto = modelo.predict([[diametro]])[0][0]  # Preço previsto da pizza
    st.write(f'O preço previsto da pizza de diametro {diametro:.2f} cm é de R$ {preco_previsto:.2f}!')  # Exibe o preço previsto
    st.balloons()  # Exibe balões de comemoração        

