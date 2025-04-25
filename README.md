# Wilderness Flash Events Reporter

Este projeto tem como objetivo gerar relatórios sobre os eventos flash do Wilderness do jogo RuneScape. Os eventos são analisados e classificados por hora, e o relatório é gerado com os nomes traduzidos para o português brasileiro.

## Funcionalidades

- **Eventos do Wilderness**: O script coleta e organiza os eventos do Wilderness com base na hora atual (em UTC).
- **Tradução**: Todos os eventos possuem nomes traduzidos para o português brasileiro.
- **Relatório Dinâmico**: O relatório gerado inclui o evento anterior, o evento atual e o próximo evento, com informações como tipo e tier.
- **Saída em Markdown**: O relatório é gerado em formato Markdown e salvo em um arquivo `.md`.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **`dotenv`**: Carregamento de variáveis de ambiente.
- **`crewai`**: Framework para criação de agentes e tarefas para automação de processos.
- **`IPython.display`**: Para exibição de relatórios no Jupyter.

## Como Usar

1. **Instalar Dependências**:
   - Clone o repositório.
   - Crie um ambiente virtual (opcional, mas recomendado).
   - Instale as dependências:
     ```bash
     pip install -r requirements.txt
     ```

2. **Configuração de Ambiente**:
   - Crie um arquivo `.env` e defina as variáveis de ambiente necessárias (caso haja alguma configuração específica).

3. **Executar o Script**:
   - O script é projetado para ser executado diretamente. Para gerar o relatório, basta rodar:
     ```bash
     python generate_report.py
     ```

4. **Saída**:
   - O relatório será gerado e exibido na tela.
   - Também será salvo como `wilderness_events_translated_report.md`.
