import os
import requests

class RetrieverAgent:
    """Fetch PDFs and metadata from APIs or local paths."""

    def fetch_pdf(self, pdf_source, save_path=None):
        """
        Fetch a PDF from a URL or use a local file path.
        If save_path is provided, saves the PDF there.
        """
        # If the source is a local file, return path
        if os.path.isfile(pdf_source):
            return pdf_source

        # Else, assume it's a URL
        response = requests.get(pdf_source)
        if response.status_code == 200:
            if not save_path:
                save_path = os.path.basename(pdf_source)
            with open(save_path, "wb") as f:
                f.write(response.content)
            return save_path
        else:
            raise ValueError(f"Failed to download PDF: {pdf_source}")

    def fetch_metadata(self, doi):
        """Mock: Replace with CrossRef API call if needed"""
        return {
            "title": "Sample Paper",
            "authors": ["Author 1", "Author 2"],
            "doi": doi
        }
