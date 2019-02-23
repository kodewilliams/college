# domath.S
# Kode Williams 
# Deeshai Escoffery
# Gedare Bloom
#

# Variables in the .data section.
.data

# string var named prompt
prompt: .asciiz "Please enter an integer: "
operator_prompt: .asciiz "Please enter an operator (+, -, *, /): "
error: .asciiz "Error: invalid arithmetic operation '"
period: .asciiz "'."
remainder: .asciiz "remainder"
newline: .asciiz "\n"



# Instructions in the .text section.
.text

# main() is the program entry point. It is responsible for
# reading two integers and an operator, and passing the read
# values to do_math

main:
	# maintain a proper call stack
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	
	# print the prompt message 
	la $a0, prompt
	li $v0, 4
	syscall

	# read an integer from user
	li $v0, 5
	syscall

	# put input integer into argument register
	or $a1, $v0, $zero
	or $s1, $a1, $zero

	# TODO: print the operator prompt, and read the operator
	# print the operator prompt
	la $a0, operator_prompt
	li $v0, 4
	syscall

	# read the operator from user
	li $v0, 12
	syscall

	# put operator character into argument register
	or $a2, $v0, $zero
	or $s2, $a2, $zero

	la $a0, newline
	li $v0, 4
	syscall
	
	# TODO: print prompt message and read another integer
	# print the prompt message again
	la $a0, prompt
	li $v0, 4
	syscall

	# read an integer from user
	li $v0, 5
	syscall

	# put input integer into argument register
	or $a3, $v0, $zero
	or $s3, $a3, $zero
	
	# reset return value register
	
	# TODO: call do_math(integer, operator, integer)
	jal do_math
	
	#output newline
	la $a0, newline
	li $v0, 4
	syscall
	
	#output newline
	la $a0, newline
	li $v0, 4
	syscall
	
	# Restore return address and unwind the stack
	lw $ra, 0($sp)
	addi $sp, $sp, 4

	# TODO: return 0
	li $v0, 10
	syscall
	

# do_math takes three register arguments containing two integers (X, Y)
# and a character indicating an arithmetic operator (OP),
# invokes a subroutine to calculate X OP Y, and
# prints the result or an error message.
do_math:

    # maintain a proper call stack
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	
	# copy operation into temporary register
	or $t5, $a2, $zero

	# determine operation using character
	# for addition
	beq $t5, 43, lets_add
	# for subtraction
	beq $t5, 45, lets_subtract
	# for multiplication
	beq $t5, 42, lets_multiply
	# for division
	beq $t5, 47, lets_divide
	
	# account for error in operator
	la $a0, error
	li $v0, 4
	syscall

	# print operator
	add $a0, $t5, $zero
	li $v0, 11
	syscall

	la $a0, period
	li $v0, 4
	syscall
	
lets_add:

	jal do_add
	b print
	
lets_subtract:

	jal do_subtract
	b print
	
lets_multiply:

	jal do_multiply
	b print
	
lets_divide:

	jal do_divide
	b print
	

	
	
print:

	or $s4, $v0, $zero
	or $s5, $v1, $zero

	li $v0, 1
	or $a0, $s1, $zero
	syscall
	
	li $v0, 11
	or $a0, $s2, $zero
	syscall
	
	
	li $v0, 1
	or $a0, $s3, $zero
	syscall
	
	li $v0, 11
	or $a0, $zero, 61
	syscall
	
	beq $s2,47, print_divide
	
	li $v0, 1
	or $a0, $s4, $zero
	syscall
	
	lw $ra, 0($sp)
	addi $sp, $sp, 4
	jr $ra
	
	print_divide:
	
	li $v0, 1
	or $a0, $s4, $zero
	syscall
	
	li $v0, 4
	la $a0, remainder
	syscall
	
	li $v0, 1
	or $a0, $s5, $zero
	syscall
	
	
    
    # Restore return address and unwind the stack
	lw $ra, 0($sp)
	addi $sp, $sp, 4
	jr $ra

do_add:
	# TODO: implement do_add
	or $t1, $a1, $zero
	or $t2, $a3, $zero

	add_loop:
		# if the second integer is zero, end the add
		beqz $t2, end_add_loop

		# else
		# find the carry
		and $t3, $t1, $t2
		
		# find a = xor(a,b)
		xor $t1, $t1, $t2

		# find b = carry << 1
		sll $t2, $t3, 1

		# jump back to the start of the loop
		j add_loop

	end_add_loop:
		or $v0, $t1, $zero
		or $s4, $v0, $zero
		jr $ra

do_subtract:
	# TODO: implement do_subtract

	# copy arguments into temporary registers
	or $t4, $a1, $zero
	or $t2, $a3, $zero
	# if the second integer is zero, end the add
	beqz $t2, end_subtract

	# else
	# invert the second integer's bits
	nor $t2, $t2, $0
	# copy value 1 into register to do one's complement addition
	ori $a1, $0, 1
	# make second argument register one's complement of second integer
	or $a3, $t2, $zero
	# copy return address
	or $t6, $ra, $zero
	# Get two's complement of second integer
	jal do_add
	# retrieve return address
	or $ra, $t6, $zero
	# Set arguments to first integer and two's complement of second integer
	or $a1, $t4, $zero
	or $a3, $v0, $zero
	# copy return address
	or $t6, $ra, $zero
	# do the addition (really subtraction)
	jal do_add
	# retrieve return address
	or $ra, $t6, $zero
	
	end_subtract:
	or $v0, $t1, $zero
	or $s4, $v0, $zero
	jr $ra
		

do_multiply:

	# maintain a proper call stack
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	
	# TODO: implement do_multiply
	or $t1, $a1, $zero
	or $t5, $a3, $zero
	or $t6, $t6, $zero

	bgt $t5, 0, multiply_loop

multiply_loop:

	beqz $t5, end_multiply

	or $a3, $t6, $zero

	jal do_add

	or $t6, $v0, $zero

	addi $t5, $t5, -1

	j multiply_loop

	end_multiply:
	or $v0, $t6, $zero
	or $s4, $v0, $zero
	
	
	  # Restore return address and unwind the stack
	lw $ra, 0($sp)
	addi $sp, $sp, 4
	jr $ra


do_divide:

        # maintain a proper call stack
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	
	# TODO: implement do_divide
	ori $t1, $a1, 0					# initializes registers $t1, $t2 with argument values (integers)
	ori $t9, $a3, 0
	or $t7, $0, $0
	
divi:
	jal do_subtract
	
	or $a1, $v0, $0
	or $a3, $t9, $0
	addi $t7, $t7, 1
        
        
	bgt $a1, $a3, divi
	beq $a1, $a3, divi
        
	
	or $v0, $t7, $0
	or $v1, $a1, $0
	
	or $s4, $t7, $0
	or $s5, $a1, $0
	
	
	# Restore return address and unwind the stack
	lw $ra, 0($sp)
	addi $sp, $sp, 4 
	
	jr $ra





