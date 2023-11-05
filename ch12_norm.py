from scipy.stats import norm
import numpy as np
import scipy.integrate as integrate

y, err = integrate.quad(lambda x: norm.pdf(x, 0, 1), -5, 5)
print(f"Exercise 12.1: {(1-y)/2:.3}")

data = [100.0, 99.8, 101.0, 100.5, 99.7]

avg, std = np.average(data), np.std(data)

y, err = integrate.quad(lambda x: norm.pdf(x, avg, std), 100.4, avg + 5 * std)
print(f"Exercise 12.2: {y:.2%}")
