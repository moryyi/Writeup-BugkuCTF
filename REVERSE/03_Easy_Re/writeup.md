|Date|Version|
|:-:|:-:|
|2018/12/17|1.0|

## Writeup
1. Open with IDA;
2. F5 and get the pseudocode of _main();
3. Notice the process:
    1. Read input string into v9 and compare it with v5;
    2. v5 was setup with:
    > _mm_storeu_si128((__m128i *)&v5, _mm_loadu_si128((const __m128i *)&xmmword_413E34));
    3. The variable *xmmword_413E34* was:
    > .rdata:00413E34 xmmword_413E34  xmmword 3074656D30633165577B465443545544h
    > .rdata:00413E34                                         ; DATA XREF: _main+10↑r
    > .rdata:00413E44 qword_413E44    dq 7D465443545544h      ; DATA XREF: _main+27↑r
    4. Notice the last severial letters in *xmmword_413E34* were:
    > 46 54 43 54 55 44: F T C T U D
    
    And it was clear that flag was given in LSB;
    At the same time, remember that '}' was 0x7d, so variable *qword_413E44* was also required;
    5. Now flag could be created with re-ordering hex string like: \x44\x55\x54\x43\x54\x46\x7b\x57\x65\x31\x63\x30\x6d\x65\x74\x30\x44\x55\x54\x43\x54\x46\x7d;