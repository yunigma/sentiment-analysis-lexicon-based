#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
# von Iliyana Kamenova, Yeon Joo Oh, Iuliia Nigmatulina

# Big Data, FS19
# Ex04

import os
import string
import re
import csv
from collections import Counter


INPUT_DIR = "../data/"
NEG_PATH = "../data/lexicon/negative-words.txt"
POS_PATH = "../data/lexicon/positive-words.txt"

punctuations = list(string.punctuation)
negations = ["no", "not"]
fout = open("../data/sentiment_table.csv", "w")
csv_writer = csv.writer(fout, delimiter=",")
csv_writer.writerow(("document", "sent_score", "label",
                     "neg words", "pos words"))

positive_words = Counter()
negative_words = Counter()


def get_score(document, option=1):
    ''' takes a raw document as an input;
        match words to negative and positive lexicons;
        2 options to calculate score: option1 is a default one;
        returns a sentiment score for the document
    '''
    pos_number = 0
    neg_number = 0
    # inluding negativity: the final score is composed of 3 scores (pos, neg and number of negations)
    negation_score = 0
    sent_score = 0
    neg_w = []
    pos_w = []

    document = document.strip()
    if len(document) > 0:
        # tokens = word_tokenize(line)
        document = re.sub(r"\.|!", " ", document)
        document = document.translate(str.maketrans('', '',
                                                    string.punctuation))
        tokens = document.split()
        # clean_tokens = [t for t in tokens if re.match(r'[^\W\d]*$', t)]
        clean_tokens = [t.lower() for t in tokens if t not in punctuations]

        if option == 1:
            for token in clean_tokens:
                if token in negations:
                    negation_score += 1
                if token in lex_pos:
                    pos_number += 1
                    positive_words[token] += 1
                    pos_w.append(token)
                if token in lex_neg:
                    neg_number += 1
                    negative_words[token] += 1
                    neg_w.append(token)

        elif option == 2:
            prev_negation = False
            for token in clean_tokens:
                if token in negations:
                    prev_negation = True
                    negation_score += 1
                elif token in lex_pos:
                    if prev_negation:
                        neg_number += 1
                        prev_negation = False
                        # print(token)
                    else:
                        pos_number += 1
                elif token in lex_neg:
                    if prev_negation:
                        pos_number += 1
                        prev_negation = False
                        # print(token)
                    else:
                        neg_number += 1
                else:
                    prev_negation = False

    if option == 1:
        sent_score = pos_number - (neg_number + negation_score)

    elif option == 2:
        sent_score = pos_number - neg_number

    print(
          # "POS: ", pos_number,
          # "\nNEG: ", neg_number,
          # "\nnegation score:", negation_score,
          # "SENTIMENT SCORE-3: ",
          sent_score,
          # "\n-------------------"
          )

    return sent_score, neg_w, pos_w


lex_neg = open(NEG_PATH, encoding="cp1252").read().split("\n")
lex_pos = open(POS_PATH, encoding="utf-8").read().split("\n")

for i, docname in enumerate(sorted(os.listdir(INPUT_DIR)), 0):
    if docname.startswith('d') and os.path.isfile(os.path.join(INPUT_DIR,
                                                               docname)):
        # print(docname)
        with open(INPUT_DIR + docname, encoding="utf-8") as fin:
            doc = fin.read()
            # option 1 or 2 should be chosen to define the way to calculate sentiment score
            score, neg_words, pos_words = get_score(doc, option=1)
            # if score >= 7:
            #     csv_writer.writerow((docname, score, "pos", neg_words, pos_words))
            # elif score <= 2:
            #     csv_writer.writerow((docname, score, "neg", neg_words, pos_words))
            # else:
            #     csv_writer.writerow((docname, score, "neut", neg_words, pos_words))
fout.close()

for pw in positive_words:
    print(pw, positive_words[pw])
