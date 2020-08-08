#[no_mangle]
pub extern fn Fib(n: u64) -> u64 {
	if n <= 1 {
		n
	}else{
		Fib(n - 1) + Fib(n - 2)
	}
}

//rustc --crate-type=cdylib fib.rs -o fib.so

