	.text

	.global	Fib
	.type	Fib, %function

Fib:	
	cmp	x0, 1
	ble	1f

	stp	x29, x30, [sp, -16]!
	sub	x29, x0, 2
	sub	x0, x0, 1
	bl	Fib

	mov	x1, x29
	mov	x29, x0
	mov	x0, x1
	bl	Fib

	add	x0, x0, x29
	ldp	x29, x30, [sp], 16

1:	ret

	.end

# as -o fib.o fib-a64.s
# ld -shared -o fib.so fib.o

