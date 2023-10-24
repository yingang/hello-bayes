from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

a = 4
b = 6

x = np.arange(0.0, 1, 0.05)
plt.plot(x, beta.pdf(x, a, b), label="5.1")

y, err = integrate.quad(lambda x: beta.pdf(x, a, b), 0.6, 1)

print(f"Exercise 5.1: {y:.2%}")

a = 9
b = 11
plt.plot(x, beta.pdf(x, a, b), label="5.2")

y, err = integrate.quad(lambda x: beta.pdf(x, a, b), 0.45, 0.55)

print(f"Exercise 5.2: {y:.2%}")

a = 109
b = 111
plt.plot(x, beta.pdf(x, a, b), label="5.3")

y, err = integrate.quad(lambda x: beta.pdf(x, a, b), 0.45, 0.55)

print(f"Exercise 5.3: {y:.2%}")

plt.legend()
plt.show()
