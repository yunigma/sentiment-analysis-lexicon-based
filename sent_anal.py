#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
# von Iuliia Nigmatulina

# Big Data, FS19
# Ex04

import os
import string
import re

# neg, neg, pos, neg, neg, pos, neut, neg, pos, neut

INPUT_DIR = "data/"
NEG_PATH = "data/lexicon/negative-words.txt"
POS_PATH = "data/lexicon/positive-words.txt"

punctuations = list(string.punctuation)
negations = ["no", "not"]


def find_lexicon(document, option):
    ''' takes a raw document as an input;
        returns a sentiment label for the document
    '''
    pos_number = 0
    neg_number = 0
    # inluding negativity: the final score is composed of 3 scores (pos, neg and number of negations)
    negation_score = 0
    sent_score = 0

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
                if token in fin_pos:
                    pos_number += 1
                if token in fin_neg:
                    neg_number += 1

        elif option == 2:
            prev_negation = False
            for token in clean_tokens:
                if token in negations:
                    prev_negation = True
                    negation_score += 1
                elif token in fin_pos:
                    if prev_negation:
                        neg_number += 1
                        prev_negation = False
                        # print(token)
                    else:
                        pos_number += 1
                elif token in fin_neg:
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

    # return sent_score


fin_neg = open(NEG_PATH, encoding="cp1252").read().split("\n")
fin_pos = open(POS_PATH, encoding="utf-8").read().split("\n")

for i, docname in enumerate(sorted(os.listdir(INPUT_DIR)), 0):
    if not docname.startswith('.') and os.path.isfile(os.path.join(INPUT_DIR,
                                                                   docname)):
        # print(docname)
        with open(INPUT_DIR + docname, encoding="utf-8") as fin:
            doc = fin.read()
            # option 1 or 2 should be chosen to define the way to calculate sentiment score
            find_lexicon(doc, option=1)
