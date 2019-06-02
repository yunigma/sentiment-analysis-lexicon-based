#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
# von Iliyana Kamenova, Yeon Joo Oh, Iuliia Nigmatulina

# Big Data, FS19
# Ex04
# To run the MapReduce scripts:
# python execute_MapReducer.py ../data/lexicon/negative-words.txt ../data/lexicon/positive-words.txt ../data/


import sys
import string
import re
import os
import MapReducer

# INPUT_DIR = "../data/"
# NEG_PATH = "../data/lexicon/negative-words.txt"
# POS_PATH = "../data/lexicon/positive-words.txt"

punctuations = list(string.punctuation)
negations = ["no", "not"]

map_reduce = MapReducer.MapReducer()
neg_scores = {}
scores = {}
doc_id = 1


def mapper(doc):
    global doc_id

    document = doc.strip()
    if len(document) > 0:
        # tokens = word_tokenize(line)
        document = re.sub(r"\.|!", " ", document)
        document = document.translate(str.maketrans('', '',
                                                    string.punctuation))
        tokens = document.split()
        # clean_tokens = [t for t in tokens if re.match(r'[^\W\d]*$', t)]
        clean_tokens = [t.lower() for t in tokens if t not in punctuations]
        for token in clean_tokens:
            if token in scores:
                map_reduce.collect_scores(doc_id, scores[token])
            else:
                map_reduce.collect_scores(doc_id, 0)

    doc_id = doc_id + 1


def reducer(key, list_of_values):
    total_score = 0
    for value in list_of_values:
        total_score = total_score + value

    map_reduce.collect_final_scores((key, float(total_score)))


if __name__ == '__main__':
    NEG_PATH = sys.argv[1]
    POS_PATH = sys.argv[2]
    INPUT_DIR = sys.argv[3]

    lex_neg = open(NEG_PATH, encoding="cp1252").read().split("\n")
    lex_pos = open(POS_PATH, encoding="utf-8").read().split("\n")

    for neg_word in lex_neg:
        scores[neg_word] = -1
    for pos_word in lex_pos:
        scores[pos_word] = 1
    for negation_word in negations:
        scores[negation_word] = -1

    for i, docname in enumerate(sorted(os.listdir(INPUT_DIR)), 0):
        if not docname.startswith('.') and os.path.isfile(os.path.join(INPUT_DIR,
                                                                       docname)):
            # print(docname)
            with open(INPUT_DIR + docname, encoding="utf-8") as fin:
                review = fin.read()
                map_reduce.execute(review, mapper, reducer)
