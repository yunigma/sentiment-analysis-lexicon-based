#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
# von Iliyana Kamenova, Yeon Joo Oh, Iuliia Nigmatulina

# Big Data, FS19
# Ex04
# create MapReducer class


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

    def collect_final_scores(self, value):
        # append value to list of results
        self.results.append(value)

    def execute(self, data, mapper, reducer):
        # call Map function for each review document
        mapper(data)

        # call Reduce task for each key:valuelist in score dictionary
        for key in self.scores_collection:
            reducer(key, self.scores_collection[key])

        self.results.sort()
        # print results
        for item in self.results:
            print(item)
