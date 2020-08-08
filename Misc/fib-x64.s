	.intel_syntax noprefix

	.global	Fib
	.type Fib, @function

	.text

#thunk for position independent code
Fib:
	mov		rax, rdi
	jmp		_Fib

_Fib:
	cmp		rax, 1
	jbe		1f

	push		rbx
	mov		rbx, rax
	sub		rbx, 2
	dec		rax
	call		_Fib        #_Fib(n-1)

	xchg		rax, rbx
	call		_Fib        #_Fib(n-2)

	add		rax, rbx    #_Fib(n-1)+_Fib(n-2)
	pop		rbx

1:	ret

	.end

# as -o fib.o fib-x64.s
# ld -shared -o fib.so fib.o
