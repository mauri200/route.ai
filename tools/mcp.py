# tools/mcp.py
from managed_deepagents import define_mcp

mcp = define_mcp(
    servers={
        "tavily_search": {
            "transport": "http",
            "url": "https://mcp.tavily.com/mcp",
        },
        "email_mcp": {
            "transport": "http",
            "url": "https://api.email-mcp-server.com/mcp",
        },
        "pdf_mcp": {
            "transport": "http",
            "url": "https://api.pdf-reader-mcp.com/mcp",
        },
    },
)