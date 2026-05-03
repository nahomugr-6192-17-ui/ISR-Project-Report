def lm_laplace(tf, doc_len, V):
    return math.log((tf + 1) / (doc_len + V))