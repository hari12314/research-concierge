# apis/arxiv_api.py
import requests
import xml.etree.ElementTree as ET

class ArxivAPI:
    BASE_URL = "http://export.arxiv.org/api/query"

    def search(self, query, max_results=5):
        params = {
            "search_query": f"all:{query}",
            "start": 0,
            "max_results": max_results
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        results = []
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            title = entry.find("{http://www.w3.org/2005/Atom}title").text
            authors = [author.find("{http://www.w3.org/2005/Atom}name").text
                       for author in entry.findall("{http://www.w3.org/2005/Atom}author")]
            results.append({"title": title, "authors": authors})
        return results
