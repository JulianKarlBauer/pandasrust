fn main() {
    println!("{}", count_5s(505));
}

fn count_5s(number: i64) -> usize {
    number.to_string().matches('5').count()
}