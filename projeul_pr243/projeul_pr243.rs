use std::time::Instant;

fn problem() {
    println!("
Problem 243: Resilience

A positive fraction whose numerator is less than its denominator is called a
proper fraction. For any denominator, d, there will be d−1 proper fractions;
for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12.

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the
ratio of its proper fractions that are resilient; for example, R(12) = 4/11.
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10.

Find the smallest denominator d, having a resilience R(d) < 15499/94744.
"
    )
}

fn explanation() {
    println!("
Notice that R(n) = φ(n)/(n-1) and R(2*3*5*7*11*13*17*19*23*29) < r;
where φ(n) is Euler's totient function and r := 15499/94744.

If q is a prime number and n = Π p_i**a_i such as q >= max p_i, we have
                        q**a * n > n
                            and
        R(q**a * n) = q**(a-1) * (q-1) * φ(n) / (q**a * n - 1)
                    = φ(n) / (n - q**(-a)) * (q-1) / q
                    < φ(n) / (n - 1) * (q-1) / q
                    < R(n)
Therefore the smallest denominator d has a prime factor decomposition that
is a subset of the set {{2, 3, 5, 7, 11, 13, 17, 19, 23, 29)}}.

          2*3*5*7*11*13*17*19*23*29 >= 2**5*3*5*7*11*13*17*19*23
                                    >= 2**4*3*5*7*11*13*17*19*23
                                    >= 2**3*3*5*7*11*13*17*19*23

    => R(2*3*5*7*11*13*17*19*23*29) <= R(2**5*3*5*7*11*13*17*19*23)
                                    <= R(2**4*3*5*7*11*13*17*19*23)
                                    <= R(2**3*3*5*7*11*13*17*19*23)
                                    <  r
                                    <= R(2**2*3*5*7*11*13*17*19*23)
    ")
}

fn solution() -> u64 {
    2u64.pow(3)*3*5*7*11*13*17*19*23
}

fn answer() {
    let start_time = Instant::now();
    println!("R({}) < 15499/94744 = {}", solution(), 15499.0/94744.0);
    let time = start_time.elapsed();
    println!("Computed in {}.{} seconds.\n", time.as_secs(), time.subsec_nanos());
}

fn main() {
    problem();
    explanation();
    answer();
}