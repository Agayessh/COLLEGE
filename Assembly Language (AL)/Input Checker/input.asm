.model small
.stack 100h
.data

  msg1 db "Press any key: $" 
  msg2 db 0Ah, 00h, "You pressed: $"
  inp db 0

.code
  mov ax, @data
  mov ds, ax

  mov ah, 09h
  mov dx, offset msg1
  int 21h

  mov ah, 01h
  int 21h

  mov inp, al

  mov ah, 09h
  mov dx, offset msg2
  int 21h

  mov ah, 02h     
  mov dl, inp      
  int 21h        

  mov ah, 4Ch
  int 21h
end