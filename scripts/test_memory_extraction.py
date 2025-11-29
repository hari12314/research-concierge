import sys
import os
from PyPDF2 import PdfReader  # pip install PyPDF2

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.extractor_agent import ExtractorAgent
from memory.memory_bank import MemoryBank

# PDF Parser class using PyPDF2
class PDFParser:
    def extract_text(self, pdf_path):
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

# PDF path
pdf_path = r"C:\Users\DELL\research-concierge\sample.pdf"

# Initialize parser and extractor
parser = PDFParser()
extractor = ExtractorAgent()

# Extract text from PDF
text = parser.extract_text(pdf_path)

# Session ID
session_id = "test_session"

# Extract metadata using the extractor agent
output = extractor.extract(session_id, text)

print("\n=== Extracted Metadata ===")
print(output)

# Access memory stored in extractor
print("\n=== Memory Stored in Extractor ===")
print(extractor.memory.memory_store[session_id])
