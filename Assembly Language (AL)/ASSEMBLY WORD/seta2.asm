.model small
.stack 100h

.data
    msg1 db "Enter a String: $"
    strName db 32, 0, 30 dup('$')
    newline db 0dh, 0ah, "$"
    
.code
    mov ax, @data
    mov ds, ax
    
    mov ah, 09h
    lea dx, msg1
    int 21h
    
    mov ah, 0ah
    lea dx, strName
    int 21h

    mov ah, 06h
    mov al, 00h
    mov bh, 07h
    mov ch, 00 
    mov cl, 00
    mov dh, 24     
    mov dl, 79  
    int 10h
    
    mov ah, 02h
    mov bh, 00
    mov dh, 00
    mov dl, 00
    int 10h
    
    lea si, strName + 2
    mov cl, [strName + 1]
    
    mov bx, 0 
    
next_char:
    cmp cl, 0
    je exit
    
    mov dl, 31
    add dl, bl
    
    push cx
    mov cx, 0
    mov cl, dl
    
spacing:
    push cx
    mov dl, ' '
    mov ah, 02h
    int 21h
    pop cx
    loop spacing
    
    mov dl, [si]
    mov ah, 02h
    int 21h
    
    mov ah, 09h
    lea dx, newline
    int 21h
    
    pop cx
    inc si
    inc bx
    dec cl
    jmp next_char
    
exit:
    mov ah, 4ch
    int 21h
    
end
