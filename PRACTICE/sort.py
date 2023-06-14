import big_o
def selection(x):
    for i in range(len(x)):
        min_idx = i
        for j in range(i + 1, len(x)):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]
    return x

# z=[5,9,7,6,4]

# print(selection(z))
#####################################
"""Complexity Cheak"""

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(selection, positive_int_generator, n_repeats=10)
print(best)