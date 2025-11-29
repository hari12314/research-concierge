# memory/memory_bank.py

import pickle
import os
from datetime import datetime

class MemoryBank:
    """Persistent memory for sessions with PDFs and metadata."""
    
    def __init__(self, persist_file="memory_store.pkl"):
        self.memory_store = {}  # session_id -> list of PDFs & metadata
        self.persist_file = persist_file
        self._load_memory()

    def store_pdf_memory(self, session_id, pdf_text, metadata=None):
        """Store PDF text and metadata for a session."""
        if session_id not in self.memory_store:
            self.memory_store[session_id] = []
        entry = {
            "timestamp": datetime.now(),
            "pdf_text": pdf_text,
            "metadata": metadata or {}
        }
        self.memory_store[session_id].append(entry)
        self._save_memory()

    def get_pdf_memory(self, session_id):
        """Retrieve all PDF entries for a session."""
        return self.memory_store.get(session_id, [])

    def pause_session(self, session_id):
        """Mark session as paused."""
        if session_id in self.memory_store:
            self.memory_store[session_id].append({"status": "paused", "timestamp": datetime.now()})
            self._save_memory()

    def resume_session(self, session_id):
        """Mark session as resumed."""
        if session_id in self.memory_store:
            self.memory_store[session_id].append({"status": "resumed", "timestamp": datetime.now()})
            self._save_memory()

    def _save_memory(self):
        """Persist memory to disk."""
        with open(self.persist_file, "wb") as f:
            pickle.dump(self.memory_store, f)

    def _load_memory(self):
        """Load memory from disk if exists."""
        if os.path.exists(self.persist_file):
            with open(self.persist_file, "rb") as f:
                self.memory_store = pickle.load(f)
