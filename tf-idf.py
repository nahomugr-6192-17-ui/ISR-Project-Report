import math

def okapi_tf(tf, doc_len, avg_doc_len):
    return tf / (tf + 0.5 + 1.5 * (doc_len / avg_doc_len))

def tf_idf(tf, df, D, doc_len, avg_doc_len):
    return okapi_tf(tf, doc_len, avg_doc_len) * math.log(D / df)
