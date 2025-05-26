import streamlit as st
import base64
from PIL import Image
import os
import tempfile
from enviar_email import enviar_emails as send_email
import re  # Adicionar import para expressão regular

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

    /* Remover o texto "Press enter to submit" */
    button[kind="primaryFormSubmit"] + div {
        display: none !important;
    }
    
    .stButton button {
        width: 100%;
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
    </nav>
</div>
""".format(logo=logo_html)

st.markdown(nav_links, unsafe_allow_html=True)

st.title("Bem-vindo a Dataconst Jr")
st.markdown(""" #### Análises confiáveis, soluções inteligentes  """)

st.markdown("---")

st.markdown("""
### Sobre Nós

A Dataconst Jr é a Empresa Júnior de Estatística da UFBA, formada por estudantes apaixonados por dados e tecnologia. 
Nosso propósito é aproximar a academia do mercado, oferecendo soluções estatísticas acessíveis e de alta qualidade.

Acreditamos na democratização da estatística e trabalhamos com uma diversidade de projetos que vão desde análises descritivas, 
modelagem preditiva, estudos de mercado, até inteligência artificial, sempre com foco em gerar valor para nossos clientes.
""")

# Adicionar imagens dos membros lado a lado
col1, col2 = st.columns(2)

with col1:
    image_path = os.path.join("imagens", "membros2.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, use_container_width=True)

with col2:
    image_path = os.path.join("imagens", "membros3.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, use_container_width=True)

st.markdown("---")

st.markdown("### Nossos Serviços")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="service-card">
        <div style="height: 100px;">
            <h5>• Serviços Acadêmicos</h5>
            <p style="margin: 0;">Realizamos análises para IC, TCC, Mestrado e Doutorado</p>
        </div>
        <div style="height: 140px;">
            <h5>• Dashboards personalizados</h5>
            <p style="margin: 0;">Transformamos dados complexos em visualizações interativas e intuitivas, com dashboards desenvolvidos para facilitar a tomada de decisão</p>
        </div>
        <div style="height: 120px;">
            <h5>• Planejamento amostral e de experimentos</h5>
            <p style="margin: 0;">Realizamos o planejamento da amostragem e estruturação de experimentos para garantir resultados confiáveis e representativos</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <div style="height: 100px;">
            <h5>• Inteligência Artificial e Machine Learning</h5>
            <p style="margin: 0;">Soluções com IA como chatbots, modelos preditivos e classificatórios</p>
        </div>
        <div style="height: 140px;">
            <h5>• Treinamentos e cursos</h5>
            <p style="margin: 0;">Capacitamos pessoas e equipes com conteúdos sobre estatística, análise de dados e ferramentas digitais como Python, R, Power BI</p>
        </div>
        <div style="height: 120px;">
            <h5>• Pesquisa de mercado e formulário</h5>
            <p style="margin: 0;">Elaboramos formulários e pesquisas de mercado, ajudando a gerar dados estratégicos</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Rodapé
st.markdown("---")

# CTA Section
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h2>🎯 Quer transformar seus dados em soluções?</h2>
    <p style="font-size: 1.2rem; margin: 1rem 0;">
        <em>Fale conosco</em> e descubra como podemos ajudar.
    </p>
</div>
""", unsafe_allow_html=True)

# Função para validar email
def validar_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Formulário de contato
# Inicializar variáveis de estado se não existirem
if 'form_nome' not in st.session_state:
    st.session_state.form_nome = ""
if 'form_email' not in st.session_state:
    st.session_state.form_email = ""
if 'form_assunto' not in st.session_state:
    st.session_state.form_assunto = ""
if 'form_mensagem' not in st.session_state:
    st.session_state.form_mensagem = ""

with st.form("contact_form"):
    nome = st.text_input("Nome*", value=st.session_state.form_nome)
    email = st.text_input("Email para contato*", value=st.session_state.form_email)
            
    assunto = st.text_input("Assunto*", value=st.session_state.form_assunto)
    mensagem = st.text_area("Mensagem*", value=st.session_state.form_mensagem)
    anexos = st.file_uploader("Anexos (opcional)", accept_multiple_files=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        submitted = st.form_submit_button("Enviar mensagem", use_container_width=True)
    
    if submitted:
        # Salvar os valores atuais no estado da sessão
        st.session_state.form_nome = nome
        st.session_state.form_email = email
        st.session_state.form_assunto = assunto
        st.session_state.form_mensagem = mensagem
        
        # Validar campos obrigatórios e formato do email
        if not nome or not email or not assunto or not mensagem:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        elif not validar_email(email):
            st.error("Por favor, insira um email válido.")
        else:
            # Converter os arquivos do Streamlit para arquivos temporários
            arquivos_temp = []
            if anexos:
                for arquivo in anexos:
                    # Criar arquivo temporário
                    temp_dir = tempfile.mkdtemp()
                    temp_path = os.path.join(temp_dir, arquivo.name)
                    
                    with open(temp_path, "wb") as f:
                        f.write(arquivo.getbuffer())
                    arquivos_temp.append(temp_path)

            senha = st.secrets["SENHA_EMAIL"]

            dic_email = {
                "senha": senha,
                "remetente": "vinicius4burame@gmail.com",
                "destinatarios": [{"nome": "", "email": "vinicius4burame@gmail.com"}],
                "assunto": f"{nome} - {email} - {assunto}",
                "corpo_base": mensagem,
                "anexos": arquivos_temp
            }
            
            try:
                send_email(**dic_email)
                st.success("Obrigado pela mensagem! Entraremos em contato em breve.")
                # Limpar os campos após envio bem-sucedido
                st.session_state.form_nome = ""
                st.session_state.form_email = ""
                st.session_state.form_assunto = ""
                st.session_state.form_mensagem = ""
                
                # Limpar arquivos temporários
                for temp_file in arquivos_temp:
                    try:
                        os.remove(temp_file)
                        os.rmdir(os.path.dirname(temp_file))
                    except:
                        pass
                        
            except Exception as e:
                st.error(f"Erro ao enviar mensagem: {str(e)}")
                
                # Limpar arquivos temporários em caso de erro
                for temp_file in arquivos_temp:
                    try:
                        os.remove(temp_file)
                        os.rmdir(os.path.dirname(temp_file))
                    except:
                        pass

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
