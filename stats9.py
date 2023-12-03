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

x = """
40 60 73 77 51 68
68 35 68 53 64 75
76 69 59 55 38 57
68 84 75 62 73 75
85 77"""
x = [int(i) for i in x.split()]
print(x)
x = sorted(x)
print(x)

print(len(x))
print(x[:13])
print(x[13:])

q1 = st.median(x[:13])
q3 = st.median(x[13:])
print('Five-number summary:', [x[0], q1, st.median(x), q3, sx[-1]])
iqr = q3 - q1
print('IQR:', iqr)
outliers = [i for i in x if i < (q1 - 1.5*iqr) or i > (q3 + 1.5*iqr)]
print('Outliers:', outliers)

plt.boxplot(x, vert=False)
plt.show()

y = """
19 18 20 29 39 43
71 56 44 44 18 19
19 18 18 20 25 29
25 22 31 24 24 23
19 19 18 28 20 31"""
y = [int(i) for i in y.split()]
print(y)
y = sorted(y)
print(y)

print(len(y))
print(y[:15])
print(y[15:])

q1 = st.median(y[:15])
q3 = st.median(y[15:])
print('Five-number summary:', [y[0], q1, st.median(y), q3, y[-1]])
iqr = q3 - q1
print('IQR:', iqr)
outliers = [i for i in y if i < (q1 - 1.5*iqr) or i > (q3 + 1.5*iqr)]
print('Outliers:', outliers)

# note that the outliers are drawn as well
plt.boxplot(y, vert=False)
plt.show()
