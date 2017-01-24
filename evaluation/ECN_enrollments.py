#These functions use data from the
#roster query in my reports
#use for finding total enrollments in ECN undergrad courses
#use for finding email addresses of students or professors
# in ECN undergraduate courses
import sys
sys.path.append('/Users/cmcdanie/Dropbox/python/ECNdepartment/library/')
import pandas as pd
from term_functions import previous_term


def prof_email(input_file, output_file):
    input_file = '/Users/cmcdanie/ECN_dept_data/input/ECN_enrollment_2171.csv'
    tbl = pd.read_csv(input_file, parse_dates=True, engine='python')
    #Asu Email Addr 2 is professor email
    emails = tbl[['Primary Instructor', 'Asu Email Addr2']]
    emails = emails.drop_duplicates()
    emails.to_csv(output_file, index=False)
    return emails


def enrollment_count(input_file, term, output_file):
    tbl = pd.read_csv(input_file, parse_dates=True, engine='python')
    tbl = tbl[tbl['Strm'] == term]
    enrollment = tbl['Catalog Nbr'].value_counts()
    enrollment.loc['Total'] = enrollment.sum()
    enrollment.to_csv('/Users/cmcdanie/ECN_dept_data/output/class_enrollment' + str(term) + '.csv')
    return enrollment

#Strm                  9325 non-null int64
#Term                  9325 non-null object
#Subject               9325 non-null object
#Catalog Nbr           9325 non-null int64
#Crse Id               9325 non-null int64
#Crse Offer Nbr        9325 non-null int64
#Class Nbr             9325 non-null int64
#Class Title           9325 non-null object
#Topic Title           116 non-null object
#Session Code          9325 non-null object
#Class Section         9325 non-null int64
#Class Career          9325 non-null object
#Class Type            9325 non-null object
#Component             9325 non-null object
#Primary Days          9325 non-null object
#Primary Time          7958 non-null object
#Building Code         9303 non-null object
#Room                  9303 non-null object
#Primary Instructor    9325 non-null object
#Capacity              9325 non-null int64
#Emplid                9325 non-null int64
#Posting Id            9325 non-null object
#Person Nm             9325 non-null object
#Stdnt Enrl Status     9325 non-null object
#Enrl Status Reason    9325 non-null object
#Grade Basis           9325 non-null object
#Unt Taken             9325 non-null int64
#Crse Grade Off        9325 non-null object
#Date Enrolled         9325 non-null object
#Date Dropped          0 non-null float64
#Program and Plan      9325 non-null object
#Academic Level        9325 non-null object
#Asu Asurite Id        9325 non-null object
#Asu Email Addr        9325 non-null object
#Ferpa Flg             9325 non-null object
#Asu Email Addr2       9325 non-null object
