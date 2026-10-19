use std::collections::HashMap;
use std::time::Instant;

const PROBLEM: &str = "Problem 50: Consecutive Prime Sum

The prime 41, can be written as the sum of six consecutive primes:
                  41 = 2 + 3 + 5 + 7 + 11 + 13.

This is the longest sum of consecutive primes that adds to a prime
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds
to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the
most consecutive primes?";

const EXPLANATION: &str = "Solution explanation:

Let S(m,n) := sum_{m<=k<n} p_k, where p_k is the k-th prime number.
Use the formula S(m,n) == S(m,n-1) + p_{n-1}, caching intermediate
results.";

struct PrimeSieve {
    top_limit: u64,
    primes: Vec<u64>,
}

impl PrimeSieve {
    fn new(up_to_n: u64) -> Self {
        let mut primes = vec![3, 5, 7];

        for m in (11..=up_to_n).step_by(2) {
            for &p in primes.iter() {
                if m % p == 0 {
                    break;
                }
                if p > m / p {
                    primes.push(m);
                    break;
                }
            }
        }

        Self {
            top_limit: up_to_n,
            primes,
        }
    }

    fn is_prime(&self, n: u64) -> bool {
        assert!(
            n <= self.top_limit * self.top_limit,
            "n={n} exceeds the sieve limit={}",
            self.top_limit * self.top_limit
        );

        if n == 1 {
            return false;
        }

        if n == 2 {
            return true;
        }

        if n % 2 == 0 {
            return false;
        }

        if n <= self.top_limit {
            return self.primes.binary_search(&n).is_ok();
        }

        for &p in self.primes.iter() {
            if p > n / p {
                break;
            }

            if n % p == 0 {
                return false;
            }
        }

        true
    }
}

struct PrimeSums<'a> {
    primes: &'a [u64],
    cache: HashMap<(usize, usize), u64>,
}

impl<'a> PrimeSums<'a> {
    fn new(primes: &'a [u64]) -> Self {
        Self {
            primes,
            cache: HashMap::new(),
        }
    }

    /// Computes the sum of primes `p_k` for `m <= k < n`
    fn compute(&mut self, m: usize, n: usize) -> u64 {
        if m >= n {
            return 0;
        }

        if let Some(&result) = self.cache.get(&(m, n)) {
            return result;
        }

        let result =
            if let Some(&prev_result) = self.cache.get(&(m, n - 1)) {
                prev_result + self.primes[n - 1]
            } else {
                self.primes[m..n].iter().sum()
            };

        self.cache.insert((m, n), result);
        result
    }
}

/// Finds the longest sum of consecutive primes that is a prime below the `limit`
fn find_longest_sum_prime(
    limit: u64,
    sieve: &PrimeSieve,
    prime_sums: &mut PrimeSums,
) -> (u64, usize) {
    let mut max_length_prime = 0;
    let mut max_length = 0;

    for m in 0..sieve.primes.len() {
        for length in (max_length + 1)..=(sieve.primes.len() - m) {
            let n = m + length;
            let p = prime_sums.compute(m, n);

            if p >= limit {
                break;
            }

            if sieve.is_prime(p) {
                max_length_prime = p;
                max_length = length;
                println!(
                    "New longest sum ({length} primes): {p} = p_{} + ... + p_{}",
                    m + 1,
                    n
                );
            }
        }
    }

    (max_length_prime, max_length)
}

fn solution(n: u64, sieve: &PrimeSieve, prime_sums: &mut PrimeSums) {
    println!(
        "
Searching for the longest sum of consecutive primes below {n}
that adds to a prime...
"
    );

    let (max_length_prime, max_length) = find_longest_sum_prime(n, sieve, prime_sums);

    println!(
        "
The longest sum of consecutive primes below {n} that adds to
a prime, contains {max_length} terms, and is equal to {max_length_prime}.
"
    );
}

const N: u64 = 10u64.pow(6);

fn main() {
    println!("{PROBLEM}\n\n");
    println!("{EXPLANATION}\n\n");

    let start = Instant::now();

    let sieve = PrimeSieve::new(N);
    let mut prime_sums = PrimeSums::new(&sieve.primes);

    println!("Results:");

    solution(1000, &sieve, &mut prime_sums);
    solution(N, &sieve, &mut prime_sums);

    println!("Computed in {:.3} seconds", start.elapsed().as_secs_f64());
}
