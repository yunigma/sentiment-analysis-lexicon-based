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

INPUT_DIR = "../data/"
NEG_PATH = "../data/lexicon/negative-words.txt"
POS_PATH = "../data/lexicon/positive-words.txt"

punctuations = list(string.punctuation)
negations = ["no", "not"]

map_reduce = MapReducer.MapReducer()
neg_scores = {}
scores = {}
doc_id = 1


def mapper(path):
    ''' takes path to the direction where all review files are. Open files
        one by one and calculate the sentiment score according to the number
        of negative, positive and negation words, maps (tags) each document
        to a list of polarity values.
        Keep all the intermediate results in MapReducer scores_collection.
    '''
    global doc_id

    for i, docname in enumerate(sorted(os.listdir(path)), 0):
        if not docname.startswith('.') and os.path.isfile(os.path.join(path,
                                                                       docname)):
            with open(path + docname, encoding="utf-8") as fin:
                document = fin.read()
                document = document.strip()
                if len(document) > 0:
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
    ''' iterates through the dictionary score_collection and aggregates scores.
    '''
    total_score = 0
    for value in list_of_values:
        total_score = total_score + value

    map_reduce.collect_final_scores((key, float(total_score)))


if __name__ == '__main__':
    # NEG_PATH = sys.argv[1]
    # POS_PATH = sys.argv[2]
    # INPUT_DIR = sys.argv[3]

    fin_neg = open(NEG_PATH, encoding="cp1252")
    fin_pos = open(POS_PATH, encoding="utf-8")
    lex_neg = fin_neg.read().split("\n")
    lex_pos = fin_pos.read().split("\n")

    for neg_word in lex_neg:
        scores[neg_word] = -1
    for pos_word in lex_pos:
        scores[pos_word] = 1
    for negation_word in negations:
        scores[negation_word] = -1

    map_reduce.execute(INPUT_DIR, mapper, reducer)

    fin_neg.close()
    fin_pos.close()
