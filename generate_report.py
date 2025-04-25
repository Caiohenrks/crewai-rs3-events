from datetime import datetime, timezone
from dotenv import load_dotenv, find_dotenv
import os
import requests

# Carrega variáveis de ambiente
load_dotenv(find_dotenv())

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

game_time = datetime.now(timezone.utc)

WILDERNESS_EVENTS = [
    {"name": "Surprising Seedlings", "translated": "Mudas Surpreendentes", "hour": 2, "type": "Skilling", "tier": "Normal"},
    {"name": "Hellhound Pack", "translated": "Matilha de Cães do Inferno", "hour": 3, "type": "Combat", "tier": "Normal"},
    {"name": "Infernal Star", "translated": "Estrela Infernal", "hour": 4, "type": "Skilling/Combat", "tier": "Especial"},
    {"name": "Lost Souls", "translated": "Almas Perdidas", "hour": 5, "type": "Skilling/Combat", "tier": "Normal"},
    {"name": "Ramokee Incursion", "translated": "Incursão Ramokee", "hour": 6, "type": "Combat", "tier": "Normal"},
    {"name": "Displaced Energy", "translated": "Energia Deslocada", "hour": 7, "type": "Skilling", "tier": "Normal"},
    {"name": "Evil Bloodwood Tree", "translated": "Árvore de Sanguinária Maligna", "hour": 8, "type": "Skilling", "tier": "Especial"},
    {"name": "Spider Swarm", "translated": "Enxame de Aranhas", "hour": 9, "type": "Combat", "tier": "Normal"},
    {"name": "Unnatural Outcrop", "translated": "Afloramento Anormal", "hour": 10, "type": "Skilling", "tier": "Normal"},
    {"name": "Stryke the Wyrm", "translated": "Stryke o Verme", "hour": 11, "type": "Combat", "tier": "Especial"},
    {"name": "Demon Stragglers", "translated": "Demônios Retardatários", "hour": 12, "type": "Combat", "tier": "Normal"},
    {"name": "Butterfly Swarm", "translated": "Enxame de Borboletas", "hour": 13, "type": "Skilling", "tier": "Normal"},
    {"name": "King Black Dragon Rampage", "translated": "Devastação do Rei Dragão Negro", "hour": 14, "type": "Combat", "tier": "Especial"},
    {"name": "Forgotten Soldiers", "translated": "Soldados Esquecidos", "hour": 15, "type": "Combat", "tier": "Normal"}
]

def get_surrounding_events(current_hour):
    sorted_events = sorted(WILDERNESS_EVENTS, key=lambda e: e["hour"])
    current_index = next((i for i, e in enumerate(sorted_events) if e["hour"] == current_hour), None)
    
    if current_index is not None:
        prev_event = sorted_events[current_index - 1] if current_index > 0 else sorted_events[-1]
        curr_event = sorted_events[current_index]
        next_event = sorted_events[(current_index + 1) % len(sorted_events)]
    else:
        prev_event = max([e for e in sorted_events if e["hour"] < current_hour], default=sorted_events[-1])
        curr_event = None
        next_event = min([e for e in sorted_events if e["hour"] > current_hour], default=sorted_events[0])
    
    return prev_event, curr_event, next_event

prev_event, current_event, next_event = get_surrounding_events(game_time.hour)

telegram_message = f"""
📢 Wilderness Flash Events - UTC {game_time.strftime('%H:%M')}

🔙 Evento Anterior ({prev_event['hour']:02d}:00)
🗓️ {prev_event['name']} | {prev_event['translated']}
🏷️ {prev_event['type']} | ⭐ {prev_event['tier']} {'📦' if prev_event['tier'] == 'Especial' else ''}

⏰ Evento Atual ({current_event['hour']:02d}:00)
🔥 {current_event['name']} | {current_event['translated']}
🏷️ {current_event['type']} | ⭐ {current_event['tier']} {'📦' if current_event['tier'] == 'Especial' else ''}

⏭️ Próximo Evento ({next_event['hour']:02d}:00)
🕒 {next_event['name']} | {next_event['translated']}
🏷️ {next_event['type']} | ⭐ {next_event['tier']} {'📦' if next_event['tier'] == 'Especial' else ''}
"""

# Enviar mensagem
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": telegram_message.strip()
}
response = requests.post(url, json=payload)
print(response.json())
