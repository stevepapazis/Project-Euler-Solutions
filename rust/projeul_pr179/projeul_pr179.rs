use std::time::Instant;

const PROBLEM: &str = "Problem 179: Consecutive Positive Divisors

Find the number of integers 1 < n < 10^7, for which n and n + 1 have the
same number of positive divisors. For example, 14 has the positive divisors
1, 2, 7, 14 while 15 has 1, 3, 5, 15.";


const N: usize = 10usize.pow(7);

fn main() {
    println!("{PROBLEM}\n");

    let start = Instant::now();

    let mut divisor_number = vec![0u32; 1 + N];

    for d in 1 ..= N.isqrt() {
        divisor_number[d*d] += 1;
        for k in d+1..=N/d {
            divisor_number[d*k] += 2;
        }
    }

    let count = divisor_number.windows(2).filter(|w| w[0] == w[1]).count();
    print!("Answer: There are {count} such numbers.");

    let time = start.elapsed();
    println!(
        "\nComputed in {}.{} seconds.",
        time.as_secs(),
        time.subsec_nanos()
    );
}
