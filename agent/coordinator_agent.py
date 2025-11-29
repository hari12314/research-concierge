from memory.memory_bank import MemoryBank
from scripts.test_pdf_parser import PDFParser
from agent.extractor_agent import ExtractorAgent  # integrate Extractor

class CoordinatorAgent:
    """Coordinator for PDF processing with session support and metadata extraction."""

    def __init__(self):
        self.memory = MemoryBank()
        self.parser = PDFParser()
        self.extractor = ExtractorAgent()
        print("[Coordinator] Ready")

    def process_pdf(self, session_id, pdf_path):
        # Extract text from PDF
        pdf_text = self.parser.extract_text(pdf_path)
        
        # Extract metadata using ExtractorAgent
        extracted_metadata = self.extractor.extract(session_id, pdf_text)
        
        # Store both text and metadata in MemoryBank
        self.memory.store_pdf_memory(session_id, pdf_text, extracted_metadata)
        return extracted_metadata

    def pause_session(self, session_id):
        self.memory.pause_session(session_id)

    def resume_session(self, session_id):
        self.memory.resume_session(session_id)

    def get_session_memory(self, session_id):
        return self.memory.get_pdf_memory(session_id)
