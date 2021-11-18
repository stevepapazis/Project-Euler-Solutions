use itertools::Itertools;
use std::time::Instant;

fn problem() {
    println!("
Problem 622: Riffle Shuffles

A riffle shuffle is executed as follows: a deck of cards is split into
two equal halves, with the top half taken in the left hand and the bottom
half taken in the right hand. Next, the cards are interleaved exactly,
with the top card in the right half inserted just after the top card in
the left half, the 2nd card in the right half just after the 2nd card in
the left half, etc. (Note that this process preserves the location of the
top and bottom card of the deck)

Let s(n) be the minimum number of consecutive riffle shuffles needed to
restore a deck of size n to its original configuration, where n is a
positive even number.

Amazingly, a standard deck of 52 cards will first return to its original
configuration after only 8 perfect shuffles, so s(52) = 8. It can be
verified that a deck of 86 cards will also return to its original
configuration after exactly 8 shuffles, and the sum of all values of that
satisfy s(n) = 8 is 412.

Find the sum of all values of n that satisfy s(n) = 60.
"
    )
}

fn explanation() {
    println!(
"
Let 0,1,2,...,n be a deck of cards. After a riffle shuffle is executed,
the m card is placed in the (2*m) % (n-1) position. if the order of the
shuffle is k, we get 2**k % (n-1) == 1 <==> (2**k-1)//d + 1 == n, where
d is a divisor of 2**k-1.
"
    )
}

fn solution(m: u32) -> u64 {
    let twopow_min1 = 2u64.pow(m) - 1;
    let mut factors: Vec<u64> = Vec::new();
    let mut temp_twopow_min1 = twopow_min1;
    let mut p = 3;
    let mut lmt = (temp_twopow_min1 as f64).sqrt() as u64;

    while temp_twopow_min1 > lmt {
        while temp_twopow_min1 % p == 0 {
            temp_twopow_min1 /= p;
            factors.push(p)
        }
        p += 2;
        lmt = (temp_twopow_min1 as f64).sqrt() as u64;
    }

    if temp_twopow_min1 > 1 {
        factors.push(temp_twopow_min1)
    }

    let divisors = (2..m).filter_map(|n| if m % n == 0 { Some(n as u32) } else { None })
                         .collect::<Vec<_>>();

    factors.iter()
           .powerset()
           .unique()
           .filter_map(|vec| {
               let d = vec.into_iter().product::<u64>();
               if twopow_min1 % d != 0 { return None; }
               let n = twopow_min1 / d + 1;

               if n == 2 && m != 1 { return None; }

               for &div in &divisors {
                   if 2u64.pow(div) % (n-1) == 1 { return None; }
               }

               Some(n)
           })
           .sum()
}

fn answer(m: u32) {
    let start_time = Instant::now();
    println!("The sum of all values of n that satisfy s(n) = {} is {}.", m, solution(m));
    let time = start_time.elapsed();
    println!("Computed in {}.{} seconds.", time.as_secs(), time.subsec_nanos());
}

fn main() {
    problem();
    explanation();
    answer(8);
    answer(60);
}