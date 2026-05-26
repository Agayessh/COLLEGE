; Write an AL program that will ask the user to input a single digit values as row and column and display the asterisk in sequence based on the input 

.model small
.stack 100h
.data
	msg1 db "Enter Row: $"
	msg2 db 0Ah,0Dh,"Enter Column: $"
	space db 0Ah, 0Dh, "$"
	row db 0
	col db 0

.code
	mov ax, @data
	mov ds, ax
	
	mov ah, 09h
	mov dx, offset msg1
	int 21h

	mov ah,01h	;read input of the user
	int 21h

	mov row, al	;save sa row
	
	mov ah,09h
	lea dx, msg2	; same sa offset
	int 21h
	
	mov ah, 01h
	int 21h

	mov col, al	;ASCII code ang naread read ng AL
	
	sub row, 30h
	sub col, 30h	; para makuha actual value kasi example 4 ang inenter ni user, so 34h ascii niya so minus 30h para 4 lang ang ma display
	
	mov ah, 09h
	lea dx, space
	int 21h
	
	mov ch, 00h	; para sure cx ay 00
	mov cl, row	; cx register

y:	push cx
	
	mov ch, 00h
	mov cl, col

	mov ah, 02h
	mov dl, '*' 
x:	int 21h

	loop x

	mov ah,09h
	lea dx, space
	int 21h

	pop cx
	loop y
	
	mov ah, 4ch
	int 21h
end