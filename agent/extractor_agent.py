from memory.memory_bank import MemoryBank

class ExtractorAgent:
    def __init__(self):
        self.memory = MemoryBank()

    def extract(self, session_id, pdf_text):
        self.memory.store_pdf_memory(session_id, pdf_text)

        extracted = {
            "full_text": pdf_text,
            "summary": self._extract_summary(pdf_text),
            "keywords": self._extract_keywords(pdf_text)
        }
        return extracted

    def _extract_summary(self, text):
        return text[:500]  # first 500 chars

    def _extract_keywords(self, text):
        words = text.split()
        return list(set(words))[:20]
