from datetime import datetime, timezone
from dotenv import load_dotenv, find_dotenv
from crewai import Agent, Task, Crew
from IPython.display import display, Markdown

load_dotenv(find_dotenv())
game_time = datetime.now(timezone.utc)

# Eventos com tradução
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

def get_surrounding_events(game_time):
    current_hour = game_time.hour
    sorted_events = sorted(WILDERNESS_EVENTS, key=lambda e: e["hour"])
    
    current_index = next((i for i, e in enumerate(sorted_events) if e["hour"] == current_hour), None)
    
    if current_index is not None:
        previous_event = sorted_events[current_index - 1] if current_index > 0 else sorted_events[-1]
        current_event = sorted_events[current_index]
        next_event = sorted_events[(current_index + 1) % len(sorted_events)]
    else:
        previous_event = max([e for e in sorted_events if e["hour"] < current_hour], default=sorted_events[-1])
        next_event = min([e for e in sorted_events if e["hour"] > current_hour], default=sorted_events[0])
        current_event = None

    return previous_event, current_event, next_event

prev_event, current_event, next_event = get_surrounding_events(game_time)

event_reporter = Agent(
    role='Gerador de Relatório de Eventos',
    goal='Gerar uma visão geral dos eventos Wilderness do RuneScape',
    backstory='Especialista em eventos com suporte multilíngue.',
    verbose=True
)

report_task = Task(
    description=f"""
    Criar relatório dos eventos com nomes traduzidos pt-BR.
    """,
    expected_output=f"""
## Wilderness Flash Events Report - UTC {game_time.strftime('%H:%M')}

### 🔙 Evento Anterior ({prev_event['hour']:02d}:00 UTC)
🗓️ **{prev_event['name']} | {prev_event['translated']}**  
🏷️ Tipo: {prev_event['type']}  
⭐ Tier: {prev_event['tier']} {"📦" if prev_event['tier'] == "Especial" else ""}

### ⏰ Evento Atual ({current_event['hour']:02d}:00 UTC)
🔥 **{current_event['name']} | {current_event['translated']}**  
🏷️ Tipo: {current_event['type']}  
⭐ Tier: {current_event['tier']} {"📦" if current_event['tier'] == "Especial" else ""}

### ⏭️ Próximo Evento ({next_event['hour']:02d}:00 UTC)
🕒 **{next_event['name']} | {next_event['translated']}**  
🏷️ Tipo: {next_event['type']}  
⭐ Tier: {next_event['tier']} {"📦" if next_event['tier'] == "Especial" else ""}
""",
    agent=event_reporter
)

crew = Crew(
    agents=[event_reporter],
    tasks=[report_task],
    verbose=True
)

resultado = crew.kickoff()
print(resultado.raw)
display(Markdown(str(resultado)))

with open("wilderness_events_translated_report.md", "w", encoding="utf-8") as file:
    file.write(str(resultado))
