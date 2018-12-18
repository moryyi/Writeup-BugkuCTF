|Date|Version|
|:-:|:-:|
|2018/12/18|1.0|

## Writeup
1. Open with IDA and get into the *_main()* and *_main_0()*;
2. In *_main_0()*, notice the last several sentences:
>if ( byte_532E28[0] == 1
&& byte_532E28[1] == 1
&& byte_532E28[2] == 1
&& byte_532E28[3] == 1
&& byte_532E28[4] == 1
&& byte_532E28[5] == 1
&& byte_532E28[6] == 1
&& byte_532E28[7] == 1 )
{
sub_457AB4();
}

3. Get into *sub_457AB4()* and *sub_45E940()* inside;
4. The *sub_45E940()* is listed below; Transform it into solve.py and get the flag;
>int sub_45E940()
{
  char v1; // [esp+0h] [ebp-164h]
  signed int i; // [esp+D0h] [ebp-94h]
  char v3; // [esp+DCh] [ebp-88h]
  ... (Intialization from v3 to v116)
  char v116; // [esp+158h] [ebp-Ch]
  sub_45A7BE((int)"done!!! the flag is ", v1);
  v60 = 18;
  v61 = 64;
  v62 = 98;
  v63 = 5;
  v64 = 2;
  v65 = 4;
  v66 = 6;
  v67 = 3;
  v68 = 6;
  v69 = 48;
  v70 = 49;
  v71 = 65;
  v72 = 32;
  v73 = 12;
  v74 = 48;
  v75 = 65;
  v76 = 31;
  v77 = 78;
  v78 = 62;
  v79 = 32;
  v80 = 49;
  v81 = 32;
  v82 = 1;
  v83 = 57;
  v84 = 96;
  v85 = 3;
  v86 = 21;
  v87 = 9;
  v88 = 4;
  v89 = 62;
  v90 = 3;
  v91 = 5;
  v92 = 4;
  v93 = 1;
  v94 = 2;
  v95 = 3;
  v96 = 44;
  v97 = 65;
  v98 = 78;
  v99 = 32;
  v100 = 16;
  v101 = 97;
  v102 = 54;
  v103 = 16;
  v104 = 44;
  v105 = 52;
  v106 = 32;
  v107 = 64;
  v108 = 89;
  v109 = 45;
  v110 = 32;
  v111 = 65;
  v112 = 15;
  v113 = 34;
  v114 = 18;
  v115 = 16;
  v116 = 0;
  v3 = 123;
  v4 = 32;
  v5 = 18;
  v6 = 98;
  v7 = 119;
  v8 = 108;
  v9 = 65;
  v10 = 41;
  v11 = 124;
  v12 = 80;
  v13 = 125;
  v14 = 38;
  v15 = 124;
  v16 = 111;
  v17 = 74;
  v18 = 49;
  v19 = 83;
  v20 = 108;
  v21 = 94;
  v22 = 108;
  v23 = 84;
  v24 = 6;
  v25 = 96;
  v26 = 83;
  v27 = 44;
  v28 = 121;
  v29 = 104;
  v30 = 110;
  v31 = 32;
  v32 = 95;
  v33 = 117;
  v34 = 101;
  v35 = 99;
  v36 = 123;
  v37 = 127;
  v38 = 119;
  v39 = 96;
  v40 = 48;
  v41 = 107;
  v42 = 71;
  v43 = 92;
  v44 = 29;
  v45 = 81;
  v46 = 107;
  v47 = 90;
  v48 = 85;
  v49 = 64;
  v50 = 12;
  v51 = 43;
  v52 = 76;
  v53 = 86;
  v54 = 13;
  v55 = 114;
  v56 = 1;
  v57 = 117;
  v58 = 126;
  v59 = 0;
  for ( i = 0; i < 56; ++i )
  {
    *(&v3 + i) ^= *(&v60 + i);
    *(&v3 + i) ^= 0x13u;
  }
  return sub_45A7BE((int)"%s\n", (unsigned int)&v3);
}