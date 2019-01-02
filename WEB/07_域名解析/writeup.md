## Writeup
1. (In win10) Modify the hosts file with a new line:
> 123.206.87.240 flag.baidu.com
2. Get in to *flag.baidu.com*, and take the flag;

## Something Else
1. Why hosts (Local DNS Resolution):
    - Help to create connection between *Hostnames* and *IP addresses*;
2. Why can't directly access IP address:
    - One of the possible reason is the *shared hosting*:
    > *One IP address* may host **many** web sites; The IP address alone is not enough information to tell the server which site is the one the user wants to visit;
    (Other information may be in the request generated);

    - Other reason may be the *reverse proxy* like Nginx:
    > a reverse proxy is a type of proxy server that retrieves resources on behalf of a client from one or more servers. These resources are then returned to the client, appearing as if they originated from the proxy server itself. ([From Wikipedia](https://en.wikipedia.org/wiki/Reverse_proxy))