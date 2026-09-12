# 🎯 Dashboard Interativo de Busca de Vagas

Dashboard desenvolvido em Python com **Streamlit** para filtro estratégico de oportunidades de vagas em Piracicaba/SP e região (até 50km).

## 📋 Funcionalidades

- ✅ **Filtros Interativos**: Cidade, Área de Atuação e Match com Currículo
- 📊 **Métricas em Tempo Real**: Total de vagas, vagas em Piracicaba, oportunidades com alto match
- 📈 **Tabela Dinâmica**: Visualização de todas as oportunidades filtradas
- 💾 **Exportação em CSV**: Baixe as vagas filtradas para análise offline
- 🔗 **Links Diretos**: Acesso rápido para cada vaga nas plataformas

## 🚀 Início Rápido

### Pré-requisitos
- Python 3.8+
- pip

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/gleisonquartarolo-max/job-search-dashboard.git
cd job-search-dashboard
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o dashboard:
```bash
streamlit run app.py
```

4. Abra seu navegador e acesse: `http://localhost:8501`

## 📁 Estrutura do Projeto

```
job-search-dashboard/
├── app.py              # Aplicação principal do Streamlit
├── requirements.txt    # Dependências Python
└── README.md          # Este arquivo
```

## 🎨 Seções do Dashboard

### 🔍 Barra Lateral - Filtros
- Seleção de cidades (até 50km)
- Áreas de atuação
- Slider para match mínimo com currículo

### 📊 Métricas Principais
- Total de vagas encontradas
- Vagas em Piracicaba/SP
- Oportunidades com match >90%
- Vagas postadas nas últimas 24 horas

### 📋 Tabela de Resultados
- Cargo, Empresa, Cidade
- Área, Data de Postagem, Plataforma
- Porcentagem de match
- Links diretos para as vagas

### 💾 Exportação
- Botão para download em CSV das vagas filtradas

## 🔄 Próximas Melhorias

- [ ] Integração com Web Scraping (LinkedIn, Indeed, Catho)
- [ ] Integração com APIs de plataformas de vagas
- [ ] Análise de tendências com gráficos
- [ ] Sistema de notificações por email
- [ ] Armazenamento em banco de dados (SQLite/PostgreSQL)
- [ ] Autenticação de usuários
- [ ] Dashboard de histórico de candidaturas

## 📧 Contato

**Gleison Quartarolo**

---

**Desenvolvido com ❤️ usando Streamlit**