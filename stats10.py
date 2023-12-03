# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import statistics as st
import matplotlib.pyplot as plt

x = "14 23 10 21 7 80 32 30 92 14 26 21 38 20 35 21".split()
x = [int(i) for i in x]
print(x)
x = sorted(x)
print(x)

print(len(x))
print(x[:8])
print(x[8:])

q1 = st.median(x[:8])
q3 = st.median(x[8:])
print('Five-number summary:', [x[0], q1, st.median(x), q3, x[-1]])

plt.boxplot(x, vert=False)
plt.show()

iqr = q3 - q1
iqr

print('Range:', x[-1] - x[0])

print('Outliers:', [i for i in x if i < (q1 - 1.5*iqr) or i > (q3 + 1.5*iqr)])

st.mean(x), st.median(x)
