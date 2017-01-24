#use this program to create output for scholarships
#the  file contains all courses taken by ECN majors

import pandas as pd
import numpy as np
from docx import Document
from award_functions import *
document = Document()

tbl = pd.read_csv('../csv_files/WPC_out_2161.csv',parse_dates = True)

#condition on level, GPA and major - outstanding senior
tbl = tbl[tbl['Cum Gpa'] > 4.0]
tbl = tbl.sort(['Cum Gpa'], ascending = False)
#tbl = tbl[tbl['Acad Level Bot'] == 40]
tbl['Catalog Nbr'] = tbl['Catalog Nbr'].convert_objects(convert_numeric=True)
tbl = tbl[tbl['Acad Plan'] == 'BAECNBS']

#Rondthaler scholars
micro = tbl[tbl['Catalog Nbr'].isin([214,312])]['Emplid']
macro = tbl[tbl['Catalog Nbr'].isin([213,313])]['Emplid']
both = x = macro[macro.isin(micro) == True]


#students to create schedules
IDs = both.unique()
#IDs = pd.unique(macro)
email = []
count = 0
for ID in IDs:
	print ID
	df = student_report(ID,tbl)
	df = drop_dup(df)
        #count ECN 400-level
	ECNs = df[df['Subject'] == 'ECN']
        level = ECNs['Catalog Nbr'].convert_objects(convert_numeric=True)
        #df['Catalog Nbr'] = df['Catalog Nbr'].convert_objects(convert_numeric=True)
        print 'x'
        ECN_GPA = subject_GPA('ECN',df)
        table = document.add_table(rows=1, cols=5,style = 'MediumList2')
        hdr_cells = table.rows[0].cells
        make_header_docx(df,document,hdr_cells)
        list_courses_prof_docx(ECNs,document,table)
        MATs = df[df['Subject'].isin(['MAT','STP'])]
        list_courses_noprof_docx(MATs,document,table)
        paragraph = document.add_paragraph(' ')
        if count % 2 == 1:
                document.add_page_break()
        count = count + 1
document.save('Rondthaler.docx')
