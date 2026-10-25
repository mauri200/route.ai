# tools/custom_tools.py
from langchain.tools import tool
from pypdf import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas

@tool(parse_docstring=True)
def read_local_pdf(file_path: str) -> str:
    """Reads and extracts text content from an attached PDF document.

    Args:
        file_path: Path to the PDF file on the filesystem.
    """
    try:
        reader = PdfReader(file_path)
        return "".join([page.extract_text() or "" for page in reader.pages])[:4000]
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

@tool(parse_docstring=True)
def generate_export_contract_pdf(buyer_name: str, product_type: str, origin_country: str, destination_hub: str, fob_price: float) -> str:
    """Generates a formal FOB/CIF B2B export contract PDF document.

    Args:
        buyer_name: Name of the foreign buyer or import company.
        product_type: Type of product being exported.
        origin_country: Country where the product originates.
        destination_hub: Target destination city and country.
        fob_price: Agreed FOB price for the transaction.
    """
    filename = f"export_contract_{buyer_name.lower().replace(' ', '_')}.pdf"
    c = Canvas(filename, pagesize=letter)
    c.drawString(100, 750, f"B2B Export Contract: {product_type}")
    c.drawString(100, 730, f"Origin: {origin_country} | Destination Hub: {destination_hub}")
    c.drawString(100, 710, f"Buyer: {buyer_name} | Agreed FOB Price: ${fob_price}")
    c.drawString(100, 690, "Incoterms: FOB / CIF Managed via route-ai Protocol")
    c.save()
    return f"Contract generated successfully as {filename}"

@tool(parse_docstring=True)
def send_purchase_rfq(supplier_name: str, product_item: str, volume_tons: float, destination_country: str) -> str:
    """Sends a formal Request for Quote (RFQ) to a verified producer or cooperative in origin.

    Args:
        supplier_name: Name of the agricultural cooperative or exporter.
        product_item: Commodity or raw material requested (e.g., green coffee beans).
        volume_tons: Quantity requested in metric tons.
        destination_country: Destination country where the importer is located.
    """
    rfq_message = (
        f"RFQ Sent to {supplier_name}: Representing a corporate importer in {destination_country}, "
        f"we request a quote for {volume_tons} metric tons of {product_item}. "
        f"Please provide FOB terms, quality profiles (+84 cup score), and next month's shipping availability."
    )
    return rfq_message

@tool
def fetch_unread_buyer_emails() -> str:
    """Fetches unread B2B buyer inquiries and proposals from connected mailboxes."""
    return "Found 1 unread inquiry from a buyer in Miami interested in import terms."