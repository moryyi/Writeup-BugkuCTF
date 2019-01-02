|Date|Version|
|:-:|:-:|
|2019/1/2|1.0|

## Writeup
1. Open the link and it is real nothing inside. So we could guess that something related to flag is inside of the package;
2. Open Burpsuite, grab the package and it will be simple to find the flag inside *Response* in Connection section:
```
Connection: close
flag{Bugku_k8_23s_istra}: 
Content-Length: 139
```

3. Or it could also be catched by wireshark. But it would spent sometime to check the related package;