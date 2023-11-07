from scipy.stats import beta, norm
import matplotlib.pyplot as plt
import numpy as np

# Exercise 13.1

plt.subplot(1, 3, 1)
x = np.arange(0.005, 0.01, 0.0001)
plt.plot(x, beta.pdf(x, 300, 39700))
plt.xlabel('Subscription Rate')
plt.ylabel('Density')
plt.title('PDF - Beta(300, 39700)')

plt.subplot(1, 3, 2)
x = np.arange(0.005, 0.01, 0.0001)
plt.plot(x, beta.cdf(x, 300, 39700))
plt.xlabel('Subscription Rate')
plt.ylabel('Cumulative Probability')
plt.title('CDF - Beta(300, 39700)')

plt.subplot(1, 3, 3)
x = np.arange(0.0, 1.0, 0.01)
plt.plot(x, beta.ppf(x, 300, 39700))
plt.xlabel('Cumulative Probability')
plt.ylabel('Subscription Rate')
plt.title('Quantile - Beta(300, 39700)')

plt.show()

# Exercise 13.2: 99.9% Confidence Interval

data = [7.8, 9.4, 10.0, 7.9, 9.4, 7.0, 7.0, 7.1, 8.9, 7.4]
avg, std = np.average(data), np.std(data)
print(f'Exercise 13.2: [{norm.ppf(0.0005, avg, std):.2f}, {norm.ppf(0.9995, avg, std):.2f}]')

# Exercise 13.3: 95% Confidence Interval

low, high = beta.ppf(0.025, 10, 20), beta.ppf(0.975, 10, 20)
print(f'Exercise 13.3: [{low * 40}, {high * 40}]')