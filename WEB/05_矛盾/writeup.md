## Writeup
1. F12 and find the is_numeric() in php;
2. Process is: $num is **NOT** a number, and it should be taken as 1;
3. is_numeric() will take '1xxx' as none-numeric, and $num==1 will be true;
4. Create get value with url: ?num=1x;
5. Got it;