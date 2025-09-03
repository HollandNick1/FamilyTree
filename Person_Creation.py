import codecs
import pandas as pd

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
        <link rel="stylesheet" type="text/css" href="../default.css" media="screen">
        <title>{forename} {surname}</title>
      </head>

      <body>

      <div class="container">

      <div class="header">

      <div class="title">
      <h1>Family Tree</h1>
      </div>

      <div class="navigation">
      <a href="../index.html">Home</a>
      <a href="../Family Names.html">Family Names</a> 
      <a href="../DNE.html">People</a>
      <a href="../Overview.html">Overview</a>

      <div class="clearer">
      <span></span></div>
      </div>
      </div>

      <div class="main">

      <div class="content">

      <h1>
      {forename} {surname}
      </h1>

      <h3>
      Sex: 
      </h3>
      <p>
      {gender}
      </p>

      <h3>
      Date of Birth: 
      </h3>
      <p>
      {dob}
      </p>
      <h3>
      Date of Death: 
      </h3>
      <p>
      {dod}
      </p>

      <h3>
      Mother: 
      </h3>
      <p>
      <a href="{mother_id}.html">{mother_forename} {mother_surname}</a>
      </p>

      <h3>
      Father: 
      </h3>
      <p>
      <a href="{father_id}.html">{father_forename} {father_surname}</a>
      </p>

      <h3>
      Partner(s): 
      </h3>
      <p>
      <a href="{partner1_id}.html">{partner1_name} {partner1_surname}</a>
      </p>
      <p>
      <a href="{partner2_id}.html">{partner2_name} {partner2_surname}</a>
      </p>
      <p>
      <a href="{partner3_id}.html">{partner3_name} {partner3_surname}</a>
      </p>

      <h3>
      Child(ren): 
      </h3>
      <p>
      <a href="{child1_id}.html">{child1_name} {child1_surname}</a>
      </p>
      <p>
      <a href="{child2_id}.html">{child2_name} {child2_surname}</a>
      </p>
      <p>
      <a href="{child3_id}.html">{child3_name} {child3_surname}</a>
      </p>
      <p>
      <a href="{child4_id}.html">{child4_name} {child4_surname}</a>
      </p>
      <p>
      <a href="{child5_id}.html">{child5_name} {child5_surname}</a>
      </p>
      <p>
      <a href="{child6_id}.html">{child6_name} {child6_surname}</a>
      </p>
      <p>
      <a href="{child7_id}.html">{child7_name} {child7_surname}</a>
      </p>
      <p>
      <a href="{child8_id}.html">{child8_name} {child8_surname}</a>
      </p>
      <p>
      <a href="{child9_id}.html">{child9_name} {child9_surname}</a>
      </p>
      <p>
      <a href="{child10_id}.html">{child10_name} {child10_surname}</a>
      </p>

      <h3>
      <a href="../Trees/{person_id} Tree.html">View Tree</a>
      </h3>

      </div>

      <div class="sidenav">

      <h1>Contribute</h1>
      <ul>
        <li><a href="../Contact.html">Contact the Owner</a></li>
        <li><a href="../DNE.html">Suggest an Addition</a></li>
        <li><a href="../DNE.html">Suggest a Correction</a></li>
      </ul>
      </div>

      <div class="clearer">
      <span></span></div>
      </div>
      </div>

      <div class="footer">
      &copy; 2021 <a href="../index.html">Holland-Walsh Family Tree</a>. Valid <a
      href="http://jigsaw.w3.org/css-validator/check/referer">CSS</a> &amp; <a
      href="http://validator.w3.org/check?uri=referer">XHTML</a>. Template design by
      <a href="http://arcsin.se">Arcsin</a> </div>
      </body>
      </html>''')

df = pd.read_excel('Holland-Walsh Family Tree.xlsx', sheet_name='Sheet1')
for row in df.itertuples():
  forename = row[1]
  surname = row[2]
  gender = row[3]
  if gender == 'M':
    gender = "Male"
  elif gender == 'F':
    gender = "Female"
  else:
    gender = "Unknown"
  dob = row[4]
  if pd.isna(dob):
    dob = "Unknown"
  lob = row[5]
  dod = row[6]
  if pd.isna(dod):
    if dob == "Unknown":
      dod = "Unknown"
    else:
      try:
        dob_year = pd.to_datetime(dob).year
        current_year = pd.Timestamp.now().year
        if current_year - dob_year > 100:
          dod = "Likely Deceased"
        elif current_year - dob_year > 80:
          dod = "Living - Possibly Deceased"
        else:
          dod = "Living"
      except Exception:
        dod = "Living"
  lod = row[7]
  father_forename = row[8]
  if pd.isna(father_forename):
    father_forename = "Unknown"
  father_surname = row[9]
  if pd.isna(father_surname):
    father_surname = "Father"
  mother_forename = row[10]
  if pd.isna(mother_forename):
    mother_forename = "Unknown"
  mother_surname = row[11]
  if pd.isna(mother_surname):
    mother_surname = "Mother"
  person_id = row[12]
  father_id = row[13]
  if pd.isna(father_id):
    father_id = "../DNE"
  mother_id = row[14]
  if pd.isna(mother_id):
    mother_id = "../DNE"


  df_partner = pd.read_excel('Holland-Walsh Family Tree.xlsx', sheet_name='Sheet2')
  partner_row = df_partner[df_partner.iloc[:, 0] == person_id]
  partner1_id = "../DNE"
  partner1_name = "N"
  partner1_surname = "/ A"
  partner2_id = ""
  partner2_name = ""
  partner2_surname = ""
  partner3_id = ""
  partner3_name = ""
  partner3_surname = ""


  if not partner_row.empty:
    partner_row_values = partner_row.iloc[0].values
    partner_count = 4
    partner_list = []
    while partner_count < len(partner_row_values):
      value = partner_row_values[partner_count]
      if pd.isna(value):
        break
      partner_list.append(value)
      partner_count += 1
    if partner_list:
      partner1_id = partner_list[0] if len(partner_list) > 0 else "DNE"
      partner1_name = partner_list[1] if len(partner_list) > 1 else "N"
      partner1_surname = partner_list[2] if len(partner_list) > 2 else "/ A"
      partner2_id = partner_list[3] if len(partner_list) > 3 else ""
      partner2_name = partner_list[4] if len(partner_list) > 4 else ""
      partner2_surname = partner_list[5] if len(partner_list) > 5 else ""
      partner3_id = partner_list[6] if len(partner_list) > 6 else ""
      partner3_name = partner_list[7] if len(partner_list) > 7 else ""
      partner3_surname = partner_list[8] if len(partner_list) > 8 else ""



  df_child = pd.read_excel('Holland-Walsh Family Tree.xlsx', sheet_name='Sheet3')
  child_row = df_child[df_child.iloc[:, 0] == person_id]
  child1_id = "../DNE"
  child1_name = "N"
  child1_surname = "/ A"
  child2_id = ""
  child2_name = ""
  child2_surname = ""
  child3_id = ""
  child3_name = ""
  child3_surname = ""
  child4_id = ""
  child4_name = ""
  child4_surname = ""
  child5_id = ""
  child5_name = ""
  child5_surname = ""
  child6_id = ""
  child6_name = ""
  child6_surname = ""
  child7_id = ""
  child7_name = ""
  child7_surname = ""
  child8_id = ""
  child8_name = ""
  child8_surname = ""
  child9_id = ""
  child9_name = ""
  child9_surname = ""
  child10_id = ""
  child10_name = ""
  child10_surname = ""

  if not child_row.empty:
    child_row_values = child_row.iloc[0].values
    child_count = 4
    children_list = []
    while child_count < len(child_row_values):
      value = child_row_values[child_count]
      if pd.isna(value):
        break
      children_list.append(value)
      child_count += 1
    if children_list:
      child1_id = children_list[0] if len(children_list) > 0 else "DNE"
      child1_name = children_list[1] if len(children_list) > 1 else "N"
      child1_surname = children_list[2] if len(children_list) > 2 else "/ A"
      child2_id = children_list[3] if len(children_list) > 3 else ""
      child2_name = children_list[4] if len(children_list) > 4 else ""
      child2_surname = children_list[5] if len(children_list) > 5 else ""
      child3_id = children_list[6] if len(children_list) > 6 else ""
      child3_name = children_list[7] if len(children_list) > 7 else ""
      child3_surname = children_list[8] if len(children_list) > 8 else ""
      child4_id = children_list[9] if len(children_list) > 9 else ""
      child4_name = children_list[10] if len(children_list) > 10 else ""
      child4_surname = children_list[11] if len(children_list) > 11 else ""
      child5_id = children_list[12] if len(children_list) > 12 else ""
      child5_name = children_list[13] if len(children_list) > 13 else ""
      child5_surname = children_list[14] if len(children_list) > 14 else ""
      child6_id = children_list[15] if len(children_list) > 15 else ""
      child6_name = children_list[16] if len(children_list) > 16 else ""
      child6_surname = children_list[17] if len(children_list) > 17 else ""
      child7_id = children_list[18] if len(children_list) > 18 else ""
      child7_name = children_list[19] if len(children_list) > 19 else ""
      child7_surname = children_list[20] if len(children_list) > 20 else ""
      child8_id = children_list[21] if len(children_list) > 21 else ""
      child8_name = children_list[22] if len(children_list) > 22 else ""
      child8_surname = children_list[23] if len(children_list) > 23 else ""
      child9_id = children_list[24] if len(children_list) > 24 else ""
      child9_name = children_list[25] if len(children_list) > 25 else ""
      child9_surname = children_list[26] if len(children_list) > 26 else ""
      child10_id = children_list[27] if len(children_list) > 27 else ""
      child10_name = children_list[28] if len(children_list) > 28 else ""
      child10_surname = children_list[29] if len(children_list) > 29 else ""
      print(f'Creating file {row[0]} / {len(df)}')


  filename = person_id
  create_html_file(f"People/{filename}.html")