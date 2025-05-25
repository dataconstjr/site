import streamlit as st
import base64
import os

# Função para carregar e codificar a imagem em base64
def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# Carregar o logo
logo_path = os.path.join("imagens", "logo+nome.png")  # Para a navbar
logo_base64 = get_image_base64(logo_path)

# CSS personalizado
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&display=swap');

    /* Cores da marca */
    :root {
        --purple: #8523F5;
        --white: #FFFFFF;
        --coral: #F15A24;
        --peach: #FFDA8F;
        --dark: #1E1E1E;
    }

    /* Reset e estilos globais */
    * {
        font-family: 'Barlow', sans-serif !important;
    }

    .main {
        background-color: var(--dark);
    }

    .main .block-container {
        padding-top: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        max-width: none !important;
    }

    /* Esconder completamente a barra lateral e seu botão */
    div[data-testid="collapsedControl"] {
        display: none !important;
    }
    
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    button[kind="header"] {
        display: none !important;
    }

    /* Novos seletores para o botão da barra lateral */
    .st-emotion-cache-1dp5vir {
        display: none !important;
    }

    .st-emotion-cache-5rimss {
        display: none !important;
    }

    .st-emotion-cache-1egp75f {
        display: none !important;
    }

    /* Forçar largura total e remover margens */
    .st-emotion-cache-18ni7ap {
        left: 0 !important;
        width: 100% !important;
        margin-left: 0 !important;
    }

    .st-emotion-cache-z5fcl4 {
        padding-left: 0 !important;
        padding-right: 0 !important;
    }

    /* Garantir que o conteúdo principal use toda a largura */
    .main .block-container {
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 0 !important;
    }

    /* Barra de navegação superior */
    .navbar {
        background: linear-gradient(135deg, var(--purple), var(--coral));
        padding: 0.5rem 2rem;  /* Reduzido o padding vertical */
        margin: -2rem -6rem 5rem -6rem;
        display: flex;
        align-items: center;
        gap: 2rem;
        position: relative;
        z-index: 1000;
        height: 80px;  /* Altura fixa para a navbar */
        overflow: hidden;  /* Para garantir que a imagem não extrapole */
    }

    .navbar-brand {
        display: flex;
        align-items: center;
        margin-left: -6.5rem;  /* Move a imagem mais para a esquerda */
        color: var(--white) !important;
        text-decoration: none;
        font-size: 1.2rem;
        font-weight: 600;
    }

    .navbar-brand img {
        height: 280px;  /* Aumentado apenas o tamanho da imagem */
        width: auto;
        object-fit: contain;
        transform: scale(1.2);  /* Aumenta um pouco mais a imagem */
    }

    .navbar-nav {
        display: flex;
        gap: 2rem;
        margin-left: auto;
    }

    .nav-item {
        color: var(--white) !important;
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        transition: background-color 0.3s;
        font-weight: 500;
        font-size: 1.3rem;  /* Aumentado o tamanho da fonte do menu */
        cursor: pointer;
    }

    .nav-item:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }

    /* Remover sublinhado dos links */
    a.nav-item {
        text-decoration: none !important;
    }

    /* Estilos de texto globais */
    .stMarkdown, .stText, div:not(.navbar *) {
        color: var(--white) !important;
    }

    /* Estilo dos textos e headers */
    p, li, label, .stTextInput > div {
        color: var(--white) !important;
        font-size: 1.1rem;
        line-height: 1.6;
    }

    h1, h2, h3, h4, h5, h6 {
        color: var(--white) !important;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* Estilo para os elementos do Streamlit */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        margin-bottom: 2rem;
    }

    .stTabs [data-baseweb="tab"] {
        color: var(--white);
        border-radius: 4px;
        padding: 0.5rem 1rem;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        background-color: var(--purple);
    }

    /* Estilo para os inputs e selects */
    .stSelectbox > div > div,
    .stFileUploader > div > div {
        background-color: rgba(255, 255, 255, 0.05);
        border-color: var(--purple);
    }

    /* Estilo para os gráficos */
    .js-plotly-plot {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Barra de navegação superior
logo_html = f'<img src="data:image/png;base64,{logo_base64}" alt="Logotipo e Slogan Dataconst Jr"/>' if logo_base64 else ''

nav_links = """
<div class="navbar">
    <div class="navbar-brand">
        {logo}
    </div>
    <nav class="navbar-nav">
        <a href="./" target="_self" class="nav-item">Página Inicial</a>
        <a href="./Analise_de_Dados" target="_self" class="nav-item">Análise de Dados</a>
        <a href="./Fale_Conosco" target="_self" class="nav-item">Fale Conosco</a>
    </nav>
</div>
""".format(logo=logo_html)

st.markdown(nav_links, unsafe_allow_html=True)

# Conteúdo da página
st.title("📬 Fale Conosco")
st.markdown("---")

st.markdown("""
### Entre em Contato

Estamos aqui para ajudar! Preencha o formulário abaixo e entraremos em contato o mais breve possível.
""")

# Formulário de contato
with st.container():
    st.markdown('<div class="contact-form">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        telefone = st.text_input("Telefone")
    
    with col2:
        empresa = st.text_input("Empresa (opcional)")
        assunto = st.text_input("Assunto")
    
    mensagem = st.text_area("Mensagem", height=150)
    enviar = st.button("Enviar Mensagem")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Informações adicionais
st.markdown("""
### Outras Formas de Contato

Você também pode nos encontrar através dos seguintes canais:
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    📍 **Endereço**  
    Instituto de Matemática e Estatística - UFBA  
    Av. Adhemar de Barros, s/n - Ondina  
    Salvador - BA, 40170-110
    """)

with col2:
    st.markdown("""
    📞 **Telefone**  
    +55 (71) 99121-6019
    
    📧 **E-mail**  
    dataconstjr@gmail.com
    """)

with col3:
    st.markdown("""
    🌐 **Redes Sociais**  
    Instagram: @dataconstjr  
    LinkedIn: Dataconst Jr
    """)

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align: center;'>Desenvolvido por Dataconst Jr - Empresa Júnior de Estatística da UFBA</p>", unsafe_allow_html=True)

# Ícones de redes sociais no rodapé
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
        <a href='mailto:dataconstjr@gmail.com' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/email.png' width='40'/>
        </a>
        <a href='https://www.instagram.com/dataconstjr' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/instagram-new.png' width='40'/>
        </a>
        <a href='https://github.com/dataconstjr' target='_blank'>
            <img src='https://img.icons8.com/ios-filled/50/000000/github.png' width='40'/>
        </a>
        <a href='https://wa.me/5571991216019' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/whatsapp.png' width='40'/>
        </a>
        <a href='https://www.linkedin.com/in/dataconst-jr-992375355/' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/linkedin.png' width='40'/>
        </a>
    </div>
    """, unsafe_allow_html=True) 