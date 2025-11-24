# Projeto Streamlit - Aplicação Interativa

## Descrição

Este é um projeto educacional que demonstra os principais componentes e funcionalidades do **Streamlit**, uma biblioteca Python para criar aplicações web interativas com facilidade.

## Funcionalidades

A aplicação inclui exemplos de:

- **Títulos e Headers**: Estruturação de conteúdo com títulos em diferentes níveis
- **Formatação de Texto**: Suporte a negrito, itálico e riscado usando Markdown
- **Entradas do Usuário**:
  - Texto (text_input)
  - Números (number_input)
  - Data (date_input)
  - Hora (time_input)

- **Componentes de Seleção**:
  - Checkbox (seleção binária)
  - Radio buttons (seleção única)
  - Selectbox (menu suspenso)
  - Slider (controle deslizante)

- **Botões e Interatividade**: Botões clicáveis com resposta imediata

- **Manipulação de Dados**: Exibição de DataFrames com Pandas em diferentes formatos

## Requisitos

- Python 3.7+
- Streamlit
- Pandas

## Instalação

1. Clone ou baixe este projeto
2. Instale as dependências:

```bash
pip install streamlit pandas
```

## Como Executar

Execute o seguinte comando no terminal:

```bash
streamlit run app.py
```

A aplicação será aberta em seu navegador padrão no endereço `http://localhost:8501`

## Estrutura do Código

- **Exibição de conteúdo**: Usando `st.title()`, `st.header()`, `st.write()` e `st.markdown()`
- **Entrada de dados**: Captura de informações do usuário através de formulários interativos
- **Lógica condicional**: Processamento de dados baseado em entradas do usuário
- **Exibição de tabelas**: Apresentação de dados estruturados em DataFrames

## Exemplo de Uso

1. Digite seu nome e idade
2. Selecione seu gênero musical favorito
3. Indique seu humor do dia
4. Visualize os dados tabulados na aplicação

## Autor

Projeto educacional para a disciplina de CPRO

## Licença

Livre para uso educacional
