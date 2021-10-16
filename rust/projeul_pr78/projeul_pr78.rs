use std::collections::HashMap;
use std::time::{Duration, Instant};

fn problem() {
    println!("
Problem 78: Coin partitions

Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can separated into piles in
exactly seven different ways, so p(5)=7.

      1.  OOOOO
      2.  OOOO  O
      3.  OOO  OO
      4.  OOO  O  O
      5.  OO  OO  O
      6.  OO  O  O  O
      7.  O  O  O  O  O

Find the least value of n for which p(n) is divisible by one million.
"
    )
}

fn explanation() {
    println!("
A recursive formula for calculating p(n) is given by the pentagonal
number theorem:
      p(n) = sum_{{k=1}}^{{+∞}} (-1)**(k-1) * p(n - g_k)
where g_k is the k-th generalized pentagonal number; that is
      g_{{2k-1}} = p_{{-k}} and g_{{2k}} = p_k,
when k = 1,2,3,... and p_n = (3n**2-n)/2.
"
    )
}

fn solution(digit_limit: u32) -> usize {
    let size = 10isize.pow(digit_limit);

    fn cutoff(n: isize, size: isize) -> isize { n.rem_euclid(size) }

    let mut pentagonals: Vec<isize> = Vec::with_capacity(size as usize);
    pentagonals.push(0);
    pentagonals.push(1);
    pentagonals.push(2);

    fn compute_pentagonal(n: isize, size: isize) -> isize {  ( (3*n-1)*n/2 ) % size  }

    fn get_pentagonal(n: isize, pentagonals: &mut Vec<isize>, size: isize) -> isize {
        if let Some(value) = pentagonals.get(n as usize) { *value }
        else {
            let last_index = pentagonals.len()/2;
            for i in ((last_index+1) as isize)..=n {
                pentagonals.push( compute_pentagonal(i, size) );
                pentagonals.push( compute_pentagonal(-i, size) );
            }
            pentagonals[n as usize]
        }
    }

    let mut partitions: HashMap<isize, isize> = HashMap::with_capacity(size as usize);
    partitions.insert(0,1);
    partitions.insert(1,1);

    fn compute_partition(
        n: isize,
        mut pentagonals: &mut Vec<isize>,
        mut partitions: &mut HashMap<isize, isize>,
        size: isize,
    ) -> isize {
        if let Some(value) = partitions.get(&n) { *value }
        else {
            let start = {
                let minus = ( ( 1.0 - f32::sqrt(24.0*n as f32 + 1.0) )/6.0 ).trunc() as isize;
                let plus = ( ( 1.0 + f32::sqrt(24.0*n as f32 + 1.0) )/6.0 ).trunc() as isize;
                if -minus == plus { 2*plus+1 } else { 2*plus }
            };
            if pentagonals.last().unwrap() < &n { get_pentagonal(n, &mut pentagonals, size); };
            let partition = (1isize..start).rev().scan(
                (0isize, &mut pentagonals, &mut partitions), |(sum, pentas, parts), i| {
                    let pentagonal = get_pentagonal(i, *pentas, size);
                    let partition = compute_partition(n - pentagonal, *pentas, *parts, size);
                    *sum = cutoff(
                        if i % 4 == 1 || i % 4 == 2  { *sum + partition }
                        else { *sum - partition },
                        size
                    );
                    Some(*sum)
                }
            ).last().expect("return partition");
            partitions.insert(n, partition);
            partition
        }
    }

    let mut zeroes = 10;
    (1isize..).skip_while( |&n| {
        let p_n = compute_partition(n, &mut pentagonals, &mut partitions, size);
        if p_n % zeroes == 0 {
            println!("n:={},   p_n % {} = {} % {} = 0", n, zeroes, p_n, zeroes);
            zeroes *= 10
        }
        p_n != 0
    }).next().expect("return solution") as usize
}

fn answer(ans: usize, time: Duration) {
    println!("\n{} is the least value of n such as p(n) is divisible by one million.", ans);
    println!("Computed in {}.{} seconds.", time.as_secs(), time.subsec_nanos());
    println!("");
}

fn main() {
    let start_time = Instant::now();
    problem();
    explanation();
    let ans = solution(6);
    answer(ans, start_time.elapsed());
}