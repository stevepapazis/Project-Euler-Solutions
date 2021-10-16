use std::time::{Duration, Instant};
use std::collections::HashMap;

fn problem() {
    println!("
Problem 203: Squarefree Binomial Coefficients

The binomial coefficients C(n,k) can be arranged in triangular form,
Pascal's triangle, like this:
                                 1
                              1     1
                           1     2     1
                        1     3     3     1
                     1     4     6     4     1
                  1     5    10     10    5     1
               1     6    15    20     15    6     1
            1     7    21    35     35    21    7     1

It can be seen that the first eight rows of Pascal's triangle contain
twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime
divides n. Of the twelve distinct numbers in the first eight rows of
Pascal's triangle, all except 4 and 20 are squarefree. The sum of the
distinct squarefree numbers in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows
of Pascal's triangle.
"
    )
}

fn explanation() {
    println!("
The binomial coefficient C(n,k) = n!/(k!(n-k)!) is squarefree exactly
when there is no prime number p <= n**.5 such as C(n,k) % p**2 == 0.
"
    )
}

fn solution(rows: u64) -> u64 {
    struct Combinations {
        cache: HashMap<(u64,u64), u64>,
    }

    impl Combinations {
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
                    self.cache.insert( (n,k), a + b );
                    self.get(n, k)
                }
            }
        }
    }

    let mut combinations = Combinations { cache: HashMap::new() };

    let squares = [2, 3, 5, 7].iter().map(|&n: &u64| n.pow(2)).collect::<Vec<u64>>();

    let mut distinct_squarefree_combinations: HashMap<u64, u64> = HashMap::new();

    for n in 0..=rows {
        for k in 0..=n/2 {
            let c = combinations.get(n, k);
            distinct_squarefree_combinations.entry(c).or_insert(
                if let None = squares.iter().find( |&&sq| c % sq == 0 ) { c }
                else { 0 }
            );
        }
    }
    distinct_squarefree_combinations.values().sum()
}

fn answer(ans: u64, time: Duration) {
    println!(
"\nTherefore, there are {} distinct squarefree numbers in
the first 51 rows of the triangle.", ans);
    println!("Computed in {}.{} seconds.\n", time.as_secs(), time.subsec_nanos());
}

fn main() {
    let start_time = Instant::now();
    problem();
    explanation();
    let ans = solution(50);
    answer(ans, start_time.elapsed());
}