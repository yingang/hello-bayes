from scipy.stats import binom

print(f"Exercise 4.2: {binom.pmf(1, 5, p = 1/13) :.2%}")

print(f"Exercise 4.2: {5 * ((1/13)**1) * ((12/13)**4) :.2%}") # same with last one

print(f"Exercise 4.3: {binom.pmf(5, 10, p = 1/13) :.2%}")

print(f"Exercise 4.4: {binom.pmf(2, 7, p = 1/5) :.2%}")

print(f"Exercise 4.5: {binom.pmf(2, 25, p = 1/10) :.2%}")