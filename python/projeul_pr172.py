problem = """Problem 172: Few Repeated Digits

How many 18-digit numbers n (without leading zeros) are there such that
no digit occurs more than three times in n?
"""


explanation = """
Solution explanation:

A recursive algorithm that generates all valid numbers can be adapted
to count them directly. This also simplifies the algorithm by replacing
the generation of individual numbers with combinatorial counting.

The resulting recurrence relation is:

 W(n, m, d) = 1_{n <= m} + W(n, m, d-1)
              + sum(C(n, k) * W(n-k, m, d-1)) for k = 1, ..., min(n, m)

where W(n, m, d) counts valid n-digit numbers using digits 0 through d,
with each digit appearing at most m times, and C(n, k) is the binomial
coefficient.

Finally, since 1/10 of the numbers start with a zero, the number of
valid n-digit numbers without leading zeros is 9/10 * W(n,m,9).
"""


def combinations(n: int, k: int) -> int:
    """Return the number of ways to choose k items from n items"""
    if k < 0 or n < k:
        return 0

    k = min(k, n - k)

    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i

    return result

def interleave_digit_copies(digit: str, prefix: str, remaining: str, n_copies: int) -> list[str]:
    """Generate numbers by interleaving `remaining` with `n_copies` copies of `digit`, prefixed by `prefix`"""

    if n_copies == 0:
        return [prefix + remaining]

    if not remaining:
        return [prefix + digit*n_copies]

    return (
        interleave_digit_copies(digit, prefix + digit, remaining, n_copies-1) +
        interleave_digit_copies(digit, prefix + remaining[0], remaining[1:], n_copies)
    )

def generate_few_repeated_digit_numbers(n_digits: int, n_copies: int, digit: int) -> list[str]:
    """Generate all n-digit numbers using digits <= digit, with each digit appearing at most n_copies times"""

    if n_digits <= 0 or n_copies <= 0:
        return []

    # numbers containing only the given digit
    numbers = [str(digit) * n_digits] if n_digits <= n_copies else []

    if digit == 0:
        return numbers

    # numbers with no copies of the digit
    numbers.extend(generate_few_repeated_digit_numbers(n_digits, n_copies, digit-1))

    # numbers containing k copies of the digit
    for k in range(1, min(n_copies, n_digits) + 1):
        for remaining in generate_few_repeated_digit_numbers(n_digits-k, n_copies, digit-1):
            numbers.extend(interleave_digit_copies(str(digit), "", remaining, k))

    return sorted(numbers)

cache: dict[tuple[int, int, int], int] = dict()

def _count_few_repeated_digit_numbers(n_digits: int, n_copies: int, digit: int) -> int:
    """Count n-digit numbers using digits <= digit, with each digit appearing at most n_copies times"""

    if n_digits <= 0 or n_copies <= 0:
        return 0

    # numbers containing only the given digit
    total = int(n_digits <= n_copies)

    if digit == 0:
        return total

    if (n_digits, n_copies, digit) in cache:
        return cache[(n_digits, n_copies, digit)]

    # numbers with no copies of the digit
    total += _count_few_repeated_digit_numbers(n_digits, n_copies, digit - 1)

    # numbers containing k copies of the digit
    for k in range(1, min(n_digits, n_copies) + 1):
        total += combinations(n_digits, k) * _count_few_repeated_digit_numbers(n_digits - k, n_copies, digit - 1)

    cache[(n_digits, n_copies, digit)] = total
    return total


def count_few_repeated_digit_numbers(n_digits: int, n_copies: int) -> int:
    """Count n-digit numbers, with each digit appearing at most n_copies times"""
    return 9*_count_few_repeated_digit_numbers(n_digits, n_copies, 9)//10

print(problem)
print(explanation)
print("Answer: 0.9 * W(18, 3, 9) =", count_few_repeated_digit_numbers(18,3))
