use std::time::Instant;


fn compute_number_of_divisors_up_to(n: usize) -> Vec<u64> {
    let mut divisors = vec![0u64; n];

    for d in 1..=n.isqrt() {
        divisors[d*d-1] += 1;
        for k in d+1..=n/d {
            divisors[d*k-1] += 2;
        }
    }

    divisors
}

fn find_max(array: &[u64]) -> (u64, usize) {
    let mut max = array[0];
    let mut max_ndx = 0;

    for (j, &value) in array.iter().enumerate().skip(1) {
        if value > max {
            max = value;
            max_ndx = j;
        }
    }

    (max, max_ndx)
}

#[allow(non_snake_case)]
fn compute_S(u: usize, k: usize, num_of_divisors: &[u64]) -> u64 {
    let mut max;
    let mut max_ndx;
    (max, max_ndx) = find_max(&num_of_divisors[..k]);

    let mut sum = max;

    for n in 1..=u-k {
        let outgoing = n-1;
        let incoming = n+k-1;
        if max_ndx == outgoing {
            (max, max_ndx) = find_max(&num_of_divisors[n..n+k]);
            max_ndx += n; // find_max returns values between 0 and k-1
        } else if num_of_divisors[incoming] > max {
            max = num_of_divisors[incoming];
            max_ndx = incoming;
        }
        sum += max;
    }
    sum
}


fn main() {
    println!(
"Problem 485: Maximum Number of Divisors

Let d(n) be the number of divisors of n.
Let M(n,k) be the maximum value of d(j) for n <= j <= n+k-1.
Let S(u,k) be the sum of M(n,k) for 1 <= n <= u-k+1.

You are given that S(1000,10)=17176.
Find S(100,000,000, 100,000).\n"
);

    let start_time = Instant::now();

    let n: usize = 10usize.pow(8);
    let k: usize = 10usize.pow(5);

    println!("Precomputing the number of divisors function d(n) ... ");
    let num_of_divisors = compute_number_of_divisors_up_to(n);
    println!("Done in {:?} seconds", start_time.elapsed());

    println!("\nComputing S(10^3, 10)");
    println!("S(10^3, 10) = {}", compute_S(1000, 10, &num_of_divisors));

    println!("\nComputing S(10^8, 10^5)");
    println!("S(10^8, 10^5) = {}", compute_S(n, k, &num_of_divisors));

    println!("\nFinished in {:?} seconds", start_time.elapsed());
}

