# agent.py
from managed_deepagents import define_deep_agent
from tools.search import internet_search
from tools.custom_tools import (
    read_local_pdf,
    generate_export_contract_pdf,
    send_purchase_rfq,
    run_closed_loop_matchmaking,
    fetch_unread_buyer_emails,
)

agent = define_deep_agent(
    name="route-ai",
    # El supervisor principal usa el modelo potente para razonamiento estratégico y de contratos
    model="nebius:nvidia/nemotron-3-ultra-43b-instruct", 
    subagents=[
        {
            "name": "fast-matcher",
            "description": "Se encarga del escaneo en segundo plano de alta frecuencia, formateo rutinario de datos y consultas rápidas.",
            "system_prompt": "Eres un agente de utilidad rápida. Realiza tareas rutinarias de emparejamiento de forma rápida y eficiente.",
            # Puedes asignar un modelo rápido y ligero de Nebius para ahorrar créditos
            "model": "nebius:nvidia/nemotron-nano-4b-instruct", 
        },
        {
            "name": "compliance-auditor",
            "description": "Realiza razonamiento legal y arancelario profundo, validación aduanera y redacción de contratos.",
            "system_prompt": "Eres un experto senior en cumplimiento comercial y legal. Garantiza absoluta precisión en Incoterms y normativas.",
            "model": "nebius:nvidia/nemotron-3-ultra-43b-instruct",
        }
    ],
    tools=[
        internet_search,
        read_local_pdf,
        generate_export_contract_pdf,
        send_purchase_rfq,
        run_closed_loop_matchmaking,
        fetch_unread_buyer_emails,
    ],
)