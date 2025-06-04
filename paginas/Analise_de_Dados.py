import streamlit as st
import pandas as pd
import plotly.express as px
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
    </nav>
</div>
""".format(logo=logo_html)

st.markdown(nav_links, unsafe_allow_html=True)

st.title("📊 Análise de Dados")
st.markdown("---")

st.markdown("""
Esta página permite carregar arquivos de dados nos formatos CSV, XLSX ou XLS, desde que estejam organizados em formato tabular, ou seja, com colunas definidas para cada variável. Com os dados carregados corretamente, você poderá explorá-los de forma interativa: gerar visualizações com sua cor preferida e acessar uma análise descritiva com estatísticas resumidas das variáveis.

Se quiser levar sua análise para o próximo nível, conte com nosso suporte especializado em estatística e ciência de dados. Estamos aqui para dar significado aos seus dados e transformar informações brutas em decisões inteligentes.
""")

st.markdown("---")
# Upload de dados
uploaded_file = st.file_uploader("", type=['csv', 'xlsx', 'xls'])

if uploaded_file is not None:
    try:
        # Leitura dos dados
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Configuração padrão para todos os gráficos
        PLOT_CONFIG = {
            'height': 500,  # Reduzindo um pouco a altura
            'width': None,
            'showlegend': False,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'margin': dict(l=40, r=40, t=60, b=40),  # Ajustando as margens
            'autosize': True  # Garantindo que o gráfico se ajuste ao container
        }

        # Seletor de cor para os gráficos
        with st.expander("🎨 Escolha uma cor para os gráficos 🎨", expanded=True):
            cor = st.color_picker("", "#8523F5")

        # Visualizações
        st.header("📈 Visualizações")
        
        # Tipos de visualização
        viz_type = st.selectbox(
            "Selecione o tipo de visualização",
            ["Histograma", "Linha do Tempo", "Gráfico de Dispersão", "Box Plot", "Gráfico de Barras", ]
        )
        
        if viz_type == "Gráfico de Dispersão":
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("Variável do eixo X", df.columns)
            with col2:
                y_col = st.selectbox("Variável do eixo Y", df.columns)
            
            fig = px.scatter(df, x=x_col, y=y_col, 
                           title=f"Gráfico de Dispersão: {x_col} vs {y_col}",
                           template="plotly_dark",
                           color_discrete_sequence=[cor])
            fig.update_layout(**PLOT_CONFIG)
            st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Histograma":
            col = st.selectbox("Variável para o histograma", df.columns)
            fig = px.histogram(df, x=col, 
                             title=f"Histograma: {col}",
                             template="plotly_dark",
                             color_discrete_sequence=[cor])
            
            # Adiciona apenas as linhas entre os bins
            fig.update_traces(marker_line_color="white",
                            marker_line_width=1,
                            opacity=1)
            
            fig.update_layout(**PLOT_CONFIG)
            st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Box Plot":
            col = st.selectbox("Variável para o box plot", df.columns)
            fig = px.box(df, y=col, 
                        title=f"Box Plot: {col}",
                        template="plotly_dark",
                        color_discrete_sequence=[cor])
            fig.update_layout(**PLOT_CONFIG)
            st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Gráfico de Barras":
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("Variável do eixo X (categorias)", df.columns)
            with col2:
                y_col = st.selectbox("Variável do eixo Y (valores)", df.columns)
            
            # Criar o gráfico de barras
            fig = px.bar(df, x=x_col, y=y_col,
                        title=f"Gráfico de Barras: {y_col} por {x_col}",
                        template="plotly_dark",
                        color_discrete_sequence=[cor])
            
            # Adiciona linhas nas barras
            fig.update_traces(marker_line_color="white",
                            marker_line_width=1,
                            opacity=1)
            
            fig.update_layout(**PLOT_CONFIG)
            st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Linha do Tempo":
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("Variável de tempo (eixo X)", df.columns)
            with col2:
                y_col = st.selectbox("Variável para plotar (eixo Y)", df.columns)
            
            # Ordenar os dados pelo eixo X para o gráfico de linha
            df_sorted = df.sort_values(by=x_col)
            
            fig = px.line(df_sorted, x=x_col, y=y_col,
                         title=f"Linha do Tempo: {y_col} por {x_col}",
                         template="plotly_dark",
                         color_discrete_sequence=[cor])
            fig.update_layout(**PLOT_CONFIG)
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # Análise Descritiva
        st.header("📋 Análise Descritiva")
        
        # Informações básicas do dataset
        st.subheader("Visão Geral dos Dados")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Registros", len(df))
        with col2:
            st.metric("Total de Colunas", len(df.columns))
        with col3:
            st.metric("Dados Ausentes (NAs)", int(df.isnull().sum().sum()))
       
       
        # Análise estatística
        st.subheader("Descrição dos Dados")
        st.dataframe(df.describe()) 


        # Visualização dos dados
        st.markdown("### Visualização das Observações")
        
        # Criar DataFrame com índice começando em 1
        df_display = df.copy()
        df_display.index = range(1, len(df) + 1)
        
        values = st.slider(
            "Selecione o intervalo de observações:",
            min_value=1,
            max_value=len(df),
            value=(1, min(5, len(df))),
            step=1
        )
        st.dataframe(df_display.iloc[values[0]-1:values[1]])
        
    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {str(e)}")
else:
    st.info("👆 Por favor, faça upload de um arquivo de dados para começar a análise")

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
            <img src='https://img.icons8.com/?size=100&id=SzgQDfObXUbA&format=png&color=000000' width='40'/>
        </a>
        <a href='https://wa.me/5571991216019' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/whatsapp.png' width='40'/>
        </a>
        <a href='https://www.linkedin.com/in/dataconst-jr-992375355/' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/linkedin.png' width='40'/>
        </a>
    </div>
    """, unsafe_allow_html=True) 
