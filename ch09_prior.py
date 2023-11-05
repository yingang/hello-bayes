from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

a = 6
b = 1

y, err = integrate.quad(lambda x: beta.pdf(x, a, b), 0.4, 0.6)
print(f"Exercise 9.1: {y:.2%}")

times = 1
data = []
while True:
    y, err = integrate.quad(lambda x: beta.pdf(x, 6 + times, 1 + times), 0.4, 0.6)
    data.append((times, y))
    if y >= 0.95:
        break
    times += 1

print(f"Exercise 9.2: {times} times")

plt.plot(*zip(*data))
plt.show()

more_times = 1
while True:
    y, err = integrate.quad(lambda x: beta.pdf(x, 6 + times + more_times, 1 + times), 0.4, 0.6)
    if y < 0.5:
        break
    more_times += 1

print(f"Exercise 9.3: {more_times} times more")
