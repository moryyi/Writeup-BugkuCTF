|Date|Version|
|:-:|:-:|
|2018/12/21|1.0|

## Writeup
1. Execute *admin.exe* and find out that this is not an executable file;
2. Open with IDA and view it in hex, and notice the content:
>data:image/png;base64,iVBO...

3. Save the rest base64-encoded content into a new file *admin_en.exe* and decode that file into new file *admin_de.exe*;
4. Execute the *admin_de.exe* and find out it is still not executable;
5. Open with IDA and notice it was a **.png** file;
6. Change the extension with *admin_de.png* and get a QR code;
7. Scan it and get the flag: 
>bugku{inde_9882ihsd8-0}

## Tips
1. In windows, use **certutil** to decode base64:
> certutil -decode <ENCODED-FILE> <DECODED-FILE>

2. In linux, use base64 --decode (not try yet, but I believe stackoverflow :))

3. Or we could write a python script to read in file, decode, and write in new file;