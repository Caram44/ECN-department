#This program takes in a file created by
# My majors by term, academic org CECON and CECONOMICS
import sys
sys.path.append('/Users/cmcdanie/ECNdept/dept_python/library/')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from term_functions import previous_term, spring_fall_only

#y = range(20)
#x1 = range(20)
#x2 = range(0, 200, 10)

#fig, axes = plt.subplots(ncols=2, sharey=True)
#axes[0].barh(y, x1, align='center', color='gray')
#axes[1].barh(y, x2, align='center', color='gray')
#axes[0].invert_xaxis()
#plt.show()


def all_stu_count(file_nm, term_range, plans):
#This function returns a datframe of enrollments by plan
    #file_nm = '/Users/cmcdanie/ECN_dept_data/input/ECN_majors_2141_2171.csv'
    #term_range = [2147, 2171]
    tbl = pd.read_csv(file_nm, parse_dates=True, engine='python')
    tbl = tbl.drop_duplicates()
    cols = ['Senior', 'Junior', 'Sophomore', 'Freshman', 'Total']
    terms = tbl['Strm'].unique()
    terms = terms[terms >= previous_term(term_range[0])]
    terms[terms <= term_range[1]]
    report_terms = terms[terms >= term_range[0]]
    report_terms = spring_fall_only(report_terms)
    report_terms = sorted(report_terms)
    tbl = tbl[tbl['Strm'].isin(terms)]
    tbl = tbl[tbl['Acad Plan'].isin(plans)]
    df_count = pd.DataFrame(columns=cols, index=[report_terms])
    for term in report_terms:
        term_mask = tbl.Strm == term
        for level in cols[0:-1]:
            level_mask = tbl.loc[term_mask, 'Asu Acad Lvl Bot D'] == level
            tot = len(tbl.loc[term_mask].loc[level_mask])
            df_count.loc[term][level] = tot
    df_count['Total'] = df_count[cols[0:-1]].sum(axis=1)
#df_count.loc['All'] = df_count.loc[report_terms].sum()
#df_count.to_csv('ECNstudents_count' + term + '.csv')
    return df_count

#Strm                  12945 non-null int64
#Acad Org              12943 non-null object
#Asu Enroll Stat       12945 non-null object
#Last Name             12945 non-null object
#First Name            12945 non-null object
#Emplid                12945 non-null int64
#Acad Career           12945 non-null object
#Acad Plan             12945 non-null object
#Trnscr Descr          12943 non-null object
#Asu Prim Rec Flg      12945 non-null object
#Acad Prog             12945 non-null object
#Acad Prog Descr       12945 non-null object
#Acad Sub Plan         12945 non-null object
#Asu Acd Splan Desc    187 non-null object
#Asu Serv Ind Neg      12945 non-null object
#Asu Immun Hold        12945 non-null object
#Asu Honors Stu        12945 non-null object
#Asu Email Addr        12945 non-null object
#Person Nm             12945 non-null object
#Acad Level Bot        12945 non-null int64
#Tot Cumulative        12945 non-null float64
#Cum Gpa               12945 non-null float64
#Trf Gpa               12945 non-null float64
#Admit Term            12945 non-null int64
#Admit Type            11113 non-null object
#Asu Acad Lvl Bot D    12945 non-null object
#Gender Cd             12945 non-null object
#Tot Trnsfr            12945 non-null float64
#Asu Citzn Country     12945 non-null object
