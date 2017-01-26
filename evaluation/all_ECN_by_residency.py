import sys
sys.path.append('/Users/cmcdanie/ECNdept/dept_python/library/')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from term_functions import previous_term, spring_fall_only, term_label_list

#def all_stu_count(file_nm, term_range, plans):
#This function returns a datframe of enrollments by plan
#Plans is a list and can include more than one plan
tbl = pd.read_csv(file_nm, parse_dates=True, engine='python')
tbl = tbl.drop_duplicates()
cols = ['Senior', 'Junior', 'Sophomore', 'Freshman', 'Total']
terms = tbl['Strm'].unique()
#Clean up terms to include only summer fall
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
df_count = df_count.sort_index()
#return df_count
