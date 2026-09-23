import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuração da Página
st.set_page_config(
    page_title="Value Engine Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título Principal
st.title("🎯 Value Engine Platform — VMO & Governança")
st.caption("Plataforma de Gestão de Valor, Priorização de Portfólio e Análise Financeira")

st.divider()

# Sidebar para Navegação dos Módulos
st.sidebar.header("🧭 Módulos do Sistema")
modulo = st.sidebar.radio(
    "Selecione o módulo:",
    [
        "1. Visão Geral do Portfólio",
        "2. Detalhamento JTBD & Outcomes",
        "3. Monetização de Proxies",
        "4. Calculadora Financeira (ROI/NPV)",
        "5. Otimização (Fronteira Eficiente)"
    ]
)

# MÓDULO 1: VISÃO GERAL
if modulo == "1. Visão Geral do Portfólio":
    st.subheader("📌 Painel de Controle do Portfólio")
    
    # KPIs Rápidos
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Projetos no Portfólio", "12", "+2 este mês")
    col2.metric("CAPEX Total", "R$ 4.2M", "-5% do teto")
    col3.metric("NPV Médio", "R$ 1.8M", "+12% vs meta")
    col4.metric("ROI Médio Esperado", "180%", "+15 pp")
    
    st.markdown("---")
    
    # Exemplo de Gráfico Interativo de Projetos
    data_projects = pd.DataFrame({
        'Projeto': [f'Projeto {chr(65+i)}' for i in range(8)],
        'Investimento_R$': np.random.randint(100, 1000, 8) * 1000,
        'NPV_Estimado_R$': np.random.randint(200, 2000, 8) * 1000,
        'Risco': ['Baixo', 'Médio', 'Alto', 'Médio', 'Baixo', 'Alto', 'Baixo', 'Médio']
    })
    
    fig = px.scatter(
        data_projects,
        x="Investimento_R$",
        y="NPV_Estimado_R$",
        color="Risco",
        size="NPV_Estimado_R$",
        text="Projeto",
        title="Relação Investimento vs. NPV Estimado",
        labels={"Investimento_R$": "Investimento Inicial (R$)", "NPV_Estimado_R$": "NPV (R$)"}
    )
    st.plotly_chart(fig, use_container_width=True)

# MÓDULOS EM CONSTRUÇÃO
else:
    st.info(f"🚧 O módulo **'{modulo}'** está pronto na arquitetura e será implementado na próxima etapa do workflow!")
    st.markdown("Acompanhe o status e os requisitos no arquivo `SKILLS_INDEX.md` do repositório.")
