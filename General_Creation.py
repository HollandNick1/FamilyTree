import codecs
import pandas as pd
import os

def create_index_file(filename):
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(f'''<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
  <meta name="description" content="Family Tree Site of Nickolas Holland">
  <meta name="keywords" content="Family Tree">
  <meta name="author" content="Nickolas Holland">
  <meta http-equiv="refresh" content="30">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="default.css" media="screen">
  <title>Home</title>
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
<a href="People.html">People</a>
<a href="Overview.html">Overview</a>

<div class="clearer">
<span></span></div>
</div>
</div>

<div class="main">

<div class="content">

<h1>
Welcome
</h1>

<div class="descr">
Introduction
</div>

<p>
This website was created in an effort to best display my genealogiacal
findings. It would be great to hear from you about what you may know that isn't
on the site. If you wish to suggest anything then you can make your way to the
contribute section on the left.
</p>

<p>
If you would like the details of a living family member made private then I
would be more than happy to do that.
</p>

<h1>
How to Use
</h1>

<div class="descr">
The ins and outs of the site
</div>

<p>
The site should be easy enough to figure out how to use but if you want some
help, here it is:
</p>

<ul>
  <li>
  Family Names - This link will take to a list of surnames on the site that
    you can click to take you to a list of people with that surname.
	</li>
  <li>
  People - This link will take you to a list of every person on the site
    and from there you can choose to see that person immediate tree or there
    info page.
	</li>
	<li>
	Overview - Overall statistics for the site
</ul>
</div>

<div class="sidenav">

<h1>Contribute</h1>
<ul>
  <li><a href="Contact.html">Contact the Owner</a></li>
  <li><a href="SuggestAdd.html">Suggest an Addition</a></li>
  <li><a href="SuggestCor.html">Suggest a Correction</a></li>
</ul>
</div>

<div class="clearer">
<span></span></div>
</div>
</div>

<div class="footer">
&copy; 2021 <a href="index.html">Website.com</a>. Valid <a
href="http://jigsaw.w3.org/css-validator/check/referer">CSS</a> &amp; <a
href="http://validator.w3.org/check?uri=referer">XHTML</a>. Template design by
<a href="http://arcsin.se">Arcsin</a> </div>
</body>
</html>
''')

def create_family_name_file(filename):
    # Ensure the Surnames directory exists
    os.makedirs("Surnames", exist_ok=True)
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(f'''<!DOCTYPE html> 
<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
  <meta name="description" content="Family Tree Site of Nickolas Holland">
  <meta name="keywords" content="Family Tree">
  <meta name="author" content="Nickolas Holland">
  <meta http-equiv="refresh" content="30">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="default.css" media="screen">
  <title>Family Names</title>
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
<a href="People.html">People</a>
<a href="Overview.html">Overview</a>

<div class="clearer">
<span></span></div>
</div>
</div>

<div class="main">

<div class="content">

<h1>
Family Names
</h1>
''')
        f.write('<div style="font-size:1.5em;">\n<ul>\n')
        f.write(''.join(f'<li><a href="Surnames/{surname}.html">{surname}</a></li>\n' for surname in sorted(df['Surname'].dropna().unique())))
        f.write('</ul>\n</div>')
        f.write(f'''<p>

            </p>
            </div>

            <div class="sidenav">

            <h1>Contribute</h1>
            <ul>
        <li><a href="Contact.html">Contact the Owner</a></li>
        <li><a href="SuggestAdd.html">Suggest an Addition</a></li>
        <li><a href="SuggestCor.html">Suggest a Correction</a></li>
            </ul>
            </div>

            <div class="clearer">
            <span></span></div>
            </div>
            </div>

            <div class="footer">
            &copy; 2021 <a href="index.html">Website.com</a>. Valid <a
            href="http://jigsaw.w3.org/css-validator/check/referer">CSS</a> &amp; <a
            href="http://validator.w3.org/check?uri=referer">XHTML</a>. Template design by
            <a href="http://arcsin.se">Arcsin</a> </div>
            </body>
            </html>''')

    # --- Add this section to create a HTML file for each surname ---
    for surname in sorted(df['Surname'].dropna().unique()):
        with codecs.open(f"Surnames/{surname}.html", 'w', 'utf-8') as sf:
            sf.write(f'''<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
  <meta name="description" content="Family Tree Site of Nickolas Holland">
  <meta name="keywords" content="Family Tree">
  <meta name="author" content="Nickolas Holland">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="../default.css" media="screen">
  <title>{surname} Family</title>
</head>
<body>
<div class="container">
<div class="header">
<div class="title">
<h1>{surname} Family</h1>
</div>
<div class="navigation">
<a href="../index.html">Home</a>
<a href="../Family Names.html">Family Names</a> 
<a href="../People.html">People</a>
<a href="../Overview.html">Overview</a>
<div class="clearer">
<span></span></div>
</div>
</div>
<div class="main">
<div class="content">
<h2>People with surname: {surname}</h2>
<ul>
''')
            # List all people with this surname, sorted by first name
            people = df[df['Surname'] == surname].copy()
            people = people.sort_values(by='First Name(s)', na_position='last')
            for _, row in people.iterrows():
              name = row.get('First Name(s)', 'Unknown')
              page = row.iloc[11] if len(row) > 11 else 'Unknown.html'
              sf.write(f'<li><a href="../People/{page}.html">{name} {surname}</a></li>\n')
            sf.write('''</ul>
          </div>
          <div class="sidenav">
          <h1>Contribute</h1>
          <ul>
          <li><a href="../Contact.html">Contact the Owner</a></li>
          <li><a href="../SuggestAdd.html">Suggest an Addition</a></li>
          <li><a href="../SuggestCor.html">Suggest a Correction</a></li>
          </ul>
          </div>
          <div class="clearer">
          <span></span></div>
          </div>
          </div>
          <div class="footer">
          &copy; 2021 <a href="../index.html">Website.com</a>. Valid <a
          href="http://jigsaw.w3.org/css-validator/check/referer">CSS</a> &amp; <a
          href="http://validator.w3.org/check?uri=referer">XHTML</a>. Template design by
          <a href="http://arcsin.se">Arcsin</a> </div>
          </body>
          </html>''')

def create_people_file(filename):
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(f'''<!DOCTYPE html>
            <html>
            <head>
        <meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
        <meta name="description" content="Family Tree Site of Nickolas Holland">
        <meta name="keywords" content="Family Tree">
        <meta name="author" content="Nickolas Holland">
        <meta http-equiv="refresh" content="30">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="default.css" media="screen">
        <title>People</title>
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
            <a href="People.html">People</a>
            <a href="Overview.html">Overview</a>

            <div class="clearer">
            <span></span></div>
            </div>
            </div>

            <div class="main">

            <div class="content">

            <h1>
            People
            </h1>
            <div style="font-size:1.5em;">
            <ul>
            ''')
        # List all people, sorted by first name then surname
        people = df.copy()
        people = people.sort_values(by=['First Name(s)', 'Surname'], na_position='last')
        for _, row in people.iterrows():
            first_name = row.get('First Name(s)', 'Unknown')
            surname = row.get('Surname', '')
            page = row.iloc[11] if len(row) > 11 else 'Unknown.html'
            f.write(f'<li><a href="{page}.html">{first_name} {surname}</a></li>\n')
        f.write('''</ul>
            </div>
            </div>

            <div class="sidenav">

            <h1>Contribute</h1>
            <ul>
        <li><a href="Contact.html">Contact the Owner</a></li>
        <li><a href="SuggestAdd.html">Suggest an Addition</a></li>
        <li><a href="SuggestCor.html">Suggest a Correction</a></li>
            </ul>
            </div>

            <div class="clearer">
            <span></span></div>
            </div>
            </div>

            <div class="footer">
            &copy; 2021 <a href="index.html">Website.com</a>. Valid <a
            href="http://jigsaw.w3.org/css-validator/check/referer">CSS</a> &amp; <a
            href="http://validator.w3.org/check?uri=referer">XHTML</a>. Template design by
            <a href="http://arcsin.se">Arcsin</a> </div>
            </body>
            </html>''')

def create_overview_file(filename):
    with codecs.open(filename, 'w', 'utf-8') as f:
        num_individuals = len(df)
        num_surnames = df['Surname'].nunique()
        f.write(f'''<!DOCTYPE html>
      <html>
      <head>
        <meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
        <meta name="description" content="Family Tree Site of Nickolas Holland">
        <meta name="keywords" content="Family Tree">
        <meta name="author" content="Nickolas Holland">
        <meta http-equiv="refresh" content="30">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="default.css" media="screen">
        <title>Overview</title>
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
      <a href="People.html">People</a>
      <a href="Overview.html">Overview</a>

      <div class="clearer">
      <span></span></div>
      </div>
      </div>

      <div class="main">

      <div class="content">

      <h1>
      Overview
      </h1>

      <div class="descr">
      Site Statistics
      </div>

      <p>
      There are <strong>{num_individuals}</strong> individuals in the Holland-Walsh Family Tree.
      </p>
      <p>
      There are <strong>{num_surnames}</strong> unique surnames represented.
      </p>

      </div>

      <div class="sidenav">

      <h1>Contribute</h1>
      <ul>
        <li><a href="Contact.html">Contact the Owner</a></li>
        <li><a href="SuggestAdd.html">Suggest an Addition</a></li>
        <li><a href="SuggestCor.html">Suggest a Correction</a></li>
      </ul>
      </div>

      <div class="clearer">
      <span></span></div>
      </div>
      </div>

      <div class="footer">
      &copy; 2021 <a href="index.html">Website.com</a>. Valid <a
      href="http://jigsaw.w3.org/css-validator/check/referer">CSS</a> &amp; <a
      href="http://validator.w3.org/check?uri=referer">XHTML</a>. Template design by
      <a href="http://arcsin.se">Arcsin</a> </div>
      </body>
      </html>''')

df = pd.read_excel('Holland-Walsh Family Tree.xlsx', sheet_name='Sheet1')

create_index_file(f"index.html")
create_family_name_file(f"Family Names.html")
create_people_file(f"People.html")
create_overview_file(f"Overview.html")