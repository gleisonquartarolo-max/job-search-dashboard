import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Dashboard de Vagas - Gleison Quartarolo", layout="wide")

# Título e Resumo
st.title("🎯 Painel Interativo de Busca de Vagas")
st.caption("Filtro estratégico para Piracicaba/SP (+50km) | Gestão, Logística, Contratos e Processos")

# Dados simulados (Estrutura pronta para integração com Web Scraping/API)
data = [
    {"Cargo": "Coordenador de Logística", "Empresa": "LogiCorp", "Cidade": "Piracicaba/SP", "Área": "Logística", "Postado": "Há 6h", "Plataforma": "LinkedIn", "Match (%)": 95, "Link": "https://linkedin.com"},
    {"Cargo": "Gerente de Operações", "Empresa": "Indústria Metal", "Cidade": "Americana/SP", "Área": "Operações", "Postado": "Há 14h", "Plataforma": "Indeed", "Match (%)": 90, "Link": "https://indeed.com"},
    {"Cargo": "Supervisor de Contratos", "Empresa": "TransSupply", "Cidade": "Limeira/SP", "Área": "Contratos", "Postado": "Há 22h", "Plataforma": "Catho", "Match (%)": 88, "Link": "https://catho.com.br"},
    {"Cargo": "Gestor de Processos", "Empresa": "AgroTech", "Cidade": "Piracicaba/SP", "Área": "Processos", "Postado": "Há 30h", "Plataforma": "Sólides", "Match (%)": 85, "Link": "https://solides.com.br"},
    {"Cargo": "Supervisor de Suprimentos", "Empresa": "AutoParts", "Cidade": "Santa Bárbara d'Oeste/SP", "Área": "Suprimentos", "Postado": "Há 40h", "Plataforma": "Vagas.com", "Match (%)": 82, "Link": "https://vagas.com.br"}
]

df = pd.DataFrame(data)

# BARRA LATERAL - FILTROS INTERATIVOS
st.sidebar.header("🔍 Filtros de Busca")

cidades_selecionadas = st.sidebar.multiselect(
    "Cidade / Raio (até 50km):",
    options=df["Cidade"].unique(),
    default=df["Cidade"].unique()
)

areas_selecionadas = st.sidebar.multiselect(
    "Área de Atuação:",
    options=df["Área"].unique(),
    default=df["Área"].unique()
)

match_minimo = st.sidebar.slider("Match Mínimo com Currículo (%):", 50, 100, 80)

# Aplicação dos filtros no DataFrame
df_filtrado = df[
    (df["Cidade"].isin(cidades_selecionadas)) &
    (df["Área"].isin(areas_selecionadas)) &
    (df["Match (%)"] >= match_minimo)
]

# MÉTRICAS PRINCIPAIS
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Vagas Encontradas", len(df_filtrado))
col2.metric("Vagas em Piracicaba", len(df_filtrado[df_filtrado["Cidade"] == "Piracicaba/SP"]))
col3.metric("Oportunidades >90% Match", len(df_filtrado[df_filtrado["Match (%)"] >= 90]))
col4.metric("Últimas 24 Horas", len(df_filtrado[df_filtrado["Postado"].str.contains("6h|14h|22h")]))

st.divider()

# TABELA INTERATIVA DE RESULTADOS
st.subheader("📋 Oportunidades Filtradas (Últimas 48h)")

st.dataframe(
    df_filtrado,
    column_config={
        "Link": st.column_config.LinkColumn("Link Direto", display_text="Acessar Vaga"),
        "Match (%)": st.column_config.ProgressColumn("Aderência ao Perfil", format="%d%%", min_value=0, max_value=100)
    },
    hide_index=True,
    use_container_width=True
)

# SEÇÃO DE EXPORTAÇÃO
st.download_button(
    label="📥 Exportar Vagas Filtradas (CSV)",
    data=df_filtrado.to_csv(index=False).encode('utf-8'),
    file_name='vagas_filtradas.csv',
    mime='text/csv'
)
