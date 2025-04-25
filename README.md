
# Wilderness Flash Events Notifier

Este script envia notificações sobre os eventos de flash do Wilderness no jogo, exibindo o evento anterior, o atual e o próximo, em tempo real.

## Descrição

Este código coleta os dados sobre os eventos programados no Wilderness e envia uma mensagem via Telegram para um chat específico, contendo informações sobre:

- Evento anterior
- Evento atual
- Próximo evento

Os eventos são classificados por hora e incluem detalhes sobre o tipo e o nível do evento.

## Pré-requisitos

Antes de executar este script, é necessário ter o seguinte:

- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `python-dotenv`
  
Você pode instalar as dependências com o seguinte comando:

```bash
pip install requests python-dotenv
```

## Configuração

1. Crie um arquivo `.env` na raiz do seu projeto e adicione as seguintes variáveis de ambiente:

    ```
    TELEGRAM_BOT_TOKEN=seu_token_aqui
    TELEGRAM_CHAT_ID=seu_chat_id_aqui
    ```

    - `TELEGRAM_BOT_TOKEN`: O token do seu bot do Telegram. Você pode obtê-lo conversando com o [BotFather](https://core.telegram.org/bots#botfather) no Telegram.
    - `TELEGRAM_CHAT_ID`: O ID do chat onde as notificações serão enviadas.

2. Certifique-se de que as variáveis de ambiente estão sendo carregadas corretamente com o `python-dotenv`.

## Como Usar

1. Execute o script Python:

    ```bash
    python script.py
    ```

2. O script enviará uma mensagem para o Telegram com os eventos de flash do Wilderness.

## Exemplo de Mensagem

O script enviará uma mensagem formatada no seguinte estilo:

```
📢 Wilderness Flash Events - UTC 14:00

🔙 Evento Anterior (13:00)
🗓️ Enxame de Borboletas | Butterfly Swarm
🏷️ Skilling | ⭐ Normal

⏰ Evento Atual (14:00)
🔥 Devastação do Rei Dragão Negro | King Black Dragon Rampage
🏷️ Combat | ⭐ Especial 📦

⏭️ Próximo Evento (15:00)
🕒 Soldados Esquecidos | Forgotten Soldiers
🏷️ Combat | ⭐ Normal
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).