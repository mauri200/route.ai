# schedules/matchmaker.py
from managed_deepagents import define_schedule

schedule = define_schedule(
    cron="*/10 * * * *",  # Se ejecuta cada 10 minutos en segundo plano
    timezone="UTC",
    prompt=(
        "Run the automated closed-loop matching engine. "
        "Scan registered profiles for unmatched supply (e.g., Colombian coffee sellers) "
        "and demand (e.g., Spanish roastery buyers). "
        "Simulate asynchronous negotiation between the seller agent and buyer agent, "
        "optimize Incoterms, and trigger automated RFQ emails and contract PDFs."
    ),
)