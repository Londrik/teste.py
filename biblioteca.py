import streamlit as st

# TÍTULO
st.title("Sistema de Biblioteca")

# CRIAR LISTA DE LIVROS (Memória temporária)
if "livros" not in st.session_state:
    st.session_state.livros = []

# CADASTRAR LIVRO
st.subheader("Cadastrar Livro")
nome_livro = st.text_input("Nome do livro")
autor = st.text_input("Autor")

# BOTÃO CADASTRAR
if st.button("Cadastrar Livro"):
    if nome_livro != "" and autor != "":
        livro = {
            "nome": nome_livro,
            "autor": autor,
            "emprestado": False
        }
        st.session_state.livros.append(livro)
        st.success("Livro cadastrado com sucesso!")
        st.rerun()

# LISTAR LIVROS
st.subheader("Livros Cadastrados")
if len(st.session_state.livros) == 0:
    st.warning("Nenhum livro cadastrado.")
else:
    for i, livro in enumerate(st.session_state.livros):
        st.write(f"### {livro['nome']}")
        st.write(f"Autor: {livro['autor']}")
        
        # STATUS DO LIVRO
        if livro["emprestado"] == False:
            st.success("Disponível")
        else:
            st.error("Emprestado")
        
        # COLUNAS PARA AÇÕES
        col1, col2 = st.columns(2)
        
        # EMPRÉSTIMO (Coluna 1)
        with col1:
            if st.button("Emprestar", key=f"emp_{i}"):
                st.session_state.livros[i]["emprestado"] = True
                st.success("Livro emprestado!")
                st.rerun()
                
        # DEVOLUÇÃO (Coluna 2)
        with col2:
            if st.button("Devolver", key=f"dev_{i}"):
                st.session_state.livros[i]["emprestado"] = False
                st.success("Livro devolvido!")
                st.rerun()
                
        st.divider()