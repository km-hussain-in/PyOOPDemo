#![macro_use]
#[allow(unused_macros)]
macro_rules! input {
    ($pr:expr, $type:ty) => {{
	use std::io::Write;
        print!($pr);
	std::io::stdout().flush().expect("io error");
        let mut line = String::new();
        std::io::stdin().read_line(&mut line).expect("No input");
        line.trim().parse::<$type>().expect("Bad input")
    }};
}


pub fn input<T>(prompt: &'static str) -> T 
where T: std::str::FromStr,
T::Err: std::fmt::Debug,
{
	use std::io::Write;
	print!("{}", prompt);
	std::io::stdout().flush().expect("io error");
	let mut line = String::new();
	std::io::stdin().read_line(&mut line).expect("No input");
	line.trim().parse::<T>().expect("Bad input")
}
