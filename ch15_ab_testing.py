from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# Chapter 15.2

prio_alpha = 3
prio_beta = 7
trials = 100000

a_samples = np.random.beta(36 + prio_alpha, 114 + prio_beta, trials)
b_samples = np.random.beta(50 + prio_alpha, 100 + prio_beta, trials)

print(f"{np.sum(a_samples < b_samples) / trials:.2%}")

plt.subplot(1, 2, 1)
plt.hist(b_samples / a_samples)
plt.xlabel('samples_b / samples_a')
plt.ylabel('frequency')

ax = plt.subplot(1, 2, 2)
stats.ecdf(b_samples / a_samples).cdf.plot(ax)
plt.xlabel('samples_b / samples_a')
plt.ylabel('accumulated probability')

plt.show()

# Exercise 15.1

prio_alpha = 300
prio_beta = 700

a_samples = np.random.beta(36 + prio_alpha, 114 + prio_beta, trials)
b_samples = np.random.beta(50 + prio_alpha, 100 + prio_beta, trials)

print(f"Exercise 15.1: {np.sum(a_samples < b_samples) / trials:.2%}")

# Exercise 15.2

a_alpha, a_beta = 30, 70
b_alpha, b_beta = 20, 80

a_samples = np.random.beta(36 + a_alpha, 114 + a_beta, trials)
b_samples = np.random.beta(50 + b_alpha, 100 + b_beta, trials)

print(f"Exercise 15.2: {np.sum(a_samples < b_samples) / trials:.2%}")

# Exercise 15.3

prio_alpha = 300    # director
prio_beta = 700     # director

a_rate = 0.25
b_rate = 0.3

b_win = 0
emails = 0
while b_win < 0.95:
    emails += 100
    a_positive = np.sum(np.random.uniform(size = emails//2) <= a_rate)  # A/B组对半分
    a_negative = emails//2 - a_positive
    b_positive = np.sum(np.random.uniform(size = emails//2) <= b_rate)
    b_negative = emails//2 - b_positive

    a_samples = np.random.beta(a_positive + prio_alpha, a_negative + prio_beta, trials)
    b_samples = np.random.beta(b_positive + prio_alpha, b_negative + prio_beta, trials)
    b_win = np.sum(a_samples < b_samples) / trials

print(f"{emails} more emails to convince the director => {b_win:.2%}")
