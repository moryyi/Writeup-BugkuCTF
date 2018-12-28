|Date|Version|
|:-:|:-:|
|2018/12/28|1.0|

## Writeup
1. I have to say that right now I have no experience in analyzing web traffic. So what I have done was just open the .pcapng file with Wirechark and check the data inside one by one;
2. After searching for flag-like string, I found that in:
> 105	20.538401	192.168.228.135	192.168.228.1	HTTP	251	HTTP/1.1 200 OK  (text/html)

3. In this package, we could get the flag with *Line-based text data* section:
> X@Yflag{This_is_a_f10g}\n

## Others
1. Some package like:
> 90	18.852373	192.168.228.1	192.168.228.135	HTTP	841	POST /shell.php HTTP/1.1  (application/x-www-form-urlencoded)

Inside that package we will notice that there is a base64 string. If you decode that string, you will get php codes. Will actually I have no idea the usage of that. Maybe it will be executed on the server side.