# ZENV GITHUB DOCS GEN
#//==================================================================================================

# google sheet auth libraries
import google.auth
import gspread
#from oauth2client.client import GoogleCredentials

# google sheet libraries
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# git libraries
import git
from git import Repo

# general libraries
import numpy as np
import time
import os
import re # regex
import shutil
import glob
import markdown
import pathlib


#//==================================================================================================
#// BASE VARIABLES 
rootdir = os.path.dirname(os.path.abspath(__file__))
repo_dir = str(rootdir) + "/" + "zenv" + "/"
output_dir = str(rootdir) + "/" + "output" + "/"

html_dir = str(output_dir) + "/" + "html" + "/"
repo_hip_dir = str(repo_dir) + "/" + "hip" + "/"

if not (os.path.exists(output_dir)):
  os.mkdir(output_dir)

#//==================================================================================================
# GOOGLE SHEET --  authorize google sheet access
def auth_gsheet_zenv():
  #sa = gspread.service_account(filename="credentials.json")
  #credentials, project = google.auth.default()
  #auth.authenticate_user()
  #creds, _ = default()
  #GoogleCredentials = gspread.authorize(credentials)
  GoogleCredentials_local = gspread.service_account(filename="credentials.json")
  print("======GOOGLE AUTHORIZED=======")
  return GoogleCredentials_local;

#//==================================================================================================
# GOOGLE SHEET -- import the sheet into panda DatatFrame 
def get_gsheet_zenv(GoogleCredentials_local):
  workbook = GoogleCredentials_local.open_by_url('https://docs.google.com/spreadsheets/d/1rPrqH1WnpWqXFze_Ly_jeYGvRRfyuh9olX2pTrEu19U/edit#gid=0')
  sheet = workbook.worksheet('HDA')
  data = sheet.get_all_values()
  df = pd.DataFrame(data)
  df.columns = df.iloc[0]
  df = df.iloc[1:]
  #print(tabulate(df, headers='keys', tablefmt='psql'))
  print("======GHSEET COMPLETE=======")
  return workbook , df;

#//==================================================================================================
# GIT -- Clone the  repo.
def git_clone_zenv():
  #shutil.rmtree(repo_dir) # delete temp cloned zenv dir
  git_url = '''https://github.com/CorvaeOboro/zenv.git'''
  print("======GIT CLONE " + str(git_url) + "=======")
  Repo.clone_from(git_url, repo_dir)
  print("======GIT CLONE COMPLETE=======")


#//==================================================================================================
#// UPDATE GSHEET
#//==================================================================================================
#//   ADD NEW FROM GITHUB TO GSHEET
#//====== GET NAMES FROM GITHUB , FOR EACH CHECK GHSSET for MATCH , IF NEW THEN ADD TO GSHEET AS NEW ROW  =======================================
def gsheet_update_zenv(workbook,df):
  new_offset = 200
  df = df.replace('', np.nan)
  total_columns = len(df.columns)
  sheet = workbook.worksheet('HDA')

  print (total_columns)
  values_list = sheet.row_values(1)
  print (values_list)
  name_index = values_list.index("NAME")
  datemodified_index = values_list.index("DATE_MODIFIED")

  EX_index = values_list.index("EX")
  EX_values_list = sheet.col_values(EX_index+1)
  IMG_index = values_list.index("IMG")
  IMG_values_list = sheet.col_values(IMG_index+1)

  print ("NAME INDEX = " + str(name_index))
  print ("DATMODIFIED INDEX = " + str(datemodified_index))
  name_values_list = sheet.col_values(name_index+1)
  print (name_values_list)

  #//=============================================
  iteration= 0
  name_iteration = 0
  for subdir, dirs, files in os.walk(repo_dir):
      for file in files:
          iteration += +1
          filepath = subdir + os.sep + file
          filename_string = str(file)

          if filepath.endswith(".hda"):
            name_iteration = 0
            name_exists = 0
            filename_found_string = "null"
            for i in name_values_list:
              current_name = name_values_list[name_iteration]
              name_iteration += 1
              if current_name.endswith(filename_string):
                name_exists = 1
                filename_found_string = filename_string
            if name_exists < 1 :
              print ("UNIQUE HDA FOUND ===   " + filename_string )
              sheet.update_cell((iteration+new_offset),(name_index+1), filename_string) # Update using cell coordinates
  # HIP check if image , check if hip
  #//=============================================
  name_iteration = 0
  for i in name_values_list:
    print(i)
    current_name = name_values_list[name_iteration]
    if current_name.endswith(".hda"):
      iteration= 0
      for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            iteration += 1
            filepath = subdir + os.sep + file
            filename_only = pathlib.Path(filepath).stem
            if filename_only in current_name:
              if filepath.endswith(".hip"):
                #EXAMPLE EXISTS
                sheet.update_cell((name_iteration+1),(EX_index+1), "1") # Update DATEMODIFIED
                print("EX FOUND = " + str(filename_only))
                time.sleep(1) # this is slow but neccesary currently due to the network request limit perhaps a better lib or way
              if filepath.endswith(".jpg"):
                #EXAMPLE EXISTS
                sheet.update_cell((name_iteration+1),(IMG_index+1), "1") # Update DATEMODIFIED
                print("IMG FOUND = " + str(filename_only))
                time.sleep(1) # this is slow but neccesary currently due to the network request limit perhaps a better lib or way

    name_iteration += 1







#//==================================================================================================
#// README MAIN
#//==================================================================================================
def gen_readme_main(workbook,df):
  print("======GENERATING README MAIN=======")
  #//   GENERATE README 
  #//====== GET NAMES FROM GSHEET , CREATE ORDERED LIST OF CATEGORIES , WRITE README MARKDOWN =======================================
  #rootdir= '/content/zhoudini'
  #rootdir= '/content/zenv'
  #imgsrc = "<img src=\"https://raw.githubusercontent.com/CorvaeOboro/zhoudini/master/icon/"
  imgsrc = "<img src=\"https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/"
  iconsize = "40"
  reponameurl = "https://github.com/corvaeoboro/zenv/"
  doublequote = '''"'''
  regex_underscore = re.compile('_')
  #%cd $rootdir

  total_columns = len(df.columns)
  total_output = 10
  col_name_list = df.columns.tolist()
  sheet = workbook.worksheet('HDA')
  print (total_columns)
  values_list = sheet.row_values(1)
  print (values_list)
  name_index = values_list.index("NAME")
  notes_index = values_list.index("NOTES")
  print ("NAME INDEX = " + str(name_index))
  name_values_list = sheet.col_values(name_index+1)
  notes_list = sheet.col_values(notes_index+1)

  TYPE_index = values_list.index("TYPE")
  TYPE_values_list = sheet.col_values(TYPE_index+1)
  TYPEorder_index = values_list.index("TYPE ORDER")
  TYPEorder_values_list = sheet.col_values(TYPEorder_index+1)
  README_index = values_list.index("README")
  README_values_list = sheet.col_values(README_index+1)
  ORDER_index = values_list.index("ORDER")
  ORDER_values_list = sheet.col_values(ORDER_index+1)

  num_absolute_index = values_list.index("NUM")

  print (TYPE_values_list)
  TYPE_cleaned = []
  TYPE_ORDER_cleaned = []
  #//=============================================
  # unique type list
  for current_TYPE in TYPE_values_list :
    if current_TYPE not in TYPE_cleaned :
      TYPE_cleaned.append(current_TYPE)
      TYPE_ORDER_cleaned.append(current_TYPE)
  print(" === CATEGORY UNIQUE = " + str(len(TYPE_cleaned)))
  # type order averaged 
  print(" === CATEGORY ORDER ===")
  clean_iteration =  0
  for current_TYPE_clean in TYPE_cleaned :
    type_iteration =  0
    for current_TYPE in TYPE_values_list :
      if ( current_TYPE_clean == current_TYPE ) :
        current_TYPE_ORDER = TYPEorder_values_list[type_iteration]
        #print(current_TYPE_ORDER)
        try:
          int(current_TYPE_ORDER)
        except ValueError:
          current_TYPE_ORDER = 0
          pass 
        if ( ( current_TYPE_ORDER != "" ) and ( int(float(current_TYPE_ORDER)) > 0 )  ):
          temp_TYPE_ORDER = int(current_TYPE_ORDER) 
          temp_order_num = TYPEorder_values_list[clean_iteration]
          try:
            int(temp_order_num)
          except ValueError:
            temp_order_num = 0
            pass 
          if (int(temp_order_num) > 0 ) :
            final_TYPE_ORDER = ( int(temp_TYPE_ORDER) + int(temp_order_num) ) / 2
            TYPE_ORDER_cleaned[clean_iteration] = final_TYPE_ORDER
          else :
            TYPE_ORDER_cleaned[clean_iteration] = temp_TYPE_ORDER
      type_iteration +=  1
    clean_iteration +=  1
  print(TYPE_cleaned)
  print(TYPE_ORDER_cleaned)
  #//=============================================
  print(" === FINAL ORDER ===")

  #// TEXT OUTPUT
  #%cd $rootdir
  textfile_output_filename = str(output_dir) + 'readme_main.txt'
  textfile_output_final = open(textfile_output_filename, 'w')
  time.sleep(0.3)

  #// TABLE OF CONTENTS
  print("+++++++++++ TABLE OF CONTENTS +++++++++++++")
  for current_final_TYPE in TYPE_cleaned : # for each category in the sorted list 
    readme_category_lowercaselink = str(current_final_TYPE).lower()
    link_tablecontents = "[ " + current_final_TYPE + " ]" + " ( " + "https://github.com/CorvaeOboro/zenv#" + readme_category_lowercaselink + " )"
    textfile_output_final.write(link_tablecontents)
    time.sleep(0.3)
    print(link_tablecontents)
  time.sleep(0.3)

  #// TOOLS LIST BY CATEGORY
  print("+++++++++++ TOOLS BY CATEGORY +++++++++++++")
  #%cd $rootdir
  category_child_list_final = []
  final_absolute_count_num = 0
  for current_final_TYPE in TYPE_cleaned : # for each category in the sorted list 
    readme_category = """## """ + str(current_final_TYPE) + """ ##"""
    textfile_output_final.write(readme_category)
    time.sleep(0.3)
    print(readme_category)
    textfile_output_final.write('\n') # newline
    name_num = 0
    category_child_list_final = []
    category_child_num_list_final = []
    category_child_notes_list_final = []
    for current_final_name in name_values_list : # for each named tool
      if ( current_final_TYPE == TYPE_values_list[name_num]) : # if the type matches
        if ( README_values_list[name_num] == "1") : # if the readme_on cell value is 1
          category_child_list_final.append(current_final_name) # add the current tool to the category section
          category_child_num_list_final.append(ORDER_values_list[name_num]) # add the current tool to the category section
          category_child_notes_list_final.append(notes_list[name_num]) # add the current tool to the category section
      name_num = name_num + 1 #iterate the name list
    #print(category_child_list_final)
    #print(category_child_num_list_final)
    names_sorted_final = [xu for _,xu in sorted(zip(category_child_num_list_final,category_child_list_final))]
    notes_sorted_final = [xy for _,xy in sorted(zip(category_child_num_list_final,category_child_notes_list_final))]
    # tool table info
    readme_table = "|  ______    |      |      |"  # need to have charsacters in first slot to fix image squishing
    readme_table_align = "| :--- | :--- | :--- |"
    print(readme_table)
    print(readme_table_align)
    textfile_output_final.write(readme_table)
    time.sleep(0.3)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(readme_table_align)
    time.sleep(0.3)
    textfile_output_final.write('\n') # newline
    time.sleep(0.3)

    final_output_num = 0
    for final_names in names_sorted_final :
      filename_noext = final_names[:-4]
      filename_short = filename_noext[0:15]
      filename_short_end = filename_noext[15:]
      filename_short_spaces = re.sub( "_" , " " , filename_noext)
      current_notes = notes_sorted_final[final_output_num]
      # <a href="" rel="some text"><img src="/path/to/file" alt="" /></a>
      linkcurrent = reponameurl + "tree/master/hip/" + filename_noext
      #readme_output =  "- " + imgsrc + filename_noext + "_icon.png\" width = \"" + iconsize + "\" height = \"" + iconsize + "\"/> " + "**[" + filename_noext + "](" + reponameurl + ")** : " + current_notes
      readme_output =  "|" + "<a href=" + doublequote + linkcurrent + doublequote + ">" + imgsrc + filename_noext + "_icon.png\" width = \"" + iconsize + "\" height = \"" + iconsize + "\"/></a>| " + "**[" + filename_short_spaces + "](" + reponameurl + "tree/master/hip/" + filename_noext + ")**|" + current_notes.strip() + "|"
      textfile_output_final.write(readme_output)
      time.sleep(0.3)
      print(readme_output)
      textfile_output_final.write('\n') # newline
      time.sleep(0.4)
      #if not os.path.isdir(filename_noext) :
        #os.mkdir(filename_noext)
      final_output_num = final_output_num+1
    # FINAL NUMBERING OF GSHEET
    final_absolute_num = 0
    for final_names in names_sorted_final :
      filename_noext = final_names[:-4]
      current_name_num = 0
      for name_temp in name_values_list :
        if name_temp == final_names :
          temp_absolute_count_combined = final_absolute_num + ( int(TYPEorder_values_list[current_name_num]) * 100 )
          #sheet.update_cell((current_name_num+1),(num_absolute_index+1), str(temp_absolute_count_combined)) # Update using cell coordinates
          #print(final_names + "=== " + str(temp_absolute_count_combined))
          time.sleep(0.4)
        current_name_num = current_name_num+1
      final_absolute_num = final_absolute_num+1
    final_absolute_count_num = final_absolute_count_num +100

  #complete text file :
  time.sleep(0.3)
  textfile_output_final.close
  time.sleep(0.3)
  #//====================================================================================
  # download generated text output
  #files.download(rootdir + "/" + textfile_output_filename)

  print("+++++++++++ COMPLETE +++++++++++++")

#//==================================================================================================
#// README COMBINED
#//==================================================================================================
def gen_readme_combined(workbook,df):
  #//   GENERATE COMBINED README WITH ALL READMES
  #//====== COLLECTS LOCAL GIT CLONES READMES AND COMBINES , IMPORTANT TO RUN WITHOUT HAVING GENERATED READMEs  =======================================

  # start readme_all.md
  #%cd '/content/'
  readme_all_txtfile = str(output_dir) + 'readme_all.md'
  textfile_output_final = open(readme_all_txtfile, 'w')
  time.sleep(0.3)

  #%cd '/content/'
  #rootdir= '/content/zenv'
  imgsrc = '''<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/'''
  iconsize = "16"
  reponameurl = "https://github.com/corvaeoboro/zenv/"
  single_quote = "'"
  

  html_start_alpha = '''
  <html >
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>em_characters</title>
  <style type="text/css">
  <!--
  body {
    font-family: Verdana, Arial, Helvetica, sans-serif;
    color: #BBBBBB;
  }
  -->
  </style></head>

  <body style="background-color:#0d1117;">
  '''
  html_end_alpha = '''
  </body>
  </html>
  '''

  # docs folder for all the htmls
  if not (os.path.exists(html_dir)):
    os.mkdir(html_dir)

  #//=========================== VARS ================================
  total_columns = len(df.columns)
  total_output = 10
  col_name_list = df.columns.tolist()
  sheet = workbook.worksheet('HDA')
  print (total_columns)
  values_list = sheet.row_values(1)
  print (values_list)
  name_index = values_list.index("NAME")
  notes_index = values_list.index("NOTES")
  print ("NAME INDEX = " + str(name_index))
  name_values_list = sheet.col_values(name_index+1)
  notes_list = sheet.col_values(notes_index+1)

  TYPE_index = values_list.index("TYPE")
  TYPE_values_list = sheet.col_values(TYPE_index+1)
  TYPEorder_index = values_list.index("TYPE ORDER")
  TYPEorder_values_list = sheet.col_values(TYPEorder_index+1)
  README_index = values_list.index("README")
  README_values_list = sheet.col_values(README_index+1)
  ORDER_index = values_list.index("ORDER")
  ORDER_values_list = sheet.col_values(ORDER_index+1)

  num_absolute_index = values_list.index("NUM")

  print (TYPE_values_list)
  TYPE_cleaned = []
  TYPE_ORDER_cleaned = []
  #//=============================================
  # unique type list
  for current_TYPE in TYPE_values_list :
    if current_TYPE not in TYPE_cleaned :
      TYPE_cleaned.append(current_TYPE)
      TYPE_ORDER_cleaned.append(current_TYPE)
  print(" === CATEGORY UNIQUE = " + str(len(TYPE_cleaned)))
  # type order averaged 
  print(" === CATEGORY ORDER ===")
  clean_iteration =  0
  for current_TYPE_clean in TYPE_cleaned :
    type_iteration =  0
    for current_TYPE in TYPE_values_list :
      if ( current_TYPE_clean == current_TYPE ) :
        current_TYPE_ORDER = TYPEorder_values_list[type_iteration]
        #print(current_TYPE_ORDER)
        try:
          int(current_TYPE_ORDER)
        except ValueError:
          current_TYPE_ORDER = 0
          pass 
        if ( ( current_TYPE_ORDER != "" ) and ( int(float(current_TYPE_ORDER)) > 0 )  ):
          temp_TYPE_ORDER = int(current_TYPE_ORDER) 
          temp_order_num = TYPEorder_values_list[clean_iteration]
          try:
            int(temp_order_num)
          except ValueError:
            temp_order_num = 0
            pass 
          if (int(temp_order_num) > 0 ) :
            final_TYPE_ORDER = ( int(temp_TYPE_ORDER) + int(temp_order_num) ) / 2
            TYPE_ORDER_cleaned[clean_iteration] = final_TYPE_ORDER
          else :
            TYPE_ORDER_cleaned[clean_iteration] = temp_TYPE_ORDER
      type_iteration +=  1
    clean_iteration +=  1
  print(TYPE_cleaned)
  print(TYPE_ORDER_cleaned)
  #//=============================================
  print(" === FINAL ORDER ===")


  #// TABLE OF CONTENTS
  print("+++++++++++ TABLE OF CONTENTS +++++++++++++")
  for current_final_TYPE in TYPE_cleaned : # for each category in the sorted list 
    readme_category_lowercaselink = str(current_final_TYPE).lower()
    link_tablecontents = "[ " + current_final_TYPE + " ]" + " ( " + "https://github.com/CorvaeOboro/zenv#" + readme_category_lowercaselink + " )"
    #textfile_output_final.write(link_tablecontents)
    time.sleep(0.1)
    print(link_tablecontents)
  time.sleep(0.3)

  #// TOOLS LIST BY CATEGORY
  print("+++++++++++ TOOLS BY CATEGORY +++++++++++++")
  #%cd /content/hip
  category_child_list_final = []
  final_absolute_count_num = 0
  for current_final_TYPE in TYPE_cleaned : # for each category in the sorted list 
    print("===" + str(current_final_TYPE) + "===")
    readme_category = """## """ + str(current_final_TYPE) + """ ##"""
    # start readme_all.md
    #%cd '/content/'
    readme_cat_txtfile = str(html_dir) + str(current_final_TYPE) + ".html"
    textfile_cat_output_final = open(readme_cat_txtfile, 'w')
    time.sleep(0.3)
    textfile_cat_output_final.write(str(html_start_alpha))
    time.sleep(0.3)


    #textfile_output_final.write(readme_category)
    #print(html_comment_line_info)
    #textfile_output_final.write('\n') # newline
    name_num = 0
    category_child_list_final = []
    category_child_num_list_final = []
    category_child_notes_list_final = []
    for current_final_name in name_values_list : # for each named tool
      if ( current_final_TYPE == TYPE_values_list[name_num]) : # if the type matches
        if ( README_values_list[name_num] == "1") : # if the readme_on cell value is 1
          category_child_list_final.append(current_final_name) # add the current tool to the category section
          category_child_num_list_final.append(ORDER_values_list[name_num]) # add the current tool to the category section
          category_child_notes_list_final.append(notes_list[name_num]) # add the current tool to the category section
      name_num = name_num + 1 #iterate the name list
    #print(category_child_list_final)
    #print(category_child_num_list_final)
    names_sorted_final = [xu for _,xu in sorted(zip(category_child_num_list_final,category_child_list_final))]
    notes_sorted_final = [xy for _,xy in sorted(zip(category_child_num_list_final,category_child_notes_list_final))]
    # tool table info


    final_output_num = 0
    print(names_sorted_final)
    #// FINAL NAMES 
    for final_names in names_sorted_final :
      filename_noext = final_names[:-4]
      filename_noextnoz = filename_noext[2:]
      filename_short_spaces = re.sub( "_" , " " , filename_noextnoz)
      current_notes = notes_sorted_final[final_output_num]
      #readme_output =  "- " + imgsrc + filename_noext + "_icon.png\" width = \"" + iconsize + "\" height = \"" + iconsize + "\"/> " + "**[" + filename_noext + "](" + reponameurl + ")** : " + current_notes
      #readme_output =  "|" + filename_noext + "**[" + filename_short + " " + filename_short_end + "](" + reponameurl + "tree/master/hip/" + filename_noext + ")" 

      #current_readme_name_existing = filename_noext + ".md"
      current_readme_name_existing = "readme" + ".md"
      current_readme_full_path = repo_hip_dir + filename_noext + '''/''' + current_readme_name_existing
      current_readme_name_existing_cap = "README" + ".md"
      current_readme_full_path_cap = repo_hip_dir + filename_noext + '''/''' + current_readme_name_existing_cap
      #print(current_readme_full_path)

      if os.path.exists(current_readme_full_path) or os.path.exists(current_readme_full_path_cap):
        with open(current_readme_full_path, "r") as infile:
          #print(current_readme_full_path)
          #infile = open(current_readme, 'r')
          #print(str(infile))
          text = infile.read()
          current_notes = markdown.markdown(text)
          print(current_notes)
          time.sleep(0.3)

          textfile_output_final.write('\n') # newline
          textfile_output_final.write(str(current_notes))
          time.sleep(0.3)
          textfile_cat_output_final.write('\n') # newline
          textfile_cat_output_final.write(str(current_notes))
          time.sleep(0.3)

          infile.close()
          time.sleep(0.3)

    # FINAL NUMBERING OF GSHEET
    final_absolute_num = 0

    final_absolute_count_num = final_absolute_count_num +100
    textfile_cat_output_final.write('\n') # newline
    textfile_cat_output_final.write(str(html_end_alpha))
    time.sleep(0.3)
    textfile_cat_output_final.close
    time.sleep(0.3)

  #for child_presorted in category_child_list_final :
  time.sleep(0.3)
  textfile_output_final.close
  time.sleep(5.0)
  readme_all_html_output =  str(output_dir) + 'readme_all_html.html'
  markdown.markdownFromFile(input=readme_all_txtfile, output=readme_all_html_output)
  time.sleep(0.3)

  print("+++++++++++ COMPLETE +++++++++++++")
  #!zip -r /content/readme_type_html.zip /content/html/
  #from google.colab import files
  #files.download("/content/readme_type_html.zip")
  #time.sleep(0.3)
  #files.download("/content/" + readme_all_txtfile)
  #time.sleep(0.3)
  #files.download("/content/" + "readme_all_html.html")
  print("+++++++++++ COMPLETED README HTML ZIP ++++++++++++")

#//==================================================================================================
#// WEBSITE MENU
#//==================================================================================================
def gen_website_menu(workbook,df):
  #//   GENERATE HTML WEBSITE MENU following the readme layout 
  print(" === GEN WEBSITE MENU ===")

  #%cd '/content/'
  #rootdir= '/content/zenv'
  imgsrc = '''<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/'''
  iconsize = "16"
  reponameurl = "https://github.com/corvaeoboro/zenv/"
  single_quote = "'"

  #//=========================== VARS ================================
  total_columns = len(df.columns)
  total_output = 10
  col_name_list = df.columns.tolist()
  sheet = workbook.worksheet('HDA')
  print (total_columns)
  values_list = sheet.row_values(1)
  print (values_list)
  name_index = values_list.index("NAME")
  notes_index = values_list.index("NOTES")
  print ("NAME INDEX = " + str(name_index))
  name_values_list = sheet.col_values(name_index+1)
  notes_list = sheet.col_values(notes_index+1)

  TYPE_index = values_list.index("TYPE")
  TYPE_values_list = sheet.col_values(TYPE_index+1)
  TYPEorder_index = values_list.index("TYPE ORDER")
  TYPEorder_values_list = sheet.col_values(TYPEorder_index+1)
  README_index = values_list.index("README")
  README_values_list = sheet.col_values(README_index+1)
  ORDER_index = values_list.index("ORDER")
  ORDER_values_list = sheet.col_values(ORDER_index+1)

  num_absolute_index = values_list.index("NUM")

  print (TYPE_values_list)
  TYPE_cleaned = []
  TYPE_ORDER_cleaned = []
  #//=============================================
  # unique type list
  for current_TYPE in TYPE_values_list :
    if current_TYPE not in TYPE_cleaned :
      TYPE_cleaned.append(current_TYPE)
      TYPE_ORDER_cleaned.append(current_TYPE)
  print(" === CATEGORY UNIQUE = " + str(len(TYPE_cleaned)))
  # type order averaged 
  print(" === CATEGORY ORDER ===")
  clean_iteration =  0
  for current_TYPE_clean in TYPE_cleaned :
    type_iteration =  0
    for current_TYPE in TYPE_values_list :
      if ( current_TYPE_clean == current_TYPE ) :
        current_TYPE_ORDER = TYPEorder_values_list[type_iteration]
        #print(current_TYPE_ORDER)
        try:
          int(current_TYPE_ORDER)
        except ValueError:
          current_TYPE_ORDER = 0
          pass 
        if ( ( current_TYPE_ORDER != "" ) and ( int(float(current_TYPE_ORDER)) > 0 )  ):
          temp_TYPE_ORDER = int(current_TYPE_ORDER) 
          temp_order_num = TYPEorder_values_list[clean_iteration]
          try:
            int(temp_order_num)
          except ValueError:
            temp_order_num = 0
            pass 
          if (int(temp_order_num) > 0 ) :
            final_TYPE_ORDER = ( int(temp_TYPE_ORDER) + int(temp_order_num) ) / 2
            TYPE_ORDER_cleaned[clean_iteration] = final_TYPE_ORDER
          else :
            TYPE_ORDER_cleaned[clean_iteration] = temp_TYPE_ORDER
      type_iteration +=  1
    clean_iteration +=  1
  print(TYPE_cleaned)
  print(TYPE_ORDER_cleaned)
  #//=============================================
  print(" === FINAL ORDER ===")

  #// TEXT OUTPUT
  website_menu_file = str(output_dir) + 'website_menu.txt'
  textfile_output_final = open(website_menu_file, 'w')
  time.sleep(0.3)

  #// TABLE OF CONTENTS
  print("+++++++++++ TABLE OF CONTENTS +++++++++++++")
  for current_final_TYPE in TYPE_cleaned : # for each category in the sorted list 
    readme_category_lowercaselink = str(current_final_TYPE).lower()
    link_tablecontents = "[ " + current_final_TYPE + " ]" + " ( " + "https://github.com/CorvaeOboro/zenv#" + readme_category_lowercaselink + " )"
    #textfile_output_final.write(link_tablecontents)
    time.sleep(0.3)
    print(link_tablecontents)
  time.sleep(0.3)

  #// TOOLS LIST BY CATEGORY
  print("+++++++++++ TOOLS BY CATEGORY +++++++++++++")
  #%cd /content/hip
  category_child_list_final = []
  final_absolute_count_num = 0
  for current_final_TYPE in TYPE_cleaned : # for each category in the sorted list 
    readme_category = """## """ + str(current_final_TYPE) + """ ##"""
    #//   HTML CATEGORY
    html_comment_line_break = '''<!-- //////////////////////////////////////////////////////////////////////////////////////// -->'''
    html_comment_line_info = '''<!-- Start of ''' + str(current_final_TYPE) + ''' container div -->'''
    html_comment_line_breakB = '''<!-- //////////////////////////////////////////////////////////////////////////////////////// -->'''
    html_div_title = '''<div class="NormalFlow">'''
    html_div_title_style = '''<p style="margin:0; font-weight:bold; padding:3px; letter-spacing:3px; font-size:small; text-align:left; font-family: Verdana, Arial, Helvetica, sans-serif;">'''
    #html_title_link = '''<a href="''' + str(current_final_TYPE) + '''.html''' + '''" target=body>''' + str(current_final_TYPE) + '''</a></p>'''
    html_title_link = '''<a href="''' + "type/" + str(current_final_TYPE) + '''.html''' + '''" target=body>''' + str(current_final_TYPE) + '''</a>'''
    html_title_expand_link = '''<a href="javascript:FlipDisplay(''' + single_quote + str(current_final_TYPE) + '''closed''' +  "','" + str(current_final_TYPE) + '''open''' + single_quote + ''')"> + </a></p>'''

    #//   HTML COLLAPSED CATEGORY
    html_category_start = '''<!-- Start of collapsed content div -->'''
    html_category_div = '''<div id="''' + str(current_final_TYPE) + '''closed''' + '''">'''
    #html_category_style = '''<p style="margin:0; text-align:left; font-family: Verdana, Arial, Helvetica, sans-serif;">'''
    #html_category_link = '''<a href="javascript:FlipDisplay(''' + single_quote + str(current_final_TYPE) + '''closed''' +  "','" + str(current_final_TYPE) + '''open''' + single_quote + ''')">  + expand + </a></p>'''
    html_category_div_end = '''</div>'''
    html_category_div_endB = '''<!-- End of collapsed content div -->'''

    #//   HTML EXPANDED CATEGORY START
    html_expanded_start = '''<!-- Start of expanded content div -->'''
    html_expanded_div = '''<div id="''' + str(current_final_TYPE) + '''open''' + '''" style="display:none;">'''
    html_expanded_style = '''<p style="margin:0; text-align:left; font-family: Verdana, Arial, Helvetica, sans-serif;">'''

    textfile_output_final.write(html_comment_line_break)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_comment_line_info)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_comment_line_breakB)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_div_title)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_div_title_style)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_title_link)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_title_expand_link)
    textfile_output_final.write('\n') # newline

    textfile_output_final.write(html_category_start)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_category_div)
    textfile_output_final.write('\n') # newline
    #textfile_output_final.write(html_category_style)
    #textfile_output_final.write('\n') # newline
    #textfile_output_final.write(html_category_link)
    #textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_category_div_end)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_category_div_endB)
    textfile_output_final.write('\n') # newline
    
    textfile_output_final.write(html_expanded_start)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_expanded_div)
    textfile_output_final.write('\n') # newline
    textfile_output_final.write(html_expanded_style)
    textfile_output_final.write('\n') # newline

    #textfile_output_final.write(readme_category)
    print(html_comment_line_info)
    #textfile_output_final.write('\n') # newline
    name_num = 0
    category_child_list_final = []
    category_child_num_list_final = []
    category_child_notes_list_final = []
    for current_final_name in name_values_list : # for each named tool
      if ( current_final_TYPE == TYPE_values_list[name_num]) : # if the type matches
        if ( README_values_list[name_num] == "1") : # if the readme_on cell value is 1
          category_child_list_final.append(current_final_name) # add the current tool to the category section
          category_child_num_list_final.append(ORDER_values_list[name_num]) # add the current tool to the category section
          category_child_notes_list_final.append(notes_list[name_num]) # add the current tool to the category section
      name_num = name_num + 1 #iterate the name list
    #print(category_child_list_final)
    #print(category_child_num_list_final)
    names_sorted_final = [xu for _,xu in sorted(zip(category_child_num_list_final,category_child_list_final))]
    notes_sorted_final = [xy for _,xy in sorted(zip(category_child_num_list_final,category_child_notes_list_final))]
    # tool table info
    readme_table = "|  ______    |      |      |"  # need to have charsacters in first slot to fix image squishing
    readme_table_align = "| :--- | :--- | :--- |"
    #print(readme_table)
    #print(readme_table_align)
    #textfile_output_final.write(readme_table)
    #textfile_output_final.write('\n') # newline
    #textfile_output_final.write(readme_table_align)
    #textfile_output_final.write('\n') # newline

    final_output_num = 0
    #// FINAL NAMES 
    for final_names in names_sorted_final :
      filename_noext = final_names[:-4]
      filename_noextnoz = filename_noext[2:]
      filename_short_spaces = re.sub( "_" , " " , filename_noextnoz)
      current_notes = notes_sorted_final[final_output_num]
      #readme_output =  "- " + imgsrc + filename_noext + "_icon.png\" width = \"" + iconsize + "\" height = \"" + iconsize + "\"/> " + "**[" + filename_noext + "](" + reponameurl + ")** : " + current_notes
      #readme_output =  "|" + filename_noext + "**[" + filename_short + " " + filename_short_end + "](" + reponameurl + "tree/master/hip/" + filename_noext + ")" 

      html_expanded_link_start = '''<p style="margin:0; text-align:left;font-family: Verdana, Arial, Helvetica, sans-serif;">'''
      html_expanded_link = '''<a href="hip/''' + filename_noext + '''.html''' + '''" target=body>''' 
      html_expanded_link_icon = imgsrc + filename_noext + '''_icon.png" width = "''' + iconsize + '''" height = \"''' + iconsize + '''"/>   '''
      html_expanded_link_name = filename_short_spaces 
      html_expanded_link_end = '''</a></p>'''
      html_expanded_link_combined = html_expanded_link_start + html_expanded_link + html_expanded_link_icon + html_expanded_link_name + html_expanded_link_end
      
      textfile_output_final.write(html_expanded_link_combined)
      print(html_expanded_link)
      textfile_output_final.write('\n') # newline
      time.sleep(0.3)
      final_output_num = final_output_num+1
    # FINAL NUMBERING OF GSHEET
    final_absolute_num = 0
    #html_expanded_collapse_link = '''<a href="javascript:FlipDisplay(''' + single_quote + str(current_final_TYPE) + '''closed''' + "','" + str(current_final_TYPE) + '''open''' + single_quote + ''')">____________</p>'''
    #html_expanded_collapse_end = '''<p style="margin:0; text-align:left;font-family: Verdana, Arial, Helvetica, sans-serif;">   - collapse - </a></p>'''
    #textfile_output_final.write(html_expanded_collapse_link)
    #textfile_output_final.write('\n') # newline
    #textfile_output_final.write(html_expanded_collapse_end)
    #textfile_output_final.write('\n') # newline

    html_expanded_div_end = '''</div>'''
    textfile_output_final.write(html_expanded_div_end)
    textfile_output_final.write('\n') # newline
    html_expanded_div_endB = '''<!-- End of expanded content div -->'''
    textfile_output_final.write(html_expanded_div_endB)
    textfile_output_final.write('\n') # newline
    time.sleep(0.3)
    
    final_absolute_count_num = final_absolute_count_num +100

  #for child_presorted in category_child_list_final :
  time.sleep(0.3)
  textfile_output_final.close
  time.sleep(0.3)
  #from google.colab import files
  #files.download("/content/" + website_menu_file)
  print("+++++++++++ COMPLETE +++++++++++++")

#//==================================================================================================
#// README TO HTML
#//==================================================================================================
def convert_readme_to_html():
  #//===================================================================================
  #//====== CONVERT HIP READMEs to HTML
  # search for all the readme.md in the hip directory 

  # docs folder for all the htmls
  docs_directory = str(output_dir) + "/docs/" 
  if not (os.path.exists(docs_directory)):
    os.mkdir(docs_directory)

  # output folder for all the htmls
  output_directory = str(output_dir) + "/docs/hip/" 
  if not (os.path.exists(output_directory)):
    os.mkdir(output_directory)

  html_start = "<html>"
  html_start_end = "</html>"
  html_head = "<head>"
  html_head_end = "</head>"
  html_title = "<title>"
  html_title_end = "</title>"
  html_body = '''<body style="background-color:#0d1117;">'''
  html_body_end = "</body>"
  html_style = '''<style type="text/css">
  <!--
  body {
    font-family: Verdana, Arial, Helvetica, sans-serif;
    color: #BBBBBB;
  }
  -->
  </style>'''
  html_style_end = "</p>"

  # for each md in hip folder
  shape_set = glob.glob(os.path.join(repo_hip_dir, "**/*.md"))

  for current_readme in shape_set :
    print("CURRENT README == " + str(current_readme))
    #%cd $output_directory
    current_path_full = pathlib.Path(current_readme)
    current_path_full.absolute()
    #current_readme_filename_noext = pathlib.Path(current_path_full).parent
    current_readme_filename_noext = os.path.split(os.path.dirname(current_path_full))[1]
    print("CURRENT FILENAME == " + str(current_readme_filename_noext))
    readme_html_output = str(output_directory) + str(current_readme_filename_noext) + '.html'
    textfile_output_final = open(readme_html_output, 'w')
    time.sleep(0.3)

    with open(current_readme, "r") as infile:
      # html start
      textfile_output_final.write(str(html_start)) #html
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_head)) #head
      textfile_output_final.write('\n') # newline
      # title
      textfile_output_final.write(str(html_title)) #title
      textfile_output_final.write(str(current_readme_filename_noext))
      textfile_output_final.write(str(html_title_end)) #title_end
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_head_end)) #head_end
      textfile_output_final.write('\n') # newline
      # body
      textfile_output_final.write(str(html_body)) #body
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_style)) #style
      textfile_output_final.write('\n') # newline

      # content
      text = infile.read()
      current_notes = markdown.markdown(text)
      time.sleep(0.3)
      textfile_output_final.write(str(current_notes))
      time.sleep(0.3)
      infile.close()

      # end html
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_style_end)) #style_end
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_body_end)) #body_end
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_start_end)) #html_start_end

    time.sleep(0.3)
    textfile_output_final.close()
    time.sleep(0.3)

  print("+++++++++++ COMPLETED CONVERTING READMEs to HTMLs +++++++++++++")

def convert_readme_main_to_html():
  #//===================================================================================
  #//====== CONVERT MAIN README TO HTML
  print("==== CONVERT MAIN README TO HTML ==== ")

  # docs folder for all the htmls
  docs_directory = str(output_dir) + "/docs/" 
  if not (os.path.exists(docs_directory)):
    os.mkdir(docs_directory)

  # output folder for all the htmls
  output_directory = str(output_dir) + "/docs/hip/" 
  if not (os.path.exists(output_directory)):
    os.mkdir(output_directory)


  html_start = "<html>"
  html_start_end = "</html>"
  html_head = "<head>"
  html_head_end = "</head>"
  html_title = "<title>"
  html_title_end = "</title>"
  html_body = '''<body style="background-color:#0d1117;">'''
  html_body_end = "</body>"
  html_style = '''<style type="text/css">
  <!--
  body {
    font-family: Verdana, Arial, Helvetica, sans-serif;
    color: #BBBBBB;
  }
  -->
  </style>'''
  html_style_end = "</p>"

  # for each md in hip folder

  shape_set = glob.glob(os.path.join(repo_dir, "README.md"))

  for current_readme in shape_set :
    print("CURRENT README == " + str(current_readme))
    #%cd $output_directory
    current_path_full = pathlib.Path(current_readme)
    current_path_full.absolute()
    current_readme_filename_noext_stem = current_path_full.stem
    #current_readme_filename_noext = pathlib.Path(current_path_full).parent
    current_readme_filename_noext = os.path.split(os.path.dirname(current_path_full))[1]
    print("CURRENT FILENAME == " + str(current_readme_filename_noext))
    readme_html_output = str(output_dir) + str(current_readme_filename_noext) + '_' + current_readme_filename_noext_stem + '.html'
    textfile_output_final = open(readme_html_output, 'w')
    time.sleep(0.3)

    with open(current_readme, "r") as infile:
      # html start
      textfile_output_final.write(str(html_start)) #html
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_head)) #head
      textfile_output_final.write('\n') # newline
      # title
      textfile_output_final.write(str(html_title)) #title
      textfile_output_final.write(str(current_readme_filename_noext))
      textfile_output_final.write(str(html_title_end)) #title_end
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_head_end)) #head_end
      textfile_output_final.write('\n') # newline
      # body
      textfile_output_final.write(str(html_body)) #body
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_style)) #style
      textfile_output_final.write('\n') # newline

      # content
      text = infile.read()
      current_notes = markdown.markdown(text,extensions=['markdown.extensions.tables'])
      
      #converter = markdown.Markdown(extras=["tables"])  # <-- markdown tables
      #extensions=['markdown.extensions.tables']
      #current_notes = converter.convert(text)

      time.sleep(0.3)
      textfile_output_final.write(str(current_notes))
      time.sleep(0.3)
      infile.close()
      time.sleep(0.3)

      # end html
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_style_end)) #style_end
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_body_end)) #body_end
      textfile_output_final.write('\n') # newline
      textfile_output_final.write(str(html_start_end)) #html_start_end

    time.sleep(0.3)
    textfile_output_final.close()
    time.sleep(0.3)
  #!zip -r /content/file_main_html.zip /content/zenv/docs/hip
  #from google.colab import files
  #files.download("/content/zenv/docs/zenv_README.html")
  print("+++++++++++ COMPLETED CONVERTING README  MAIN to HTMLs +++++++++++++")

#//==================================================================================================
#// MAIN - auth gsheet git , generate readme and html docs
#//==================================================================================================
gc = auth_gsheet_zenv()
workbook , df = get_gsheet_zenv(gc)
git_clone_zenv()

gsheet_update_zenv(workbook,df)

#gen_readme_main(workbook,df)
#gen_readme_combined(workbook,df)
#gen_website_menu(workbook,df)

#convert_readme_to_html()
#convert_readme_main_to_html()

#readme_all_txtfile = str(output_dir) + 'readme_all.md'
#readme_all_html_output =  str(output_dir) + 'readme_all_html.html'
#markdown.markdownFromFile(input=readme_all_txtfile, output=readme_all_html_output)
