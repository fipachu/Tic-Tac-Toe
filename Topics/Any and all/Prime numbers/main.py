prime_numbers = []
for i in range(2, 1001):
    remainders = [i % divisor for divisor in range(2, int(i ** 0.5 + 1))]
    if all(remainders):
        prime_numbers.append(i)
