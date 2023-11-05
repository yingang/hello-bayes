from scipy.stats import norm
import numpy as np
import scipy.integrate as integrate

y, err = integrate.quad(lambda x: norm.pdf(x, 0, 1), -5, 5)
print(f"Exercise 12.1: {(1-y)/2:.3}")

data = [100.0, 99.8, 101.0, 100.5, 99.7]
avg, std = np.average(data), np.std(data)

y, err = integrate.quad(lambda x: norm.pdf(x, avg, std), 100.4, avg + 5 * std)
print(f"Exercise 12.2: {y:.2%}")

data = [2.5, 3, 3.5, 4, 2]
avg, std = np.average(data), np.std(data)
t_500 = np.sqrt(500 * 2 / 9.8)
print(f"Average: {avg:.3}, Std: {std:.2}, T_500M: {t_500:.4}")

y, err = integrate.quad(lambda x: norm.pdf(x, avg, std), t_500, 200)
print(f"Exercise 12.3: {y}")

y, err = integrate.quad(lambda x: norm.pdf(x, avg, std), 0, 200)
print(f"Exercise 12.4: {1-y}")