use num_bigint::BigUint;
use std::collections::HashMap;
use std::time::{Duration, Instant};

fn problem() {
    println!("
Problem 435: Polynomials of Fibonacci numbers

The Fibonacci numbers {{f_n, n>=0}} are defined recursively as
f_n = f_{{n-1}} + f_{{n-2}} with base cases f_0 = 0 and f_1 = 1.

Define the polynomials {{F_n, n>=0}} as F_n(x) = Σ_{{i=0}}^n f_i * x**i.

For example, F_7(x) = x + x**2 + 2x**3 + 3x**4 + 5x**5 + 8x**6 + 13x**7,
and F_7(11) = 268357683.

Let n = 10**15. Find the sum Σ_{{x=0}}^100 F_n(x) and give your answer
modulus 1,307,674,368,000 (=15!).
"
    )
}

fn explanation() {
    println!("
Let φ = (1+5**.5)/2 and ψ = 1-φ. Since f_n = (φ**n - ψ**n)/5**.5, we
compute
   F_n(x) == Σ_{{k=0}}^n φ**k/5**.5 * x**k - ψ**k/5**.5 * x**k
          == ( x - f_n*x**(n+2) - f_{{n+1}}*x**(n+1) )/(1-x-x**2)

Let F_n(x) = A/B. Then, in order to compute F_n(x) % m and since B|A,
we use the formula F_n(x) % m == (A/B) % m == ( A % (B*m) ) / B and
the identities
            f_{{2*n-1}} == f_n**2 + f_{{n-1}}**2
              f_{{2*n}} == ( f_{{n-1}} + f_{{n+1}} ) * f_n
                      == ( 2*f_{{n-1}} + f_{{n}} ) * f_n
                      == ( 2*f_{{n+1}} - f_{{n}} ) * f_n
"
    )
}

fn solution(n: u64, max: u64) -> u64 {
    struct TrimmedFibonacci {
        cache: HashMap<BigUint, BigUint>,
        modulus: BigUint,
    }

    impl TrimmedFibonacci {
        fn new(modulus: &BigUint) -> Self {
           let mut fib = TrimmedFibonacci { cache: HashMap::new(), modulus: modulus.clone() };
           fib.cache.insert(BigUint::from(0u32), BigUint::from(0u32));
           fib.cache.insert(BigUint::from(1u32), BigUint::from(1u32));
           fib
        }

        fn get(&mut self, n: &BigUint) -> BigUint {
            if let Some(val) = self.cache.get(n) { val.clone() }
            else {
                let half = &(n/2u32);
                let fib = {
                    if (n % 2u32) == BigUint::from(1u32) {
                        ( self.get(half).pow(2) + self.get( &(half + 1u32) ).pow(2) ) % &self.modulus
                    } else {
                        let cur = self.get(half);
                        if let Some(prev) = self.cache.get( &(half - 1u32) ) {
                            ( ( prev * 2u32 + &cur ) * &cur ) % &self.modulus
                        }
                        else {
                            let next = self.get( &(half + 1u32) );
                            if &(&next * 2u32) > &cur {
                                ( ( &next * 2u32 - &cur ) * &cur ) % &self.modulus
                            } else {
                                ( ( &self.modulus + &next * 2u32 - &cur ) * &cur ) % &self.modulus
                            }
                        }
                    }
                };
                self.cache.insert(n.clone(), fib.clone());
                fib
            }
        }
    }

    let modulus = (1..=15).product::<u64>();
    let n = &BigUint::from(n);

    (
        (1..=max).map(|x: u64| {
            let denominator = x.pow(2) + x - 1;
            let top_modulus = &BigUint::from(modulus * denominator);

            let x = &BigUint::from(x);
            let xpow = &x.modpow(n, top_modulus);

            let mut fib = TrimmedFibonacci::new( top_modulus );

            (
                x * (
                    fib.get(n) * xpow * x
                + fib.get( &(n+&1u32) ) * xpow
                - &1u32
                ) / &denominator
            ) % &modulus
        }).sum::<BigUint>() % &modulus
    ).to_u64_digits()
     .first()
     .expect("the answer modulo 15! fits in a u64")
     .to_owned()
}

fn answer(ans: u64, time: Duration) {
    println!("\nTherefore Σ_{{x=0}}^100 F_n(x) = {}, when n = 10**15.", ans);
    println!("Computed in {}.{} seconds.", time.as_secs(), time.subsec_nanos());
    println!("");
}

fn main() {
    let start_time = Instant::now();
    problem();
    explanation();
    let ans = solution(10u64.pow(15), 100);
    answer(ans, start_time.elapsed());
}