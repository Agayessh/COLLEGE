.model small
.stack 100h
.data
.code
    mov ax, @data
    mov ds, ax

    mov cx, 9              
    mov bh, 49h            
    mov bl, 61h            
    mov dh, 39h            

y:  
    push cx                

    mov ah, 02h
    mov dl, bh
    int 21h


    mov dl, bl
    int 21h

    mov ch, 00h
    mov cl, dh
    sub cl, 30h            

    mov ah, 02h
    mov dl, dh            

x:  int 21h               
    dec dl                 
    loop x                 

    mov dl, bl
    int 21h

    mov dl, bh
    int 21h


    mov dl, 0Ah
    int 21h
    mov dl, 0Dh
    int 21h

    dec bh                 
    inc bl                 
    dec dh                 

    pop cx                 
    loop y

    mov ah, 4Ch
    int 21h
end