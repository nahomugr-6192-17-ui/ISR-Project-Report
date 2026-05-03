from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
INDEX_NAME = "cranfield"

def get_term_stats(term):
    query = {
        "query": {
            "match": {
                "text": term
            }
        },
        "size": 1000
    }

    res = es.search(index=INDEX_NAME, body=query)

    df = res['hits']['total']['value']
    docs = []

    for hit in res['hits']['hits']:
        docno = hit['_id']
        text = hit['_source']['text']

        tf = text.lower().split().count(term)
        doc_len = len(text.split())

        docs.append((docno, tf, doc_len))

    return df, docs
