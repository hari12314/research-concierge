# scripts/test_evaluation.py

from scripts.test_pdf_parser import PDFParser
from agent.extractor_agent import ExtractorAgent

# --- Config ---
PDFS = [r"C:\Users\DELL\research-concierge\sample.pdf"]  # add more PDFs here
SESSION_ID = "evaluation_session"

# Initialize agents
parser = PDFParser()
extractor = ExtractorAgent()

# Run evaluation (mock)
for pdf_path in PDFS:
    # Extract text
    pdf_text = parser.extract_text(pdf_path)
    
    # Run extraction
    result = extractor.extract(SESSION_ID, pdf_text)
    summary = result.get("summary", "")
    keywords = result.get("keywords", [])
    
    print(f"PDF: {pdf_path}")
    print(f"Summary (first 300 chars):\n{summary[:300]}...")
    print(f"Keywords: {keywords}")
    print("="*60)
