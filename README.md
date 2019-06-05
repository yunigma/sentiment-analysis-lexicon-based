# Sentiment Analysis lexicon based

1)
Annotation:    d1    d2    d3   d4   d5    d6   d7     d8   d9     d10
- Julia:      neg, neg, pos, neg, neg, pos, neut, neg, pos, neut
- Iliyana:    neg, neg, pos, neut, neg, pos, neut, neg, pos, neut
- Yeon Joo:   neg, neg, pos, neg, neg, pos, neut, neg, pos, neg

Inter-annotator agreement
Fleiss Kappa (k) statistics for nominal scales:

n = 3 annotators
k = 3 categories
10 data points (=documents)
N = 3 x 10 = 30
(sum(pj^2) = 8x9 + 2x4 + 1x2 = 72 + 8 + 2 = 82)
P = (sum(pj^2) — N) / (N * (n — 1)) = (82 — 30) / (30 * 2) = 52 / 60 = 0.8666
Pe = sum(pi^2) = 0.09 + 0.25 + 0.04 = 0.38
pi = sum(p_column_i) / N

kappa = (P — Pe) / (1 — Pe) =
= (0.8666 — 0.38) / (1 — 0.38) =
= 0.4866 / 0.62 =
= 0.7848
