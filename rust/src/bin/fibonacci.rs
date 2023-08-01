fn fibonacci(n:usize) -> Vec<u64> {
    let mut fib = vec![0, 1];
    for i in 2..n {
        fib.push(fib[i-1] + fib[i-2]);
    }

    fib
}

fn main() {
    println!("{:?}", fibonacci(6))
}