# Dashboard Financeiro Interativo

Este é um projeto de um **Dashboard Financeiro Interativo** desenvolvido com [Streamlit](https://streamlit.io/), que permite a visualização de dados financeiros simulados (receitas, despesas e saldo) e a interação com os dados por meio de filtros, gráficos e estatísticas. Além disso, há uma opção para download dos dados filtrados em formato CSV.

## Funcionalidades

- **Visualização gráfica** das receitas, despesas e saldo financeiro ao longo dos meses.
- **Filtro de período** interativo para selecionar quais meses serão exibidos no dashboard.
- **Gráficos interativos** gerados com a biblioteca [Plotly](https://plotly.com/python/):
  - Gráfico de barras comparando receitas e despesas.
  - Gráfico de linha mostrando o saldo acumulado mês a mês.
- **Estatísticas financeiras** automáticas, como o total de receitas, despesas e saldo final, exibidas na barra lateral.
- **Exportação de dados filtrados** em CSV para download.

## Instalação

1. Clone este repositório em sua máquina local:

    ```bash
    git clone https://github.com/vbertotto/dashboard-financeiro.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd dashboard-financeiro
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

4. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

## Como Executar

Após instalar as dependências, você pode iniciar o dashboard com o comando:

```bash
streamlit run app.py
