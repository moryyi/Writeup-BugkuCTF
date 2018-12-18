|Date|Version|
|:-:|:-:|
|2018/12/18|1.0|

## Writeup
1. Notice this is a kind of cryptography?encoding? using Ook! language (a language similar to brainfuck, details see *Refers*)
2. Using online encode/decode tools and get the original text, then we get the flag:
>flag{ok-ctf-1234-admin}

## About Ook!
The basic rule for Ook! language was:
>***Ook. Ook?***
Move the Memory Pointer to the next array cell.
***Ook? Ook.***
Move the Memory Pointer to the previous array cell.
***Ook. Ook.***
Increment the array cell pointed at by the Memory Pointer.
***Ook! Ook!***
Decrement the array cell pointed at by the Memory Pointer.
***Ook. Ook!***
Read a character from STDIN and put its ASCII value into the cell pointed at by the Memory Pointer.
***Ook! Ook.***
Print the character with ASCII value equal to the value in the cell pointed at by the Memory Pointer.
***Ook! Ook?***
Move to the command following the matching Ook? Ook! if the value in the cell pointed at by the Memory Pointer is zero. Note that Ook! Ook? and Ook? Ook! commands nest like pairs of parentheses, and matching pairs are defined in the same way as for parentheses.
***Ook? Ook!***
Move to the command following the matching Ook! Ook? if the value in the cell pointed at by the Memory Pointer is non-zero.

## TODO
1. (Finished: 2018/12/18) Try to *understand* this fucking language and write a script(see solve.py) for implementation;

## References
1. [Wikipedia: brainfuck](https://en.wikipedia.org/wiki/Brainfuck)
2. [CSDN: Brainfuck and Ook!](https://www.cnblogs.com/WangAoBo/p/6373318.html)