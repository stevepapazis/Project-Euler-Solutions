use std::time::Instant;

fn problem() {
    println!("
Problem 190: Maximising a weighted product

Let Sm = (x1, x2, ... , xm) be the m-tuple of positive real numbers with
x1 + x2 + ... + xm = m for which P_m = x1 * x2**2 * ... * xm**m is maximised.

For example, it can be verified that [P_10] = 4112 ([ ] is the integer part
function).

Find Σ[P_m] for 2 ≤ m ≤ 15.
"
    )
}

fn explanation() {
    println!("
Let P_m(x) = Π xi**i and g(x) = x1 + x2 + ... + xm - m. Use the method of
Lagrange multipliers to maximise P_m subject to the condition g = 0. We find
the unique critical point x = (2/(m+1), 2*2/(m+1), ..., 2*m/(m+1)) where P_m
is maximised.
"
    )
}

fn solution(max: u64) -> u64 {
    (2..=max).map(|m| {
                (1..=m).map( |n| {
                            let xn = 2.0*(n as f64)/(m as f64 + 1.0);
                            xn.powi(n as i32)
                     }).product::<f64>() as u64
           }).sum()
}

fn answer(max_ndx: u64) {
    let start_time = Instant::now();
    let int_sum_p_m = solution(max_ndx);
    let time = start_time.elapsed();
    print!("\nΣ[P_m] = {} when 2 ≤ m ≤ {}. ", int_sum_p_m, max_ndx);
    println!("Computed in {}.{} seconds.\n", time.as_secs(), time.subsec_nanos());
}

fn main() {
    problem();
    explanation();
    answer(15);
}