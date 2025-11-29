# apis/crossref_api.py
import requests

class CrossRefAPI:
    BASE_URL = "https://api.crossref.org/works"

    def search(self, query, rows=5):
        params = {"query": query, "rows": rows}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        results = []
        for item in data.get("message", {}).get("items", []):
            results.append({
                "title": item.get("title", [""])[0],
                "authors": [a.get("given", "") + " " + a.get("family", "") for a in item.get("author", [])],
                "doi": item.get("DOI", "")
            })
        return results
