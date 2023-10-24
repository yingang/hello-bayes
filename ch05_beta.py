from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as intergrate

a = 4
b = 6

x = np.arange(0.0, 1, 0.05)
plt.plot(x, beta.pdf(x, a, b))
plt.show()

print(intergrate.quad(lambda x: beta.pdf(x, a, b), 0.6, 1))