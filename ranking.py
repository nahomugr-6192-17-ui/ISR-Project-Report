def rank_documents(queries, avg_doc_len, D):
    results = {}

    for qid, terms in queries.items():
        scores = {}

        for term in terms:
            df, docs = get_term_stats(term)

            for docno, tf, doc_len in docs:
                score = tf_idf(tf, df, D, doc_len, avg_doc_len)

                if docno not in scores:
                    scores[docno] = 0

                scores[docno] += score

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        results[qid] = ranked[:100]

    return results