import streamlit as st 
import random

# sidebar 
st.sidebar.title("Menu")

pagina = st.sidebar.selectbox(
    "Escolha uma pagina",
    ["home", "gráfico"]
)

if pagina == "home":
    st.title("Página Home")
    st.write("Sistema usando o Streamlit")
    
    # Input de texto
    nome = st.text_input("Digite seu nome")
    
    # Selectbox (Corrigido de st.cursor para st.selectbox)
    linguagem = st.selectbox(
        "Escolha uma linguagem",
        ["Python", "Java", "JavaScript"]
    )
    
    # Slider
    idade = st.slider(
        "Escolha sua idade",
        min_value=0,
        max_value=100,
        value=20
    )
    
    #checkbox 
    mostrar = st.checkbox("Mostrar mensagem")
    
    if mostrar:
        st.success("checkbox marcado")
        

    # Exibindo os resultados
    if nome:
        st.write(f"Olá {nome}, você prefere {linguagem} e tem {idade} anos!")
    #Botão 
    
    if st.button("Clique aqui"):
        st.write(f"nome {nome},")
        st.write(f"curso {linguagem},")
        st.write(f"idade {idade},")
        
        st.subheader("colunas")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("coluna 1")
            st.info("conteudo da coluna 1")
            
        with col2:
            st.subheader("coluna 2")
            st.warning("conteudo da coluna 2")        
        

elif pagina == "gráfico":
    st.title("Página de Gráfico")
    st.write("Aqui está um exemplo de gráfico aleatório:")
    
    # Criando dados aleatórios
    dados = [random.randint(0, 100) for _ in range(20)]
    st.line_chart(dados)