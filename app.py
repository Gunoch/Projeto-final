import streamlit as st

st.title("Olá, streamlit!")
st.header('Seção principal')
st.subheader("Subseção com detalhes")
st.write("texto com **negrito**, *itálico*, e ~~riscado~~")

st.markdown("""
# Título H1
## Título H2
Lista:
    - Item 1
    - Item 2
            
> Citações também funcionam.
""")

nome = st.text_input("Digite seu nome:")
idade = st.number_input("Idade:", min_value=0, max_value=120)

if (nome != ''  and idade > 0):
    st.markdown(f"Seu nome é: {nome}  \nSua idade é: {idade}")

else: 
    pass

mostrar = st.checkbox("Mostrar texto adcional")
nivel = st.slider("Nível de intensidade", 0, 10, 3)

genero = st.selectbox("Escolha um gênero musical:", ["Pop", "Rock", "Hip-hop", "Eletrônica"])

humor = st.radio("Seu humor hoje:", ["Feliz", "Triste", "Cansado", "Animado"])

if st.button("Clique aqui"):
    st.write("Você clicou no botão!")

data = st.date_input("Escolha uma data:")

horario = st.time_input("Escolha um hórario:")

intervalo = st.slider("Selicione o intervalo", 0, 100, (20 ,80))

import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Daniela"],
    "Idade": [23, 30, 19, 28],
    "Cidade": ["Goiânia", "São Paulo", "Rio de Janeiro", "Salvador"]
}

df = pd.DataFrame(dados)

st.write(df)
st.dataframe(df)
st.table(df)
    
