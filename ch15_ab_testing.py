from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# Chapter 15.2

alpha = 3
beta = 7
times = 100000

samples_a = np.random.beta(36 + alpha, 114 + beta, times)
samples_b = np.random.beta(50 + alpha, 100 + beta, times)

print(f"{np.sum(samples_a < samples_b) / times:.2%}")

plt.subplot(1, 2, 1)
plt.hist(samples_b / samples_a)
plt.xlabel('samples_b / samples_a')
plt.ylabel('frequency')

ax = plt.subplot(1, 2, 2)
stats.ecdf(samples_b / samples_a).cdf.plot(ax)
plt.xlabel('samples_b / samples_a')
plt.ylabel('accumulated probability')

plt.show()
