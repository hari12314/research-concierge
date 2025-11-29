import sys
import os
# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.extractor_agent import ExtractorAgent
from memory.memory_bank import MemoryBank
from scripts.test_pdf_parser import PDFParser  # make sure this exists

# -----------------------------
# CONFIG
# -----------------------------
pdf_path = r"C:\Users\DELL\research-concierge\sample.pdf"
session_id = "week4_session"

# -----------------------------
# INITIALIZE
# -----------------------------
parser = PDFParser()
extractor = ExtractorAgent()
memory = MemoryBank()

# -----------------------------
# EXTRACT PDF TEXT
# -----------------------------
pdf_text = parser.extract_text(pdf_path)

# -----------------------------
# EXTRACT METADATA
# -----------------------------
metadata = extractor.extract(session_id, pdf_text)

print("\n=== Extracted Metadata ===")
print(metadata)

# -----------------------------
# STORE IN MEMORY
# -----------------------------
memory.store_pdf_memory(session_id, pdf_text, metadata)
print("\n=== Memory after storing PDF ===")
for entry in memory.get_pdf_memory(session_id):
    print(entry)

# -----------------------------
# PAUSE & RESUME
# -----------------------------
memory.pause_session(session_id)
memory.resume_session(session_id)

print("\n=== Memory after pause/resume ===")
for entry in memory.get_pdf_memory(session_id):
    print(entry)
