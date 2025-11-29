# scripts/test_week5.py

import os
import logging
from agent.coordinator_agent import CoordinatorAgent
from agent.extractor_agent import ExtractorAgent
from memory.memory_bank import MemoryBank
from scripts.test_pdf_parser import PDFParser

# -----------------------------
# Setup logging
# -----------------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# -----------------------------
# Initialize agents and memory
# -----------------------------
logging.info("Initializing agents and memory bank...")
coordinator = CoordinatorAgent()
extractor = ExtractorAgent()
mb = MemoryBank()
parser = PDFParser()

# -----------------------------
# Define PDFs and gold metadata
# -----------------------------
pdfs = [
    {
        "file_path": r"C:\Users\DELL\research-concierge\sample.pdf",
        "gold_metadata": {
            "summary": "The dominant sequence transduction models are based on complex recurrent or convolutional networks...",
            "keywords": ["sequence", "transduction", "neural", "networks", "encoder", "decoder", "attention"]
        }
    },
    # Add more PDFs here
]

session_id = "week5_test_session"

# -----------------------------
# Process PDFs
# -----------------------------
results = []

for pdf in pdfs:
    file_path = pdf["file_path"]
    gold = pdf["gold_metadata"]

    logging.info(f"Processing PDF: {file_path}")

    # Extract text
    pdf_text = parser.extract_text(file_path)

    # Extract metadata
    extracted = extractor.extract(session_id, pdf_text)

    # Store in memory
    mb.store_pdf_memory(session_id, pdf_text, extracted)

    # -----------------------------
    # Evaluate extraction
    # -----------------------------
    # Simple metrics: check summary and keywords
    summary_match = extracted["summary"][:50] == gold["summary"][:50]
    keywords_match = any(k in extracted["keywords"] for k in gold["keywords"])

    logging.info(f"Extracted summary (first 100 chars): {extracted['summary'][:100]}")
    logging.info(f"Extracted keywords: {extracted['keywords']}")
    logging.info(f"Summary matches gold (first 50 chars)? {summary_match}")
    logging.info(f"Any keyword match? {keywords_match}")

    results.append({
        "file": file_path,
        "summary_match": summary_match,
        "keywords_match": keywords_match
    })

# -----------------------------
# Print final memory and results
# -----------------------------
logging.info("=== Memory Stored ===")
for entry in mb.get_pdf_memory(session_id):
    logging.info(entry)

logging.info("=== Evaluation Results ===")
for r in results:
    logging.info(r)

print("\n=== End of Week 5 Test ===")
