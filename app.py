import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuração da Página
st.set_page_config(
    page_title="Value Engine Platform",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo Customizado de KPIs
st.markdown("""
<style>
    .stMetric {
        background-color: #f6f6f6;
        padding: 15px;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎯 Value Engine Platform — VMO & Governança")
st.caption("Plataforma Integrada de Priorização de Portfólio, JTBD e Gestão de Outcomes")

st.divider()

# Sidebar de Navegação
st.sidebar.header("🧭 Navegação de Módulos")
modulo = st.sidebar.radio(
    "Ir para:",
    [
        "1. Visão Geral do Portfólio",
        "2. Detalhamento JTBD & Outcomes",
        "3. Monetização de Proxies",
        "4. Calculadora Financeira (ROI/NPV)",
        "5. Otimização (Fronteira Eficiente)"
    ]
)

# -----------------------------------------------------------------------------
# MÓDULO 1: VISÃO GERAL
# -----------------------------------------------------------------------------
if modulo == "1. Visão Geral do Portfólio":
    st.subheader("📌 Visão Geral do Portfólio de Investimentos")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Projetos Mapeados", "8 Projetos", "+2 este mês")
    col2.metric("CAPEX Total", "R$ 4.250.000", "Dentro do limite")
    col3.metric("NPV Consolidado", "R$ 7.820.000", "Retorno positivo")
    col4.metric("ROI Médio Esperado", "184%", "+14 pp vs meta")
    
    st.markdown("---")
    
    # Base de dados simulada para exibição
    data = pd.DataFrame({
        'Projeto': ['Automação VMO', 'Portal EAD v2', 'Migração Cloud', 'IA de Atendimento', 'Data Lake Core'],
        'Investimento (R$)': [150000, 450000, 1200000, 350000, 800000],
        'NPV Esperado (R$)': [420000, 980000, 1900000, 890000, 1400000],
        'Score Oportunidade (Ulwick)': [14.2, 11.5, 9.8, 16.5, 12.1],
        'Risco': ['Baixo', 'Médio', 'Alto', 'Médio', 'Baixo']
    })
    
    col_chart, col_table = st.columns([3, 2])
    
    with col_chart:
        fig = px.scatter(
            data,
            x="Investimento (R$)",
            y="NPV Esperado (R$)",
            size="Score Oportunidade (Ulwick)",
            color="Risco",
            text="Projeto",
            title="Matriz: Investimento vs. NPV (Tamanho = Score JTBD)"
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col_table:
        st.write("### Detalhes das Iniciativas")
        st.dataframe(data, hide_index=True, use_container_width=True)

# -----------------------------------------------------------------------------
# MÓDULO 2: DETALHAMENTO JTBD & OUTCOMES
# -----------------------------------------------------------------------------
elif modulo == "2. Detalhamento JTBD & Outcomes":
    st.subheader("💡 Mapeamento de JTBD (Jobs-To-Be-Done) & Desired Outcomes")
    st.info("Algoritmo de Oportunidade (Anthony Ulwick): Score = Importância + max(Importância - Satisfação, 0)")
    
    st.markdown("### 📝 Calculadora de Oportunidade de Outcomes")
    
    col_input1, col_input2, col_input3 = st.columns(3)
    with col_input1:
        job_title = st.text_input("Descrição do Outcome Desejado", "Minimizar tempo de aprovação de orçamento")
    with col_input2:
        importancia = st.slider("Importância do Outcome (1 a 10)", 1, 10, 8)
    with col_input3:
        satisfacao = st.slider("Satisfação Atual (1 a 10)", 1, 10, 3)
        
    # Cálculo da Oportunidade segundo Ulwick
    score_oportunidade = importancia + max((importancia - satisfacao), 0)
    
    st.markdown("---")
    st.write(f"#### Outcome: *{job_title}*")
    
    c1, c2 = st.columns(2)
    c1.metric("Score de Oportunidade", f"{score_oportunidade:.1f} / 20.0")
    
    if score_oportunidade >= 15:
        c2.success("🔥 **Alta Oportunidade de Inovação!** (Área extremamente desatendida)")
    elif score_oportunidade >= 10:
        c2.warning("⚡ **Oportunidade Moderada.** (Vale investimento de otimização)")
    else:
        c2.error("❄️ **Sobreatendida ou Baixa Relevância.** (Não priorizar no portfólio)")

# -----------------------------------------------------------------------------
# MÓDULO 4: CALCULADORA FINANCEIRA (ROI / NPV)
# -----------------------------------------------------------------------------
elif modulo == "4. Calculadora Financeira (ROI/NPV)":
    st.subheader("🧮 Simulação de Viabilidade Financeira de Projetos")
    
    c_inv, c_taxa, c_anos = st.columns(3)
    with c_inv:
        investimento = st.number_input("Investimento Inicial - CAPEX (R$)", value=250000, step=25000)
    with c_taxa:
        tma = st.number_input("Taxa Mínima de Atratividade - TMA (% a.a.)", value=12.0, step=0.5) / 100
    with c_anos:
        anos = st.slider("Horizonte de Análise (Anos)", 1, 5, 3)
        
    st.markdown("#### Fluxo de Caixa Anual Projetado (Benefício Líquido)")
    
    fluxos = []
    cols_fluxo = st.columns(anos)
    for i, col in enumerate(cols_fluxo):
        with col:
            val = st.number_input(f"Ano {i+1} (R$)", value=(i+1)*120000, step=10000, key=f"f_{i}")
            fluxos.append(val)
            
    # Cálculos Financeiros
    npv = -investimento + sum([f / ((1 + tma) ** (idx + 1)) for idx, f in enumerate(fluxos)])
    retorno_total = sum(fluxos)
    roi = ((retorno_total - investimento) / investimento) * 100
    
    st.markdown("---")
    res1, res2, res3 = st.columns(3)
    res1.metric("Retorno Bruto Total", f"R$ {retorno_total:,.2f}")
    res2.metric("NPV (Valor Presente Líquido)", f"R$ {npv:,.2f}", delta="Viável" if npv > 0 else "Inviável")
    res3.metric("ROI Simples", f"{roi:.1f}%")

# -----------------------------------------------------------------------------
# OUTROS MÓDULOS
# -----------------------------------------------------------------------------
else:
    st.info(f"🚧 O módulo **'{modulo}'** está programado na arquitetura (`SKILLS_INDEX.md`) e será o próximo a ser implementado.")
