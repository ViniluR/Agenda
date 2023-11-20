import streamlit as st
from views import View

class AtualizarPerfilUI:
    def main():
        st.header("Atualizar perfil")
        AtualizarPerfilUI.atualizar()

    def atualizar():
        op = View.cliente_listar_id(st.session_state["cliente_id"])
        nome = "admin"
        if op.get_nome() != "admin":
            nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha")
        if st.button("Atualizar"):
            id = op.get_id()
            View.cliente_atualizar(id, nome, email, fone, senha)
            st.success("Perfil atualizado com sucesso")