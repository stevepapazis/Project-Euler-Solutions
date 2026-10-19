use std::time::Instant;

const PROBLEM: &str = "Problem 7: 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 100001st prime number?
";

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


fn main() {
    println!("{PROBLEM}");

    let start = Instant::now();

    let mut sieve = PrimeSieve::new(1000);

    let mut next_odd = *sieve.primes.last().expect("should exist");

    while sieve.primes.len() < 10000 {
        next_odd += 2;

        if sieve.is_prime(next_odd) {
            sieve.primes.push(next_odd);
        }
    }

    println!("Answer: {next_odd}");

    println!("\nComputed in {:.3} seconds", start.elapsed().as_secs_f64());
}
