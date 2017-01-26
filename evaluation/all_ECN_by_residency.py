import sys
sys.path.append('/Users/cmcdanie/ECNdept/dept_python/library/')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from term_functions import spring_fall_only, term_label_list

file_nm = '/Users/cmcdanie/ECN_dept_data/input/ECN_majors_2141_2171.csv'
plans = ['LAECNBS', 'BAECNBS']
term_range = [2147, 2171]


def all_stu_res(file_nm, term_range, plans):
    #This function returns a datframe of enrollments by residency
    #Plans is a list and can include more than one plan
    tbl = pd.read_csv(file_nm, parse_dates=True, engine='python')
    tbl = tbl.drop_duplicates()
    #Clean up terms to include only summer fall
    terms = tbl['Strm'].unique()
    terms = terms[terms >= term_range[0]]
    terms[terms <= term_range[1]]
    report_terms = spring_fall_only(terms)
    report_terms = sorted(report_terms)
    tbl = tbl[tbl['Strm'].isin(terms)]
    tbl = tbl[tbl['Acad Plan'].isin(plans)]
    #Create residency series
    cols = ['Arizona', 'Domestic non-res', 'International', 'Total']
    tbl['Residency_revised'] = np.nan
    AZmask = tbl['Residency'] == 'RES'
    tbl.loc[AZmask, 'Residency_revised'] = 'Arizona'
    Intl_mask = tbl['Asu Citzn Country'] != 'USA'
    tbl.loc[Intl_mask, 'Residency_revised'] = 'International'
    Oos_mask = pd.isnull(tbl['Residency_revised'])
    tbl.loc[Oos_mask, 'Residency_revised'] = 'Domestic non-res'
    #Create dataframe to store output
    df_count = pd.DataFrame(columns=cols, index=[report_terms])
    for term in report_terms:
        term_mask = tbl.Strm == term
        for res in cols[0:-1]:
            res_mask = tbl.loc[term_mask, 'Residency_revised'] == res
            tot = len(tbl.loc[term_mask].loc[res_mask])
            df_count.loc[term][res] = tot
    df_count['Total'] = df_count[cols[0:-1]].sum(axis=1)
    df_count = df_count.sort_index()
    return df_count


def plot_majors_by_residency(infile, term_range, outfile):
    dftot = all_stu_res(infile, term_range, ['BAECNBS', 'LAECNBS'])
    dfWPC = all_stu_res(infile, term_range, ['BAECNBS'])
    dfCLAS = all_stu_res(infile, term_range, ['LAECNBS'])
    terms = list(dfWPC.index)
    dfs = [dfWPC, dfCLAS]
    y_pos = np.arange(len(terms))
    levels = list(dfWPC.columns)
    colors = ['xkcd:dusty orange', 'xkcd:saffron',
              'xkcd:greyish teal']
    val = dftot['Total']
    plt.matplotlib.rcParams.update({'font.size': 14})
    fig, ax = plt.subplots(figsize=(12, 8))
    for ind in range(0, len(levels) - 1):
        ax.bar(y_pos, val, color=colors[ind],
               edgecolor='black', align='center', label=levels[ind])
        ax.set_xticks(y_pos)
        ax.set_xticklabels(term_label_list(terms))
        ax.set_yticks(np.arange(0, 1800, 50), minor=True)
        ax.bar(y_pos, val - dfs[1][levels[ind]], color=colors[ind],
               edgecolor='black', hatch='///', align='center')
        plt.legend(loc=2)
        val = val - dftot[levels[ind]]
        ax.grid(which='both', color='k', linestyle=':', linewidth=0.5)
        plt.savefig(outfile)
    plt.show()

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
#Residency             12945 non-null object
