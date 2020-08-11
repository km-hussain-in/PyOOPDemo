extern "C" {
	fn Fib(n: u64) -> u64;
}

fn main() {
	let args: Vec<String> = std::env::args().collect();
	let mut n: u64 = 10;
	if args.len() > 1 {
		n = args[1].parse().unwrap();
	}
	unsafe {
		println!("Result = {}", Fib(n));
	}
}

//ar rcs libfib.a fib.o 
//rustc callfib.rs -L -lfib

