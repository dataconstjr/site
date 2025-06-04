import streamlit as st
import os

# Configuração da página - DEVE SER A PRIMEIRA CHAMADA STREAMLIT
st.set_page_config(
    page_title="Dataconst Jr",
    page_icon=os.path.join("imagens", "logo.png"),
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Definindo as páginas
pages = {
    "": [
        st.Page("paginas/Home.py", title="Página Inicial", icon="🏠", default=True)
    ],
    "Análise": [
        st.Page("paginas/Analise_de_Dados.py", title="Análise de Dados", icon="📊")
    ],
    #"Contato": [
    #    st.Page("pages/Fale_Conosco.py", title="Fale Conosco", icon="📬")
    #]
}

# Executar a página selecionada
pg = st.navigation(pages)
pg.run() 
