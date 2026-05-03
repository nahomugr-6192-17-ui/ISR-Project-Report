import re

def process_query(query):
    query = query.lower()
    query = re.sub(r'[^a-z0-9\s]', '', query)
    tokens = query.split()
    return tokens

def load_queries(file_path):
    queries = {}

    with open(file_path, 'r') as f:
        for line in f:
            if ":" in line:
                qid, text = line.split(":", 1)
                queries[qid.strip()] = process_query(text.strip())

    return queries

if __name__ == "__main__":
    queries = load_queries("query_desc.51-100.short.txt")

    for qid, tokens in queries.items():
        print(qid, tokens)