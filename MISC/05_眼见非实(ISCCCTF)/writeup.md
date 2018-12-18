|Date|Version|
|:-:|:-:|
|2018/12/18|1.0|

## Writeup
1. Change the *zip* to *a.zip* and unpack the zip file;
2. Get the *眼见非实.docx*, check it and find out that it seems not a normal .docx file;
3. Change the *眼见非实.docx* to *b.zip* and unpack the new zip file;
4. Get the folder *眼见非实*;
5. Briefly check the content, we could find the *flag* in *word/document.xml*:
><w:r>
<w:t>Flag</w:t>
</w:r>
<w:r>
<w:t>**在这里呦！**</w:t>
</w:r>
</w:p>
<w:p w:rsidR="002B3D8D" w:rsidRPr="002B3D8D" w:rsidRDefault="002B3D8D">
<w:pPr>
<w:rPr>
<w:rFonts w:hint="eastAsia"/>
<w:vanish/>
</w:rPr>
</w:pPr>
<w:r w:rsidRPr="002B3D8D">
<w:rPr>
<w:vanish/>
</w:rPr>
<w:t>**flag{F1@g}**</w:t>
</w:r>
<w:bookmarkStart w:id="0" w:name="_GoBack"/>
<w:bookmarkEnd w:id="0"/>
</w:p>
