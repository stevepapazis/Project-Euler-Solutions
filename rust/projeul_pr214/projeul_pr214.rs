use std::time::Instant;

const PROBLEM: &str = "Problem 214: Totient Chains

Let φ be Euler's totient function, i.e. for a natural number n,
φ is the number of k, 1 <= k <= n, for which gcd(k, n) = 1.

By iterating φ, each positive integer generates a decreasing
chain of numbers ending in 1. E.g. if we start with 5 the
sequence 5,4,2,1 is generated. Here is a listing of all chains
with length 4:
                         5,4,2,1
                         7,6,2,1
                         8,4,2,1
                         9,6,2,1
                        10,4,2,1
                        12,4,2,1
                        14,6,2,1
                        18,6,2,1
Only two of these chains start with a prime, their sum is 12.

What is the sum of all primes less than 40000000 which generate
a chain of length 25?";

struct CacheableTotient {
    cache: Vec<u32>
}

impl CacheableTotient {
    fn new(top_value: usize) -> Self {
        let mut cache = vec![1u32; top_value/2];

        for p in (3..=top_value).step_by(2) {
            if cache[p/2] != 1 {
                continue;
            }

            cache[p/2] *= (p - 1) as u32;

            for n in (3*p..=top_value).step_by(2*p) {
                if cache[n/2] == 1 {
                    cache[n/2] = n as u32;
                }
                cache[n/2] -= cache[n/2]/p as u32;
            }
        }

        Self { cache }
    }

    fn compute(&self, n: u32) -> u32 {
        if n == 1 {
            return 1;
        }

        let a = n.trailing_zeros();
        if a > 0 {
            let t = self.compute(n>>a);
            return  t * (1<<(a-1));
        }

        self.cache[n as usize / 2]
    }
}

fn solution(limit: usize, length: usize, totient: &CacheableTotient) {
    let mut sum = 0u64;

    for i in 0..limit/2 {
        let p = (2 * i + 1) as u32;

        if totient.compute(p) != p - 1 { // p is not prime
            continue
        }

        let mut phi_p = p;
        for i in 2..=length {
            phi_p = totient.compute(phi_p);
            if phi_p == 1 {
                if i == length {
                    sum += p as u64;
                } else {
                    break
                }
            }
        }
    }

    println!(
"The sum of all primes less than {limit} that generate a chain
of length {length} is {sum}\n"
    );
}

const N: usize = 4*10usize.pow(7);

fn main() {
    println!("{PROBLEM}\n\n");

    let start = Instant::now();

    let totient = CacheableTotient::new(N);

    println!("Results:");
    solution(100, 4, &totient);
    solution(N, 25, &totient);

    println!("Computed in {:.3} seconds", start.elapsed().as_secs_f64());
}
