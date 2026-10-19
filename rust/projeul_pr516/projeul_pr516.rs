use std::collections::HashMap;
use std::time::Instant;

const PROBLEM: &str = "Problem 516: 5-smooth Totients

5-smooth numbers are numbers whose largest prime factor doesn't
exceed 5. 5-smooth numbers are also called Hamming numbers.

Let S(L) be the sum of the numbers n not exceeding L such that
Euler's totient function φ(n) is a Hamming number. S(100)=3728.

Find S(10^12). Give your answer modulo 2^32.";

const EXPLANATION: &str = "Solution explanation:

Consider the prime factorization n = product(p_i^k_i). Then
Euler's totient function is
            φ(n) = product(p_i^(k_i-1) * (p_i-1)).

For φ(n) to be 5-smooth, every prime factor p_i > 5 of n must
have k_i = 1, and p_i - 1 must also be 5-smooth. Equivalently,
the prime factors greater than 5 take the form
               p_i = 1 + 2^a_i * 3^b_i * 5^c_i.

Let S(L,k) be the sum of products of distinct 5-smooth totient
primes chosen from the first k such primes, with each product
not exceeding L.

Partition the products in S(L,k) into those containing p_k and
those excluding it. Using the definitions of S(L,k-1) and
S(floor(L/p_k), we obtain
        S(L,k) = S(L,k-1) + p_k * S(floor(L/p_k),k-1).

Putting it all together, every valid integer n is written as
         n = 2^a * 3^b * 5^c * p_1 * p_2 * ... * p_k.

Thus, S(L) is given by
       S(L) = sum 2^a * 3^b * 5^c * S(L(a,b,c), k(a,b,c)),
where
           L(a,b,c) = floor(L / (2^a * 3^b * 5^c))
             k(a,b,c) = max{k : p_k <= L(a,b,c)}.

Precomputing the relevant primes and memoizing intermediate
results allows the answer to be computed efficiently.";

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

/// A collection of Hamming totient primes of the form
/// `1 + 2^a * 3^b * 5^c`, up to a given limit
struct HammingTotientPrimes {
    values: Vec<u64>,
}

impl HammingTotientPrimes {
    fn new(limit: u64) -> Self {
        let mut values = Vec::new();

        let sieve = PrimeSieve::new(1 + limit.isqrt());

        for a in 0..=limit.ilog(2) {
            let remainder_without_2s = limit / 2u64.pow(a);

            for b in 0..=remainder_without_2s.ilog(3) {
                let remainder_without_2_and_3s =
                    remainder_without_2s / 3u64.pow(b);

                for c in 0..=remainder_without_2_and_3s.ilog(5) {
                    let n = 1 + 2u64.pow(a)
                                   * 3u64.pow(b)
                                   * 5u64.pow(c);

                    if sieve.is_prime(n) {
                        values.push(n);
                    }
                }
            }
        }

        values.sort_unstable();

        Self { values }
    }

    fn index_of_greatest_leq(&self, n: u64) -> Option<usize> {
        self.values
            .partition_point(|&x| x <= n)
            .checked_sub(1)
    }
}

/// Computes cached sums of square-free products of the Hamming
/// totient primes 7, 11, 13, ...
struct SfHtpProductSums<'a> {
    ht_primes : &'a HammingTotientPrimes,
    cache: HashMap<(u64,usize), u64>,
}

impl<'a> SfHtpProductSums<'a> {
    fn new(hamming_totient_primes: &'a HammingTotientPrimes) -> Self {
        Self {
            ht_primes: hamming_totient_primes,
            cache: HashMap::new(),
        }
    }

    /// Computes the sum of square-free products of Hamming totient
    /// primes up to the prime at index `k`, each product not
    /// exceeding `n`.
    /// The primes are indexed as in `HammingTotientPrimes`, so 7 is
    /// index 3, 11 is index 4, etc.
    fn compute(&mut self, n: u64, k: usize) -> u64 {
        if k <= 2 || n < 7 {
            if n > 0 {
                return 1;
            } else {
                return 0;
            }
        }

        if let Some(&result)= self.cache.get(&(n,k)) {
            return result;
        }

        let pk = self.ht_primes.values[k];
        let s1 = self.compute(n, k - 1);
        let s2 = self.compute(n / pk, k - 1);
        let res = s1.wrapping_add(pk.wrapping_mul(s2));

        self.cache.insert((n,k), res);

        res
    }
}

fn solution(limit: u64, hamming_totient_primes: &HammingTotientPrimes) {
    let mut sqf_prod_sums = SfHtpProductSums::new(hamming_totient_primes);

    let mut sum = 0u32;

    for a in 0..=limit.ilog(2) {
        let remainder_without_2s = limit / 2u64.pow(a);

        for b in 0..=remainder_without_2s.ilog(3) {
            let remainder_without_2_and_3s =
                remainder_without_2s / 3u64.pow(b);

            for c in 0..=remainder_without_2_and_3s.ilog(5) {
                let m =
                    2u64.pow(a)
                        .wrapping_mul(3u64.pow(b)
                        .wrapping_mul(5u64.pow(c)
                    )) as u32;

                let remainder = remainder_without_2_and_3s / 5u64.pow(c);

                let s =
                    if let Some(k) = hamming_totient_primes.index_of_greatest_leq(remainder) {
                        sqf_prod_sums.compute(remainder, k) as u32
                    } else {
                        1
                    };

                sum = sum.wrapping_add(m.wrapping_mul(s));
            }
        }
    }

    println!("S({limit}) % 2^32 = {sum}");
}


const N: u64 = 10u64.pow(12);

fn main() {
    println!("{PROBLEM}\n\n");
    println!("{EXPLANATION}\n\n");

    let start = Instant::now();

    let hamming_totient_primes = HammingTotientPrimes::new(N);

    println!("Results:");
    solution(100, &hamming_totient_primes);
    solution(10u64.pow(12), &hamming_totient_primes);

    println!("\nComputed in {:.3} seconds", start.elapsed().as_secs_f64());
}