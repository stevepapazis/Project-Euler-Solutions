use std::time::{Duration, Instant};

fn problem() {
    println!("
Problem 64: Odd period square roots

All square roots are periodic when written as continued fractions
and can be written in the form:
          N**.5 = a0 + 1/(a1 + 1/(a2 + 1/(a3 + ... )))

For example, let us consider 23**.5:
         23**.5 = 4 + 23**.5 - 4 = 4 + 1/(1 + 23**.5/7)

If we continue we would get the following expansion:
        23**.5 = 4 + 1/(1 + 1/(3 + 1/(1 + 1/(8 + ... ))))

It can be seen that the sequence 1,3,1,8,... is repeating. For
conciseness, we use the notation 23**.5 = [4;(1,3,1,8)], to
indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational)
square roots are:
                2**.5=[1;(2)], period=1
                3**.5=[1;(1,2)], period=2
                5**.5=[2;(4)], period=1
                6**.5=[2;(2,4)], period=2
                7**.5=[2;(1,1,1,4)], period=4
                8**.5=[2;(1,4)], period=2
                10**.5=[3;(6)], period=1
                11**.5=[3;(3,6)], period=2
                12**.5=[3;(2,6)], period=2
                13**.5=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N<=13, have an odd period.

How many continued fractions for N<=10000 have an odd period?
"
    )
}

fn explanation() {
    println!("
Let N**.5=[a0; a1,a2,a3,...]. It can be proven that the pattern
repeats when a_k == 2*a_0 and the period is k.
"
    )
}

fn solution(max: u64) -> u64 {
    fn is_not_square(n: u64) -> bool { (n as f64).sqrt().floor().powi(2) as u64 != n }

    fn  compute_period(n: u64) -> u64 {
        let (mut m, mut d, mut a, mut len) = (0, 1, (n as f64).sqrt().floor() as u64, 0);
        let a0 = a;

        while a!=2*a0 {
            m = d*a - m;
            d = (n - m*m)/d;
            a = (a0 + m)/d;
            len += 1;
        }

        len
    }

    (1u64..=max).filter( |&n| { is_not_square(n) })
                .map( |n| { compute_period(n) })
                .filter( |&p| { p % 2 == 1 } )
                .map( |_| { 1 } )
                .sum()
}

fn answer(ans: u64, time: Duration) {
    println!("\nFor N<=10000, there are {} continued fractions with an odd period.", ans);
    println!("Computed in {}.{} seconds.", time.as_secs(), time.subsec_nanos());
    println!("");
}

fn main() {
    let start_time = Instant::now();
    problem();
    explanation();
    let ans = solution( 10000 );
    answer(ans, start_time.elapsed());
}