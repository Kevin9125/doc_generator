struct Rational {
    num: i64,
    den: i64,
}

impl Rational {
    fn new(num: i64, den: i64) -> Self {
        if den == 0 {
            panic!("Zero denominator");
        }
        let g = gcd(num.abs(), den.abs());
        let n = if g == 0 { num } else { num / g };
        let d = if g == 0 { den } else { den / g };
        Rational { num: n, den: d }
    }

    fn add(self, other: Rational) -> Rational {
        let num = self.num * other.den + other.num * self.den;
        let den = self.den * other.den;
        Rational::new(num, den)
    }

    fn mul(self, other: Rational) -> Rational {
        let num = self.num * other.num;
        let den = self.den * other.den;
        Rational::new(num, den)
    }
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}