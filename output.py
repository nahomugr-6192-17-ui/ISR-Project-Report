def write_results(results, filename):
    with open(filename, 'w') as f:
        for qid in results:
            for rank, (docno, score) in enumerate(results[qid], start=1):
                f.write(f"{qid} Q0 {docno} {rank} {score} Exp\n")