import sys
import time
import ctypes

def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2)

count = int(sys.argv[1])

print("Using pure Python")
t = time.time()
result = fib(count)
t = time.time() - t
print(f'Result = {result} computed in {t} seconds')

print("Using Assembly and Python")
lib = ctypes.CDLL("./fib.so")
t = time.time()
result = lib.Fib(count)
t = time.time() - t
print(f'Result = {result} computed in {t} seconds')

