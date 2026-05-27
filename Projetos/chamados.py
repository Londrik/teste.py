import streamlit as st

# Configuração inicial da página
st.set_page_config(page_title="Sistema de Chamados", layout="centered")
st.title("🎫 Sistema de Chamados")

# 1. Criar a lista de chamados no estado da sessão
if "chamados" not in st.session_state:
    st.session_state.chamados = []

# --- SEÇÃO 1: ABRIR CHAMADO ---
st.subheader("📝 Abrir Chamado")

# Formulário para evitar que a página recarregue a cada clique
with st.form(key="novo_chamado", clear_on_submit=True):
    titulo = st.text_input("Título do Chamado")
    descricao = st.text_area("Descrição de serviço")
    botao_enviar = st.form_submit_button("Abrir Chamado")

    if botao_enviar:
        if titulo.strip() != "" and descricao.strip() != "":
            novo_chamado = {
                "id": len(st.session_state.chamados),  # ID único para controle
                "titulo": titulo,
                "descricao": descricao,
                "status": "Aberto"
            }
            st.session_state.chamados.append(novo_chamado)
            st.success("✅ Chamado aberto com sucesso!")
        else:
            st.error("⚠️ Por favor, preencha todos os campos.")

st.markdown("---")

# --- SEÇÃO 2: VISUALIZAR E GERENCIAR CHAMADOS ---
st.subheader("📋 Chamados Registrados")

if not st.session_state.chamados:
    st.info("Nenhum chamado aberto no momento.")
else:
    # Loop para exibir cada chamado de trás para frente (mais recentes primeiro)
    for index, chamado in enumerate(reversed(st.session_state.chamados)):
        # Descobrir o índice real no array original
        id_real = len(st.session_state.chamados) - 1 - index
        
        # Cria um card visual para cada chamado
        with st.expander(f"📌 {chamado['titulo']} - [{chamado['status']}]"):
            st.write(f"**Descrição:** {chamado['descricao']}")
            
            # Linha com opções de ações (Mudar Status e Excluir)
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # Seletor de status
                opcoes_status = ["Aberto", "Em Andamento", "Resolvido"]
                idx_atual = opcoes_status.index(chamado['status'])
                novo_status = st.selectbox(
                    f"Alterar status de '{chamado['titulo']}'",
                    opcoes_status,
                    index=idx_atual,
                    key=f"status_{id_real}"
                )
                
                # Atualiza o status se ele for alterado
                if novo_status != chamado['status']:
                    st.session_state.chamados[id_real]['status'] = novo_status
                    st.rerun()
            
            with col2:
                # Botão para excluir chamado
                st.write("") # Espaçamento para alinhar o botão
                if st.button("🗑️ Excluir", key=f"del_{id_real}"):
                    st.session_state.chamados.pop(id_real)
                    st.toast("Chamado excluído!")
                    st.rerun()