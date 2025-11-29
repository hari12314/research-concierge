from apis.crossref_api import CrossRefAPI
from apis.arxiv_api import ArxivAPI

crossref = CrossRefAPI()
arxiv = ArxivAPI()

print(crossref.search("Machine Learning"))
print(arxiv.search("Machine Learning"))
