from scripts.test_pdf_parser import PDFParser
from agent.coordinator_agent import CoordinatorAgent
from agent.extractor_agent import ExtractorAgent

# PDF path
pdf_path = r"C:\Users\DELL\research-concierge\sample.pdf"

# Initialize parser, coordinator, and extractor
parser = PDFParser()
extractor = ExtractorAgent()
coordinator = CoordinatorAgent()

# Extract PDF text using PDFParser
pdf_text = parser.extract_text(pdf_path)

# Session ID
session_id = "test_session"

# Pass extracted text to extractor (or coordinator pipeline)
output = extractor.extract(session_id, pdf_text)

print("\n=== Extracted Metadata ===")
print(output)

# Optional: access memory
print("\n=== Memory Stored in Extractor ===")
print(extractor.memory.memory_store[session_id])
