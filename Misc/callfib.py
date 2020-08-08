import sys
import time
import ctypes

def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2)

count = int(sys.argv[1])

print("Using pure Python code")
t = time.time()
result = fib(count)
t = time.time() - t
print(f'Result = {result} computed in {t} seconds')

print("Using Native and Python code")
lib = ctypes.CDLL("./fib.so")
t = time.time()
result = lib.Fib(count)
t = time.time() - t
print(f'Result = {result} computed in {t} seconds')

