def lm_jm(tf, doc_len, cf, total_terms, lamb=0.7):
    p_doc = tf / doc_len if doc_len > 0 else 0
    p_corpus = cf / total_terms

    return math.log(lamb * p_doc + (1 - lamb) * p_corpus)