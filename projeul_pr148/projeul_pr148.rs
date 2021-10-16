use std::time::{Duration, Instant};
use std::collections::HashMap;

fn problem() {
    println!("
Problem 148: Exploring Pascal's triangle

We can easily verify that none of the entries in the first seven rows of
Pascal's triangle are divisible by 7:
                                    1
                                 1     1
                              1     2     1
                           1     3     3     1
                        1     4	    6	  4     1
                     1     5	10     10    5     1
                  1     6    15    20	  15    6     1

However, if we check the first one hundred rows, we will find that only
2361 of the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first
one billion (10**9) rows of Pascal's triangle.
"
    )
}

fn explanation() {
    struct CachedSequence {
        modulus: u64,
        cache: HashMap<(u64,u64), u64>,
    }

    impl CachedSequence {
        fn get(&mut self, n: u64, k: u64) -> u64 {
            if let Some(v) = self.cache.get( &(n,k) ) { *v }
            else {
                if k == 0 || n == k {
                    self.cache.insert( (n,k), 1 );
                    1
                }
                else {
                    let a = { self.get(n-1, k) };
                    let b = { self.get(n-1, k-1) };
                    let c = if let Some(v) = a.checked_add(b) { v }
                            else { a % self.modulus + b % self.modulus };
                    self.cache.insert( (n,k), c );
                    c
                }
            }
        }

        fn pretty_print_triangle(&mut self, size: u64) {
            let padding = size.to_string().len();
            for i in 0..size {
                print!("\n{:<width$}  ", i+1, width=padding);
                for j in 0..=i {
                    if self.get(i,j) % self.modulus == 0 { print!("x") }
                    else { print!(".") }
                }
            }
        }
    }

    let mut combinations = CachedSequence { cache: HashMap::new(), modulus: 3 };

    println!("
We modify Pascal's triangle, replacing entries which are not divisible
by {} with a dot ('.') and all the other entries with an 'x'.", combinations.modulus);

    combinations.pretty_print_triangle(130);

    println!("\n
The generated pattern is a fractal, similar to a Sierpiński triangle.
We get similar patterns if we replace {} with any other prime p. For
example, when p=7 we get:", combinations.modulus);

    let mut combinations = CachedSequence { cache: HashMap::new(), modulus: 7 };
    combinations.pretty_print_triangle(130);

    println!("\n
Let e(n) be the number of entries in the first n rows which are not
divisible by 7 and let T(n) be the nth triangular number. From the
above analysis, we can deduce the formula

              e(n) = T(a) * T(7)**k + (a+1) * e(n-a*7**k)

where k := floor( log_p(n) ) and a := n//(p**k).
    ");
}

fn solution(rows: u64, p: u64) -> u64 {
    let mut n = rows;
    let k = (n as f64).log(p as f64).floor() as u32;
    let mut p_pow_k = p.pow(k);
    let mut prod = 1u64;
    let triangular_p = p*(p+1)/2;
    let mut triangular_p_pow_k = triangular_p.pow(k);
    let mut sum = 0;

    #[allow(unused_comparisons)]
    while p_pow_k > 0 {
        let a = n/p_pow_k;
        n -= a*p_pow_k;
        sum += prod * a*(a+1)/2 * triangular_p_pow_k;
        prod *= a + 1;
        p_pow_k /= p;
        triangular_p_pow_k /= triangular_p;
    };
    sum
}

fn answer(ans: u64, time: Duration) {
    println!(
"\nTherefore, there are {} entries which are not divisible
by 7 in the first one billion rows of the triangle.", ans);
    println!("Computed in {}.{} seconds.\n", time.as_secs(), time.subsec_nanos());
}

fn main() {
    let start_time = Instant::now();
    problem();
    explanation();
    let ans = solution(10u64.pow(9), 7);
    answer(ans, start_time.elapsed());
}