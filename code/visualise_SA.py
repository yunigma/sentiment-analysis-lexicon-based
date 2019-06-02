#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
# von Iliyana Kamenova, Yeon Joo Oh, Iuliia Nigmatulina

# Big Data, FS19
# Ex04
# visualise the results of sentiment analysis


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# with open("../data/sentiment_table.csv", "r") as fin:
df = pd.read_csv("../data/sentiment_table.csv")
# df1 = df.groupby(['sent_score', 'label']).size().reset_index(name='counts')
df1 = df.sort_values('sent_score')
# print(df1)
# df2 = df[df['label'] == 'pos']
print(df1)

fig, ax = plt.subplots()
plt.plot(df1['sent_score'], df1['document'], 'bo')
plt.plot(df1['sent_score'][df['label'] == 'pos'],
         df1['document'][df['label'] == 'pos'], 'ro')
plt.plot(df1['sent_score'][df['label'] == 'neut'],
         df1['document'][df['label'] == 'neut'], 'mo')
labels = df1['sent_score'].tolist()
plt.axis([-6, 21, -1, 10])
ax.set_ylabel('Documents')
ax.set_title('Sentiment of restaurant reviews')
ax.legend(['pos', 'neg', 'neut'])
plt.show()
