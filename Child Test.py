import codecs
import pandas as pd
import xlsxwriter
import numpy as np

def create_html_file(filename):
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(f'''<!DOCTYPE html>
                <html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
  <meta name="description" content="Family Tree Site of Nickolas Holland">
  <meta name="keywords" content="Family Tree">
  <meta name="author" content="Nickolas Holland">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="default.css" media="screen">
  <title>TEST</title>
</head>

<body>

<div class="container">

<div class="header">

<div class="title">
<h1>Family Tree</h1>
</div>

<div class="navigation">
<a href="index.html">Home</a>
<a href="Family Names.html">Family Names</a> 
<a href="DNE.html">People</a>
<a href="Overview.html">Overview</a>

<div class="clearer">
<span></span></div>
</div>
</div>

<div class="main">

<div class="content">

<h1>

</h1>

<h3>
Sex: 
</h3>
<p>

</p>

<h3>
Date of Birth: 
</h3>
<p>

</p>
<h3>
Date of Death: 
</h3>
<p>

</p>

<h3>
Mother: 
</h3>
<p>

</p>

<h3>
Father: 
</h3>
<p>

</p>

<h3>
Partner(s): 
</h3>
<p>
N/A
</p>

<h3>
Child(ren): 
</h3>
<p>
N/A
</p>

<h3>
<a href="DNE.html">View Tree</a>
</h3>

</div>

<div class="sidenav">

<h1>Contribute</h1>
<ul>
  <li><a href="Contact.html">Contact the Owner</a></li>
  <li><a href="DNE.html">Suggest an Addition</a></li>
  <li><a href="DNE.html">Suggest a Correction</a></li>
</ul>
</div>

<div class="clearer">
<span></span></div>
</div>
</div>

<div class="footer">
© 2021 <a href="index.html">Website.com</a>. Valid <a
href="http://jigsaw.w3.org/css-validator/check/referer">CSS</a> &amp; <a
href="http://validator.w3.org/check?uri=referer">XHTML</a>. Template design by
<a href="http://arcsin.se">Arcsin</a> </div>
</body>
</html>''')
        


df_child = pd.read_excel('Holland-Walsh Family Tree.xlsx', sheet_name='Sheet3')
for row in df_child.itertuples():
    count = 5
    children_list = []
    while count < len(row):
        value = row[count]
        if pd.isna(value):
            break
        children_list.append(value)
        count += 1
    print(children_list)

create_html_file("test.html")