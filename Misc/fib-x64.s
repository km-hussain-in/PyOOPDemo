	.intel_syntax noprefix

	.global	Fib
	.type Fib, @function

	.text

Fib:
	mov		rax, rdi
	call	_Fib
	ret

_Fib:
	cmp		rax, 1
	jbe		1f

	push	rbx
	mov		rbx, rax
	sub		rbx, 2
	dec		rax
	call	_Fib

	xchg	rax, rbx
	call	_Fib

	add		rax, rbx
	pop		rbx

1:	ret


