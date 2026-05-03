def bm25(tf, df, D, doc_len, avg_doc_len, tf_q=1, k1=1.2, b=0.75, k2=100):
    idf = math.log((D + 0.5) / (df + 0.5))

    part1 = (tf * (k1 + 1)) / (tf + k1 * ((1 - b) + b * (doc_len / avg_doc_len)))
    part2 = (tf_q * (k2 + 1)) / (tf_q + k2)

    return idf * part1 * part2
