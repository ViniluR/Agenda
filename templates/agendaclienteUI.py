import streamlit as st
import pandas as pd
from views import View

class AgendaClienteUI:
  def main():
    st.header("Meus agendamentos")
    AgendaClienteUI.listar()

  def listar():
    cliente = View.cliente_listar_id(st.session_state["cliente_id"])
    agendas = View.agenda_listarcliente(cliente)
    if len(agendas) == 0:
      st.write("Você não possui nenhum agendamento")
    else:
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)