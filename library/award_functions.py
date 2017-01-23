import numpy as np


def gpa_calc(df):
    # this takes a two column data frame and returns a single GPA value
    noGPA = ['-', 'Y', 'LC', 'Z', 'X', 'I']
    df = df[~df['Crse Grade Off'].isin(noGPA)]
    if len(df) == 0:
        return 0
    else:
        grdpt = {
            'A+': 4.33,
            'A': 4.0,
            'A-': 3.67,
            'B+': 3.33,
            'B': 3.0,
            'B-': 2.67,
            'C+': 2.33,
            'C': 2.0,
            'D': 1.0,
            'E': 0,
            'XE': 0}
        for l in grdpt:
            df['Crse Grade Off'][df['Crse Grade Off'] == l] = grdpt[l]
        pts = df['Crse Grade Off'] * df['Unt Taken']
        return np.sum(pts) / np.sum(df['Unt Taken'])


def subject_GPA(sub, df):
    df = df[df['Subject'] == sub]
    gpa = gpa_calc(df)
    return gpa


def drop_dup(df):
    k = ['Emplid', 'Strm', 'Class Nbr']
    return df.drop_duplicates(cols=k)


def strm_con(strm):
    terms = {'7': 'Fall', '4': 'Summer', '1': 'Spring', '0': 'Winter'}
    strm = str(strm)
    if len(strm) < 4:
        year = '?'
        term = '?'
    else:
        year = strm[0] + '0' + strm[1] + strm[2]
        term = terms[strm[3]]
    out = term + ' ' + year
    return out


def list_course_prof(df, fl):
    # sort on term
    from string import Template
    lst = Template('$trm \t $course \t  $number \t $grade \t $prof \n')
    df = df.sort_index(by=['Strm Enrl'], ascending=[True])
    for index, row in df.iterrows():
        nterm = strm_con(row['Strm Enrl'])
    instr = str(row['Instructor']).split(',')[0]
    x = lst.substitute(
        trm=nterm,
        course=row['Subject'],
        number=row['Catalog Nbr'],
        grade=row['Crse Grade Off'],
        prof=instr)
    fl.write(x)


def list_course_noprof(df, fl):
    # sort on term
    from string import Template
    lst = Template('$trm \t $course \t  $number \t $grade \n')
    df = df.sort_index(by=['Strm Enrl'], ascending=[True])
    for index, row in df.iterrows():
        nterm = strm_con(row['Strm Enrl'])
        x = lst.substitute(
            trm=nterm,
            course=row['Subject'],
            number=row['Catalog Nbr'],
            grade=row['Crse Grade Off'])
        fl.write(x)


def make_header(df, fl):
    from string import Template
    hdr = Template(
        ' $Last, $First \t $ID \t Cum GPA: $GPA \t ECN GPA: $ECNGPA  \n')
    ECN_GPA = subject_GPA('ECN', df)
    xx = hdr.substitute(
        ID=list(
            df['Emplid'])[0], Last=list(
            df['Last Name'])[0], First=list(
            df['First Name'])[0], GPA=list(
            df['Cum Gpa'])[0], ECNGPA=(
            "%.2f" % ECN_GPA))
    fl.write(xx)


def make_header_docx(df, document, hdr_cells):
    ECN_GPA = subject_GPA('ECN', df)
    hdr_cells[0].text = str(list(df['Emplid'])[0])
    hdr_cells[1].text = list(df['Last Name'])[0]
    hdr_cells[2].text = list(df['First Name'])[0]
    hdr_cells[3].text = 'GPA: ' + str(list(df['Cum Gpa'])[0])
    hdr_cells[4].text = 'ECN GPA: ' + ("%.2f" % ECN_GPA)


def make_header2_docx(df, document, hdr_cells):
    hdr_cells[0].text = 'Term'
    hdr_cells[1].text = 'Subject'
    hdr_cells[2].text = ' '
    hdr_cells[3].text = ' '
    hdr_cells[4].text = 'Professor'


def make_header_Chase_docx(df, document, ECN_GPA, hdr_cells):
    hdr_cells[0].text = str(list(df['Emplid'])[0])
    hdr_cells[1].text = list(df['Last Name'])[0]
    hdr_cells[2].text = list(df['First Name'])[0]
    hdr_cells[3].text = 'GPA: ' + str(list(df['Cum Gpa'])[0])
    hdr_cells[4].text = 'ECN GPA: ' + ("%.2f" % ECN_GPA)


def list_courses_prof_docx(df, document, table):
    # sort on term
    df = df.sort_index(by=['Strm Enrl'], ascending=[True])
    for index, r in df.iterrows():
        nterm = strm_con(r['Strm Enrl'])
        instr = str(r['Instructor']).split(',')[0]
        row_cells = table.add_row().cells
        row_cells[0].text = nterm
        row_cells[1].text = r['Subject']
        row_cells[2].text = str(r['Catalog Nbr'])
        row_cells[3].text = r['Crse Grade Off']
        row_cells[4].text = instr


def list_courses_noprof_docx(df, document, table):
    # sort on term
    df = df.sort_index(by=['Strm Enrl'], ascending=[True])
    for index, r in df.iterrows():
        nterm = strm_con(r['Strm Enrl'])
        row_cells = table.add_row().cells
        row_cells[0].text = nterm
        row_cells[1].text = r['Subject']
        row_cells[2].text = str(int(r['Catalog Nbr']))
        row_cells[3].text = r['Crse Grade Off']


def student_report(ID, tbl):
    tbl = tbl[tbl['Emplid'] == ID]
    return tbl


# Emplid                6114  non-null values
# First Name            6114  non-null values
# Last Name             6114  non-null values
# Strm                  6114  non-null values
# Campus                6114  non-null values
# Acad Group            6114  non-null values
# Acad Career           6114  non-null values
# Acad Prog             6114  non-null values
# Acad Org              6114  non-null values
# Acad Plan             6114  non-null values
# Degree                6114  non-null values
# Trnscr Descr          6114  non-null values
# Strm Enrl             6114  non-null values
# Session Code          6114  non-null values
# Acad Group Course     6114  non-null values
# Subject               6114  non-null values
# Catalog Nbr           6114  non-null values
# Class Nbr             6114  non-null values
# Unt Taken             6114  non-null values
# Crse Grade Off        6114  non-null values
# Repeat Code           6114  non-null values
# Grading Basis Enrl    6114  non-null values
# Class Type            6114  non-null values
# Instruction Mode      6114  non-null values
# Location              6114  non-null values
# Class Mtg Nbr         5895  non-null values
# Days                  6114  non-null values
# Facility Id           5895  non-null values
# Instructor            5794  non-null values
# Tot Taken Gpa         6114  non-null values
# Acad Level Bot        6114  non-null values
# Acad Level Eot        6114  non-null values
# Tot Cumulative        6114  non-null values
# Tot Passd Prgrss      6114  non-null values
# Cum Gpa               6114  non-null values
# Trf Gpa               6114  non-null values


# for ID in IDs:
#	df = student_report(ID,tbl)
#	df = drop_dup(df)
#	print ID
#	make_header(df,tfile)
#	tfile.write('----ECN courses ----- \n ')
#	ECNs = df[df['Subject'] == 'ECN']
#	list_course_prof(ECNs,tfile)
#	tfile.write('---- MAT courses ----- \n')
#	MATs = df[df['Subject'].isin(['MAT','STP'])]
#	list_course_noprof(MATs,tfile)
#	#tfile.write('---------' + '\n')
#	tfile.write('\n')
#	tfile.write('\n')
