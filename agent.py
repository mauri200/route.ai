# agent.py
from managed_deepagents import define_deep_agent
from tools.search import internet_search
from tools.custom_tools import (
    read_local_pdf,
    generate_export_contract_pdf,
    send_purchase_rfq,
    fetch_unread_buyer_emails,
)

agent = define_deep_agent(
    name="route-ai",
    model="nebius:meta-llama/Llama-3.3-70B-Instruct",  # O el identificador exacto del modelo en Nebius Token Factory
    tools=[
        internet_search,
        read_local_pdf,
        generate_export_contract_pdf,
        send_purchase_rfq,
        fetch_unread_buyer_emails,
    ],
)