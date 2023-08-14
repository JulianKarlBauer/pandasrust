fn count_5s(number: i64) -> usize {
    number.to_string().matches('5').count()
}

fn count_5s_vec(values: Vec<i64>) -> Vec<usize> {
    values.into_iter()
        .map(count_5s)
        .collect()
}

fn main() {
    println!("{}", count_5s(505));
    let data = vec![1, 2, 5, 505];
    println!("{:?}", count_5s_vec(data));
}
