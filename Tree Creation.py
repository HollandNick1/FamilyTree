import codecs
import pandas as pd

def create_tree_file(filename):
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
  	<link href="../ancestortree.css" media="screen" rel="stylesheet" type="text/css" />
	<link href="../narrative-print.css" media="print" rel="stylesheet" type="text/css" />
	<link href="../narrative-screen.css" media="screen" rel="stylesheet" type="text/css" />
	<link href="../Basic-Ash.css" media="screen" rel="alternate stylesheet" title="Basic-Ash" type="text/css" />
	<link href="../Basic-Blue.css" media="screen" rel="alternate stylesheet" title="Basic-Blue" type="text/css" />
	<link href="../Basic-Cypress.css" media="screen" rel="alternate stylesheet" title="Basic-Cypress" type="text/css" />
	<link href="../Basic-Lilac.css" media="screen" rel="alternate stylesheet" title="Basic-Lilac" type="text/css" />
	<link href="../Basic-Peach.css" media="screen" rel="alternate stylesheet" title="Basic-Peach" type="text/css" />
	<link href="../Basic-Spruce.css" media="screen" rel="alternate stylesheet" title="Basic-Spruce" type="text/css" />
	<link href="../Mainz.css" media="screen" rel="alternate stylesheet" title="Mainz" type="text/css" />
	<link href="../Nebraska.css" media="screen" rel="alternate stylesheet" title="Nebraska" type="text/css" />
  <title>Tree of {surname}, {forename}</title>
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
<body>
			<div id="tree">
				<div class="content_tree" id="toggle_anc" style="display:block">
					<div id="treeContainer" style="width:1234px; height:1200px; top: 0px">
						<div class="boxbg {gender.lower()} AncCol0" style="top: 530px; left: 6px;">
							<a class="noThumb" href="../People/{person_id}.html">
							{surname}, {forename}<br>*{dob}<br>+{dod}
							</a>
						</div>
						<div class="shadow" style="top: 535px; left: 10px;"></div>
						<div class="bvline" style="top: 550px; left: 285px; width: 15px"></div>
						<div class="gvline" style="top: 555px; left: 285px; width: 20px"></div>
						<div class="boxbg male AncCol1" style="top: 230px; left: 316px;">
							<a class="noThumb" href="../People/{ancestor1_id}.html">
							{ancestor1_surname}, {ancestor1_name}<br>*{ancestor1_dob}<br>+{ancestor1_dod}
							</a>
						</div>
						<div class="shadow" style="top: 235px; left: 320px;"></div>
						<div class="bvline" style="top: 250px; left: 300px; width: 15px;"></div>
					
						<div class="bhline" style="top: 250px; left: 300px; height: 301px;"></div>
					
						<div class="bvline" style="top: 250px; left: 595px; width: 15px"></div>
						<div class="gvline" style="top: 255px; left: 595px; width: 20px"></div>
						<div class="boxbg male AncCol2" style="top: 80px; left: 626px;">
							<a class="thumbnail" href="../People/{ancestor3_id}.html">
								<table class="table">
									<tr>
										<td class="name">
										{ancestor3_surname}, {ancestor3_name}<br>*{ancestor3_dob}<br>+{ancestor3_dod}
										</td>
									</tr>
								</table>
							</a>
						</div>
						<div class="shadow" style="top: 85px; left: 630px;"></div>
						<div class="bvline" style="top: 100px; left: 610px; width: 15px;"></div>
					
						<div class="bhline" style="top: 100px; left: 610px; height: 151px;"></div>
					
						<div class="bvline" style="top: 100px; left: 905px; width: 15px"></div>
						<div class="gvline" style="top: 105px; left: 905px; width: 20px"></div>
						<div class="boxbg male AncCol3" style="top: 5px; left: 936px;">
							<a class="thumbnail" href="../People/{ancestor7_id}.html">
								<table class="table">
									<tr>
										<td class="name">
										{ancestor7_surname}, {ancestor7_name}<br>*{ancestor7_dob}<br>+{ancestor7_dod}
										</td>
									</tr>
								</table>
							</a>
						</div>
						<div class="shadow" style="top: 10px; left: 940px;"></div>
						<div class="bvline" style="top: 25px; left: 920px; width: 15px;"></div>
					
						<div class="bhline" style="top: 25px; left: 920px; height: 76px;"></div>
					
						<div class="boxbg female AncCol3" style="top: 155px; left: 936px;">
							<a class="thumbnail" href="../People/{ancestor11_id}.html">
								<table class="table">
									<tr>
										<td class="name">
										{ancestor11_surname}, {ancestor11_name}<br>*{ancestor11_dob}<br>+{ancestor11_dod}
										</td>
									</tr>
								</table>
							</a>
						</div>
						<div class="shadow" style="top: 160px; left: 940px;"></div>
						<div class="bvline" style="top: 175px; left: 920px; width: 15px;"></div>
					
						<div class="bhline" style="top: 100px; left: 920px; height: 76px;"></div>
					
						<div class="boxbg female AncCol2" style="top: 380px; left: 626px;">
							<a class="thumbnail" href="../People/{ancestor5_id}.html">
								<table class="table">
									<tr>
										<td class="name">
										{ancestor5_surname}, {ancestor5_name}<br>*{ancestor5_dob}<br>+{ancestor5_dod}
										</td>
									</tr>
								</table>
							</a>
						</div>
						<div class="shadow" style="top: 385px; left: 630px;"></div>
						<div class="bvline" style="top: 400px; left: 610px; width: 15px;"></div>
					
						<div class="bhline" style="top: 250px; left: 610px; height: 151px;"></div>
					
						<div class="bvline" style="top: 400px; left: 905px; width: 15px"></div>
						<div class="gvline" style="top: 405px; left: 905px; width: 20px"></div>
						<div class="boxbg male AncCol3" style="top: 305px; left: 936px;">
							<a class="thumbnail" href="../People/{ancestor8_id}.html">
								<table class="table">
									<tr>
										<td class="name">
											{ancestor8_surname}, {ancestor8_name}<br>*{ancestor8_dob}<br>+{ancestor8_dod}
										</td>
									</tr>
								</table>
							</a>
						</div>
						<div class="shadow" style="top: 310px; left: 940px;"></div>
						<div class="bvline" style="top: 325px; left: 920px; width: 15px;"></div>
					
						<div class="bhline" style="top: 325px; left: 920px; height: 76px;"></div>
					
						<div class="boxbg female AncCol3" style="top: 455px; left: 936px;">
							<a class="noThumb" href="../People/{ancestor12_id}.html">
							{ancestor12_surname}, {ancestor12_name}<br>*{ancestor12_dob}<br>+{ancestor12_dod}
							</a>
						</div>
						<div class="shadow" style="top: 460px; left: 940px;"></div>
						<div class="bvline" style="top: 475px; left: 920px; width: 15px;"></div>
					
						<div class="bhline" style="top: 400px; left: 920px; height: 76px;"></div>
					
						<div class="boxbg female AncCol1" style="top: 830px; left: 316px;">
							<a class="noThumb" href="../People/{ancestor2_id}.html">
							{ancestor2_surname}, {ancestor2_name}<br>*{ancestor2_dob}<br>+{ancestor2_dod}
							</a>
						</div>
						<div class="shadow" style="top: 835px; left: 320px;"></div>
						<div class="bvline" style="top: 850px; left: 300px; width: 15px;"></div>
					
						<div class="bhline" style="top: 550px; left: 300px; height: 301px;"></div>
					
						<div class="bvline" style="top: 850px; left: 595px; width: 15px"></div>
						<div class="gvline" style="top: 855px; left: 595px; width: 20px"></div>
						<div class="boxbg male AncCol2" style="top: 680px; left: 626px;">
							<a class="noThumb" href="../People/{ancestor4_id}.html">
							{ancestor4_surname}, {ancestor4_name}<br>*{ancestor4_dob}<br>+{ancestor4_dod}
							</a>
						</div>
						<div class="shadow" style="top: 685px; left: 630px;"></div>
						<div class="bvline" style="top: 700px; left: 610px; width: 15px;"></div>
					
						<div class="bhline" style="top: 700px; left: 610px; height: 151px;"></div>
					
						<div class="bvline" style="top: 700px; left: 905px; width: 15px"></div>
						<div class="gvline" style="top: 705px; left: 905px; width: 20px"></div>
						<div class="boxbg male AncCol3" style="top: 605px; left: 936px;">
							<a class="thumbnail" href="../People/{ancestor9_id}.html">
								<table class="table">
									<tr>
										<td class="name">
										{ancestor9_surname}, {ancestor9_name}<br>*{ancestor9_dob}<br>+{ancestor9_dod}
										</td>
									</tr>
								</table>
							</a>
						</div>
						<div class="shadow" style="top: 610px; left: 940px;"></div>
						<div class="bvline" style="top: 625px; left: 920px; width: 15px;"></div>
					
						<div class="bhline" style="top: 625px; left: 920px; height: 76px;"></div>
					
						<div class="boxbg female AncCol3" style="top: 755px; left: 936px;">
							<a class="thumbnail" href="../People/{ancestor13_id}.html">
								<table class="table">
									<tr>
										<td class="name">
										{ancestor13_surname}, {ancestor13_name}<br>*{ancestor13_dob}<br>+{ancestor13_dod}
										</td>
									</tr>
								</table>
							</a>
						</div>
						<div class="shadow" style="top: 760px; left: 940px;"></div>
						<div class="bvline" style="top: 775px; left: 920px; width: 15px;"></div>
					
						<div class="bhline" style="top: 700px; left: 920px; height: 76px;"></div>
					
						<div class="boxbg female AncCol2" style="top: 980px; left: 626px;">
							<a class="thumbnail" href="../People/{ancestor6_id}.html">
								<table class="table">
									<tr>
										<td class="name">
										{ancestor6_surname}, {ancestor6_name}<br>*{ancestor6_dob}<br>+{ancestor6_dod}
										</td>
									</tr>
								</table>
							</a>
						</div>
						<div class="shadow" style="top: 985px; left: 630px;"></div>
						<div class="bvline" style="top: 1000px; left: 610px; width: 15px;"></div>
					
						<div class="bhline" style="top: 850px; left: 610px; height: 151px;"></div>
					
						<div class="bvline" style="top: 1000px; left: 905px; width: 15px"></div>
						<div class="gvline" style="top: 1005px; left: 905px; width: 20px"></div>
						<div class="boxbg male AncCol3" style="top: 905px; left: 936px;">
							<a class="thumbnail" href="../People/{ancestor10_id}.html">
								<table class="table">
									<tr>
										<td class="name">
										{ancestor10_surname}, {ancestor10_name}<br>*{ancestor10_dob}<br>+{ancestor10_dod}
										</td>
									</tr>
								</table>
							</a>
						</div>
						<div class="shadow" style="top: 910px; left: 940px;"></div>
						<div class="bvline" style="top: 925px; left: 920px; width: 15px;"></div>
					
						<div class="bhline" style="top: 925px; left: 920px; height: 76px;"></div>
					
						<div class="boxbg female AncCol3" style="top: 1055px; left: 936px;">
							<a class="thumbnail" href="../People/{ancestor14_id}.html">
								<table class="table">
									<tr>
										<td class="name">
										{ancestor14_surname}, {ancestor14_name}<br>*{ancestor14_dob}<br>+{ancestor14_dod}
										</td>
									</tr>
								</table>
							</a>
						</div>
						<div class="shadow" style="top: 1060px; left: 940px;"></div>
						<div class="bvline" style="top: 1075px; left: 920px; width: 15px;"></div>
					
						<div class="bhline" style="top: 1000px; left: 920px; height: 76px;"></div>
					
					</div>
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



  df_ancestor = pd.read_excel('Holland-Walsh Family Tree.xlsx', sheet_name='Sheet4')
  ancestor_row = df_ancestor[df_ancestor.iloc[:, 0] == person_id]
  ancestor1_id = "../DNE"
  ancestor1_name = "N"
  ancestor1_surname = "/ A"
  ancestor2_id = ""
  ancestor2_name = ""
  ancestor2_surname = ""
  ancestor3_id = ""
  ancestor3_name = ""
  ancestor3_surname = ""
  ancestor4_id = ""
  ancestor4_name = ""
  ancestor4_surname = ""
  ancestor5_id = ""
  ancestor5_name = ""
  ancestor5_surname = ""
  ancestor6_id = ""
  ancestor6_name = ""
  ancestor6_surname = ""
  ancestor7_id = ""
  ancestor7_name = ""
  ancestor7_surname = ""
  ancestor8_id = ""
  ancestor8_name = ""
  ancestor8_surname = ""
  ancestor9_id = ""
  ancestor9_name = ""
  ancestor9_surname = ""
  ancestor10_id = ""
  ancestor10_name = ""
  ancestor10_surname = ""
  ancestor11_id = ""
  ancestor11_name = ""
  ancestor11_surname = ""
  ancestor12_id = ""
  ancestor12_name = ""
  ancestor12_surname = ""
  ancestor13_id = ""
  ancestor13_name = ""
  ancestor13_surname = ""
  ancestor14_id = ""
  ancestor14_name = ""
  ancestor14_surname = ""

  if not ancestor_row.empty:
    ancestor_row_values = ancestor_row.iloc[0].values
    ancestor_count = 6
    ancestors_list = []
    while ancestor_count < len(ancestor_row_values):
      value = ancestor_row_values[ancestor_count]
      ancestors_list.append(value)
      ancestor_count += 1
    if ancestors_list:
      ancestor1_id = ancestors_list[0] if len(ancestors_list) > 0 else "DNE"
      ancestor1_name = ancestors_list[1] if len(ancestors_list) > 1 else "N"
      ancestor1_surname = ancestors_list[2] if len(ancestors_list) > 2 else "/ A"
      ancestor1_dob = ancestors_list[3] if len(ancestors_list) > 3 else "Unknown"
      ancestor1_dod = ancestors_list[4] if len(ancestors_list) > 4 else "Unknown"
      if ancestor1_dod == 0 or pd.isna(ancestor1_dod):
        if ancestor1_dod == "0":
          ancestor1_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor1_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor1_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor1_dod = "Living - Possibly Deceased"
            else:
              ancestor1_dod = "Living"
          except Exception:
            ancestor1_dod = "Living"
      if pd.isna(ancestor1_id) or ancestor1_id == 0:
        ancestor1_id = "../DNE"
        ancestor1_name = "Unknown"
        ancestor1_surname = "Ancestor"
        ancestor1_dob = "Unknown"
        ancestor1_dod = "Unknown"

      ancestor2_id = ancestors_list[5] if len(ancestors_list) > 5 else ""
      ancestor2_name = ancestors_list[6] if len(ancestors_list) > 6 else ""
      ancestor2_surname = ancestors_list[7] if len(ancestors_list) > 7 else ""
      ancestor2_dob = ancestors_list[8] if len(ancestors_list) > 8 else "Unknown"
      ancestor2_dod = ancestors_list[9] if len(ancestors_list) > 9 else "Unknown"
      if ancestor2_dod == 0 or pd.isna(ancestor2_dod):
        if ancestor2_dod == "0":
          ancestor2_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor2_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor2_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor2_dod = "Living - Possibly Deceased"
            else:
              ancestor2_dod = "Living"
          except Exception:
            ancestor2_dod = "Living"
      if pd.isna(ancestor2_id) or ancestor2_id == 0:
        ancestor2_id = "../DNE"
        ancestor2_name = "Unknown"
        ancestor2_surname = "Ancestor"
        ancestor2_dob = "Unknown"
        ancestor2_dod = "Unknown"

      ancestor3_id = ancestors_list[10] if len(ancestors_list) > 10 else ""
      ancestor3_name = ancestors_list[11] if len(ancestors_list) > 11 else ""
      ancestor3_surname = ancestors_list[12] if len(ancestors_list) > 12 else ""
      ancestor3_dob = ancestors_list[13] if len(ancestors_list) > 13 else "Unknown"
      ancestor3_dod = ancestors_list[14] if len(ancestors_list) > 14 else "Unknown"
      if ancestor3_dod == 0 or pd.isna(ancestor3_dod):
        if ancestor3_dod == "0":
          ancestor3_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor3_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor3_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor3_dod = "Living - Possibly Deceased"
            else:
              ancestor3_dod = "Living"
          except Exception:
            ancestor3_dod = "Living"
      if pd.isna(ancestor3_id) or ancestor3_id == 0:
        ancestor3_id = "../DNE"
        ancestor3_name = "Unknown"
        ancestor3_surname = "Ancestor"
        ancestor3_dob = "Unknown"
        ancestor3_dod = "Unknown"

      ancestor4_id = ancestors_list[15] if len(ancestors_list) > 15 else ""
      ancestor4_name = ancestors_list[16] if len(ancestors_list) > 16 else ""
      ancestor4_surname = ancestors_list[17] if len(ancestors_list) > 17 else ""
      ancestor4_dob = ancestors_list[18] if len(ancestors_list) > 18 else "Unknown"
      ancestor4_dod = ancestors_list[19] if len(ancestors_list) > 19 else "Unknown"
      if ancestor4_dod == 0 or pd.isna(ancestor4_dod):
        if ancestor4_dod == "0":
          ancestor4_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor4_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor4_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor4_dod = "Living - Possibly Deceased"
            else:
              ancestor4_dod = "Living"
          except Exception:
            ancestor4_dod = "Living"
      if pd.isna(ancestor4_id) or ancestor4_id == 0:
        ancestor4_id = "../DNE"
        ancestor4_name = "Unknown"
        ancestor4_surname = "Ancestor"
        ancestor4_dob = "Unknown"
        ancestor4_dod = "Unknown"

      ancestor5_id = ancestors_list[20] if len(ancestors_list) > 20 else ""
      ancestor5_name = ancestors_list[21] if len(ancestors_list) > 21 else ""
      ancestor5_surname = ancestors_list[22] if len(ancestors_list) > 22 else ""
      ancestor5_dob = ancestors_list[23] if len(ancestors_list) > 23 else "Unknown"
      ancestor5_dod = ancestors_list[24] if len(ancestors_list) > 24 else "Unknown"
      if ancestor5_dod == 0 or pd.isna(ancestor5_dod):
        if ancestor5_dod == "0":
          ancestor5_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor5_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor5_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor5_dod = "Living - Possibly Deceased"
            else:
              ancestor5_dod = "Living"
          except Exception:
            ancestor5_dod = "Living"
      if pd.isna(ancestor5_id) or ancestor5_id == 0:
        ancestor5_id = "../DNE"
        ancestor5_name = "Unknown"
        ancestor5_surname = "Ancestor"
        ancestor5_dob = "Unknown"
        ancestor5_dod = "Unknown"

      ancestor6_id = ancestors_list[25] if len(ancestors_list) > 25 else ""
      ancestor6_name = ancestors_list[26] if len(ancestors_list) > 26 else ""
      ancestor6_surname = ancestors_list[27] if len(ancestors_list) > 27 else ""
      ancestor6_dob = ancestors_list[28] if len(ancestors_list) > 28 else "Unknown"
      ancestor6_dod = ancestors_list[29] if len(ancestors_list) > 29 else "Unknown"
      if ancestor6_dod == 0 or pd.isna(ancestor6_dod):
        if ancestor6_dod == "0":
          ancestor6_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor6_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor6_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor6_dod = "Living - Possibly Deceased"
            else:
              ancestor6_dod = "Living"
          except Exception:
            ancestor6_dod = "Living"
      if pd.isna(ancestor6_id) or ancestor6_id == 0:
        ancestor6_id = "../DNE"
        ancestor6_name = "Unknown"
        ancestor6_surname = "Ancestor"
        ancestor6_dob = "Unknown"
        ancestor6_dod = "Unknown"

      ancestor7_id = ancestors_list[30] if len(ancestors_list) > 30 else ""
      ancestor7_name = ancestors_list[31] if len(ancestors_list) > 31 else ""
      ancestor7_surname = ancestors_list[32] if len(ancestors_list) > 32 else ""
      ancestor7_dob = ancestors_list[33] if len(ancestors_list) > 33 else "Unknown"
      ancestor7_dod = ancestors_list[34] if len(ancestors_list) > 34 else "Unknown"
      if ancestor7_dod == 0 or pd.isna(ancestor7_dod):
        if ancestor7_dod == "0":
          ancestor7_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor7_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor7_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor7_dod = "Living - Possibly Deceased"
            else:
              ancestor7_dod = "Living"
          except Exception:
            ancestor7_dod = "Living"
      if pd.isna(ancestor7_id) or ancestor7_id == 0:
        ancestor7_id = "../DNE"
        ancestor7_name = "Unknown"
        ancestor7_surname = "Ancestor"
        ancestor7_dob = "Unknown"
        ancestor7_dod = "Unknown"

      ancestor8_id = ancestors_list[35] if len(ancestors_list) > 35 else ""
      ancestor8_name = ancestors_list[36] if len(ancestors_list) > 36 else ""
      ancestor8_surname = ancestors_list[37] if len(ancestors_list) > 37 else ""
      ancestor8_dob = ancestors_list[38] if len(ancestors_list) > 38 else "Unknown"
      ancestor8_dod = ancestors_list[39] if len(ancestors_list) > 39 else "Unknown"
      if ancestor8_dod == 0 or pd.isna(ancestor8_dod):
        if ancestor8_dod == "0":
          ancestor8_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor8_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor8_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor8_dod = "Living - Possibly Deceased"
            else:
              ancestor8_dod = "Living"
          except Exception:
            ancestor8_dod = "Living"
          except Exception:
            ancestor8_dod = "Living"
      if pd.isna(ancestor8_id) or ancestor8_id == 0:
        ancestor8_id = "../DNE"
        ancestor8_name = "Unknown"
        ancestor8_surname = "Ancestor"
        ancestor8_dob = "Unknown"
        ancestor8_dod = "Unknown"
        
      ancestor9_id = ancestors_list[40] if len(ancestors_list) > 40 else ""
      ancestor9_name = ancestors_list[41] if len(ancestors_list) > 41 else ""
      ancestor9_surname = ancestors_list[42] if len(ancestors_list) > 42 else ""
      ancestor9_dob = ancestors_list[43] if len(ancestors_list) > 43 else "Unknown"
      ancestor9_dod = ancestors_list[44] if len(ancestors_list) > 44 else "Unknown"
      if ancestor9_dod == 0 or pd.isna(ancestor9_dod):
        if ancestor9_dod == "0":
          ancestor9_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor9_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor9_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor9_dod = "Living - Possibly Deceased"
            else:
              ancestor9_dod = "Living"
          except Exception:
            ancestor9_dod = "Living"
          except Exception:
            ancestor9_dod = "Living"
      if pd.isna(ancestor9_id) or ancestor9_id == 0:
        ancestor9_id = "../DNE"
        ancestor9_name = "Unknown"
        ancestor9_surname = "Ancestor"
        ancestor9_dob = "Unknown"
        ancestor9_dod = "Unknown"
        
      ancestor10_id = ancestors_list[45] if len(ancestors_list) > 45 else ""
      ancestor10_name = ancestors_list[46] if len(ancestors_list) > 46 else ""
      ancestor10_surname = ancestors_list[47] if len(ancestors_list) > 47 else ""
      ancestor10_dob = ancestors_list[48] if len(ancestors_list) > 48 else "Unknown"
      ancestor10_dod = ancestors_list[49] if len(ancestors_list) > 49 else "Unknown"
      if ancestor10_dod == 0 or pd.isna(ancestor10_dod):
        if ancestor10_dod == "0":
          ancestor10_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor10_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor10_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor10_dod = "Living - Possibly Deceased"
            else:
              ancestor10_dod = "Living"
          except Exception:
            ancestor10_dod = "Living"
          except Exception:
            ancestor10_dod = "Living"
      if pd.isna(ancestor10_id) or ancestor10_id == 0:
        ancestor10_id = "../DNE"
        ancestor10_name = "Unknown"
        ancestor10_surname = "Ancestor"
        ancestor10_dob = "Unknown"
        ancestor10_dod = "Unknown"
        
      ancestor11_id = ancestors_list[50] if len(ancestors_list) > 50 else ""
      ancestor11_name = ancestors_list[51] if len(ancestors_list) > 51 else ""
      ancestor11_surname = ancestors_list[52] if len(ancestors_list) > 52 else ""
      ancestor11_dob = ancestors_list[53] if len(ancestors_list) > 53 else "Unknown"
      ancestor11_dod = ancestors_list[54] if len(ancestors_list) > 54 else "Unknown"
      if ancestor11_dod == 0 or pd.isna(ancestor11_dod):
        if ancestor11_dod == "0":
          ancestor11_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor11_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor11_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor11_dod = "Living - Possibly Deceased"
            else:
              ancestor11_dod = "Living"
          except Exception:
            ancestor11_dod = "Living"
          except Exception:
            ancestor11_dod = "Living"
      if pd.isna(ancestor11_id) or ancestor11_id == 0:
        ancestor11_id = "../DNE"
        ancestor11_name = "Unknown"
        ancestor11_surname = "Ancestor"
        ancestor11_dob = "Unknown"
        ancestor11_dod = "Unknown"
        
      ancestor12_id = ancestors_list[55] if len(ancestors_list) > 55 else ""
      ancestor12_name = ancestors_list[56] if len(ancestors_list) > 56 else ""
      ancestor12_surname = ancestors_list[57] if len(ancestors_list) > 57 else ""
      ancestor12_dob = ancestors_list[58] if len(ancestors_list) > 58 else "Unknown"
      ancestor12_dod = ancestors_list[59] if len(ancestors_list) > 59 else "Unknown"
      if ancestor12_dod == 0 or pd.isna(ancestor12_dod):
        if ancestor12_dod == "0":
          ancestor12_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor12_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor12_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor12_dod = "Living - Possibly Deceased"
            else:
              ancestor12_dod = "Living"
          except Exception:
            ancestor12_dod = "Living"
          except Exception:
            ancestor12_dod = "Living"
      if pd.isna(ancestor12_id) or ancestor12_id == 0:
        ancestor12_id = "../DNE"
        ancestor12_name = "Unknown"
        ancestor12_surname = "Ancestor"
        ancestor12_dob = "Unknown"
        ancestor12_dod = "Unknown"
        
      ancestor13_id = ancestors_list[60] if len(ancestors_list) > 60 else ""
      ancestor13_name = ancestors_list[61] if len(ancestors_list) > 61 else ""
      ancestor13_surname = ancestors_list[62] if len(ancestors_list) > 62 else ""
      ancestor13_dob = ancestors_list[63] if len(ancestors_list) > 63 else "Unknown"
      ancestor13_dod = ancestors_list[64] if len(ancestors_list) > 64 else "Unknown"
      if ancestor13_dod == 0 or pd.isna(ancestor13_dod):
        if ancestor13_dod == "0":
          ancestor13_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor13_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor13_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor13_dod = "Living - Possibly Deceased"
            else:
              ancestor13_dod = "Living"
          except Exception:
            ancestor13_dod = "Living"
          except Exception:
            ancestor13_dod = "Living"
      if pd.isna(ancestor13_id) or ancestor13_id == 0:
        ancestor13_id = "../DNE"
        ancestor13_name = "Unknown"
        ancestor13_surname = "Ancestor"
        ancestor13_dob = "Unknown"
        ancestor13_dod = "Unknown"
        
      ancestor14_id = ancestors_list[65] if len(ancestors_list) > 65 else ""
      ancestor14_name = ancestors_list[66] if len(ancestors_list) > 66 else ""
      ancestor14_surname = ancestors_list[67] if len(ancestors_list) > 67 else ""
      ancestor14_dob = ancestors_list[68] if len(ancestors_list) > 68 else "Unknown"
      ancestor14_dod = ancestors_list[69] if len(ancestors_list) > 69 else "Unknown"
      if ancestor14_dod == 0 or pd.isna(ancestor14_dod):
        if ancestor14_dod == "0":
          ancestor14_dod = "Unknown"
        else:
          try:
            dob_year = pd.to_datetime(ancestor14_dob).year
            current_year = pd.Timestamp.now().year
            if current_year - dob_year > 100:
              ancestor14_dod = "Likely Deceased"
            elif current_year - dob_year > 80:
              ancestor14_dod = "Living - Possibly Deceased"
            else:
              ancestor14_dod = "Living"
          except Exception:
            ancestor14_dod = "Living"
          except Exception:
            ancestor14_dod = "Living"
      if pd.isna(ancestor14_id) or ancestor14_id == 0:
        ancestor14_id = "../DNE"
        ancestor14_name = "Unknown"
        ancestor14_surname = "Ancestor"
        ancestor14_dob = "Unknown"
        ancestor14_dod = "Unknown"
        
      print(f'Creating file {row[0]} / {len(df)}')



  filename = person_id
  create_tree_file(f"Trees/{filename} Tree.html")