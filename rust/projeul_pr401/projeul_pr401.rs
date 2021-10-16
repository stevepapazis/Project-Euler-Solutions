use std::fmt;
use std::ops::{Add, Mul, Sub};
use std::time::Instant;

fn problem() {
    println!("
Problem 401: Sum of squares of divisors

The divisors of 6 are 1, 2, 3 and 6. The sum of the squares of these
numbers is 1 + 4 + 9 + 36 = 50.

Let sigma2(n) represent the sum of the squares of the divisors of n.
Thus sigma2(6) = 50.

Let SIGMA2 represent the summatory function of sigma2, that is
              SIGMA2(n) = ∑ sigma2(i) for i = 1,...,n.

The first 6 values of SIGMA2 are: 1, 6, 16, 37, 63 and 113.
Find SIGMA2(10**15) % 10**9.
"
    )
}

fn explanation() {
    println!("
Note that SIGMA2(N) = ∑_{{i=1}}^N  i * ( S(N//i) - S(N//(i+1)) )
where S(n) = ∑_{{i=1}}^n i**2 = n**3/3 + n**2/2 + n/6.
"
    )
}


#[derive(Clone, Copy, Debug)]
struct ModularNum {
    num: u64,
    modulus: u64,
}

impl ModularNum {
    #![allow(dead_code)]

    fn new(n: u64, m: u64) -> Self {
        Self { num: n % m, modulus: m, }
    }

    fn to_u64(&self) -> u64 { self.num }

    fn pow(self, exp: u64) -> Self {
        if exp == 0 { return Self::new(1, self.modulus); }
        let mut base = self;
        let mut exp = exp;
        let mut result = base;
        while exp > 1 {
            if exp % 2 == 1 {
                result = result * base;
            }
            result = result * base;
            exp >>= 1;
            base = base * base;
        }
        result
    }
}

impl fmt::Display for ModularNum {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
       write!(f, "{} (mod {})", self.num, self.modulus)
    }
}

impl Add for ModularNum {
    type Output = Self;

    fn add(self, rhs: Self) -> Self {
        debug_assert!(
            self.modulus == rhs.modulus,
            "Different moduli in the addition of {} and {}", self, rhs
        );
        Self::new(
            self.num + rhs.num,
            self.modulus
        )
    }
}

impl Sub for ModularNum {
    type Output = Self;

    fn sub(self, rhs: Self) -> Self {
        debug_assert!(
            self.modulus == rhs.modulus,
            "Different moduli in the subtraction of {} and {}", self, rhs
        );
        Self::new(
            self.modulus + self.num - rhs.num,
            self.modulus
        )
    }
}


impl Mul for ModularNum {
    type Output = Self;

    fn mul(self, rhs: Self) -> Self {
        debug_assert!(
            self.modulus == rhs.modulus,
            "Different moduli in the multiplication of {} and {}", self, rhs
        );
        Self::new(
            if let Some(value) = self.num.checked_mul(rhs.num) { value }
            else {
                (  (self.num as u128) * (rhs.num as u128) % (self.modulus as u128)  ) as u64
            },
            self.modulus
        )
    }
}

#[allow(non_snake_case)]
fn solution(n: u64, modulus: u64) -> u64 {
    let partial_sum_of_squares = |x: u64| -> ModularNum {
        let sum_of_squares = |x: u64| {
            let m = (6 * modulus) as u128;
            let x = x as u128;
            let sq = x * x % m;
            let cb = sq * x % m;
            ModularNum::new(  ( (2 * cb + 3 * sq + x) % m / 6 ) as u64, modulus  )
        };
        sum_of_squares( n/x ) - sum_of_squares( n/(x+1) )
    };

    let mut k = 1;
    let mut SIGMA2 = ModularNum::new(0, modulus);

    while k < n/k {
        let kmod = ModularNum::new(k, modulus);
        let ndivk = ModularNum::new(n/k, modulus);

        SIGMA2 = SIGMA2
               + kmod * partial_sum_of_squares(k)
               + ndivk * partial_sum_of_squares(n/k);
        k += 1;
    }

    if k == n/k {
        let kmod = ModularNum::new(k, modulus);
        SIGMA2 = SIGMA2 + kmod * partial_sum_of_squares(k);
    }

    SIGMA2.to_u64()
}

fn answer(top_index: u64, modulus: u64) {
    let start_time = Instant::now();
    println!(
        "Then SIGMA2({}) % {} = {}.",
        top_index,
        modulus ,
        solution(top_index, modulus)
    );
    let time = start_time.elapsed();
    println!("Computed in {}.{} seconds.\n", time.as_secs(), time.subsec_nanos());
}

fn main() {
    problem();
    explanation();
    answer(10u64.pow(15), 10u64.pow(9));
}