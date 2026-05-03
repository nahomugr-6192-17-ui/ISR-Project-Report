from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup
import re

es = Elasticsearch("http://localhost:9200")
INDEX_NAME = "cranfield"

def create_index():
    if es.indices.exists(index=INDEX_NAME):
        es.indices.delete(index=INDEX_NAME)

    es.indices.create(index=INDEX_NAME)

def index_documents(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, "xml")
    docs = soup.find_all("doc")

    for doc in docs:
        docno = doc.find("docno").text.strip()
        title = doc.find("title").text.strip()
        author = doc.find("author").text.strip()
        bib = doc.find("bib").text.strip()
        text = doc.find("text").text.strip()

        # clean text
        text = re.sub(r'\s+', ' ', text)

        json_doc = {
            "title": title,
            "author": author,
            "bib": bib,
            "text": text
        }

        es.index(index=INDEX_NAME, id=docno, document=json_doc)

def main():
    create_index()
    index_documents("cran.all.1400.xml")

if __name__ == "__main__":
    main()