import sys
sys.path.append('/Users/cmcdanie/ECNdept/dept_python/library/')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from term_functions import previous_term, spring_fall_only, term_label_list
from ECN_enrollments import enrollment_count

file_nm = '/Users/cmcdanie/ECN_dept_data/input/ECN_enrollment_2171.csv'

tbl = pd.read_csv(file_nm, parse_dates=True, engine='python')
tbl = tbl.drop_duplicates()
class_nbrs = tbl['Class Nbr'].unique()
cols = ['Catalog Nbr', 'Primary Instructor', 'Count']
df_counts = pd.DataFrame(index=class_nbrs, columns=cols)
for c in class_nbrs:
    prof = tbl.loc[tbl['Class Nbr'] == c,'Primary Instructor'].unique()[0]
    df_counts.loc[c,'Primary Instructor'] = prof
    cat_nbr = tbl.loc[tbl['Class Nbr'] == c,'Catalog Nbr'].unique()[0]
    df_counts.loc[c,'Catalog Nbr'] = cat_nbr
df_counts['Count'] = tbl['Class Nbr'].value_counts()

tot = df_counts['Count'].sum()

fig, ax = plt.subplots()
ax.scatter(df_counts.index, df_counts['Count']/tot, s=df_counts['Count'])
plt.show()

profs = df_counts['Primary Instructor'].unique()
courses = df_counts['Catalog Nbr'].unique()
lower = courses[courses < 300]
theory = [312, 313, 410, 425]
electives = [306, 315, 331, 355, 394]
upper_electives = [413, 416, 421, 438, 445, 453, 455, 475, 484, 493, 499]
#theory_mask = df_counts['Catalog Nbr'].isin([312, 313, 410, 425])
#theory = df_counts[theory_mask, 'Catalog Nbr'].unique()



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
#dtypes: float64(1), int64(9), object(26)
#memory usage: 2.6+ MB
