#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
# von Iliyana Kamenova, Yeon Joo Oh, Iuliia Nigmatulina

# Big Data, FS19
# Ex04
# create MapReducer class

NEG = 2
POS = 7


class MapReducer:
    def __init__(self):
        # dictionary with scores for each review from Map step
        self.scores_collection = {}
        # list with results from Reduce step
        self.results = []

    def collect_scores(self, key, value):
        # if key not in dictionary, set value to empty list
        self.scores_collection.setdefault(key, [])
        # add value to list associated with key
        self.scores_collection[key].append(value)

    def collect_final_scores(self, key, value):
        # append value to list of results
        if value >= POS:
            self.results.append((key, value, "positive"))
        elif value <= NEG:
            self.results.append((key, value, "negative"))
        else:
            self.results.append((key, value, "neutral"))

    def execute(self, data, mapper, reducer):
        # call Map function for each review document
        mapper(data)

        # call Reduce task for each key:valuelist in score dictionary
        for key in self.scores_collection:
            reducer(key, self.scores_collection[key])

        # sort by sentiment class
        self.results.sort(key=lambda x: x[2])
        # sort by doc id
        # self.results.sort()
        # print results
        for item in self.results:
            print(item)
