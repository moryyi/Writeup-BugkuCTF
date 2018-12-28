|Date|Version|
|:-:|:-:|
|2018/12/21|1.0|

## Writeup
1. Cipher and numberlist[2, 1, 6, 5, 3, 4] are given; Notice that the length of cipher text is 24 and length of numberlist is 6; It is much like the order of each 6 letters;
2. For each 6 letters: re-order these letters with the given order; and do it for severial times;
3. The result for 10 times is given below:
>flga5{20844c537d49df}1@@
lf{5ga02c48435947dfd@@}1
flag{52048c453d794df1}@@
lf5{ag024c483549d7fd@@1}
flga5{20844c537d49df}1@@
lf{5ga02c48435947dfd@@}1
flag{52048c453d794df1}@@
lf5{ag024c483549d7fd@@1}
flga5{20844c537d49df}1@@
lf{5ga02c48435947dfd@@}1

Notice there is a clear pattern;
4. *flag{52048c453d794df1}@@* was very similar to usual flag string;
5. Get rid of the last 2 '@' and now we get the flag:
>flag{52048c453d794df1}