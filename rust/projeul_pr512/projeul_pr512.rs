use std::time::Instant;

const PROBLEM: &str = "Problem 512: Sums of Totients of Powers

Let φ(n) be Euler's totient function.

Let f(n) = sum_{i=1}^n φ(n^i) mod (n+1).

Let g(n) = sum_{i=1}^n f(i).

g(100) = 2007.

Find g(5x10^8).";

const EXPLANATION: &str = "Solution explanation:

Since φ(n^i) = n^(i-1) * φ(n) and n = -1 (mod n+1), we have
    f(n) = φ(n) * (sum_{i=1}^{n} (-1)^(i-1)) mod (n+1).

The alternating sum is 0 when n is even and 1 when n is odd.
Hence,
                f(n) = 0      if n is even,
                f(n) = φ(n)   if n is odd,

and g(n) is the sum of φ(m) over all odd integers m <= n.";

const N: usize = 5*10usize.pow(8);

/// Sums Euler's totient function over the odd integers <= n
fn g(n: usize) -> u64 {
    let mut totient_cache: Vec<u32> =
        (0..n / 2).map(|i| (2 * i + 1) as u32).collect();

    for p in (3..=n).step_by(2) {
        let phi_p = &mut totient_cache[p / 2];

        if *phi_p == p as u32 { // no update => p is prime
            for m in (p..=n).step_by(2 * p) {
                let phi_m = &mut totient_cache[m / 2];
                *phi_m -= *phi_m / p as u32;
            }
        }
    }

    totient_cache
        .iter()
        .map(|&x| x as u64)
        .sum()
}

fn main() {
    println!("{PROBLEM}\n\n");
    println!("{EXPLANATION}\n\n");

    let start = Instant::now();

    println!("Results:");
    println!("g(100) = {}", g(100));
    println!("g({N}) = {}", g(N));

    println!("\nComputed in {:.3} seconds", start.elapsed().as_secs_f64());
}
