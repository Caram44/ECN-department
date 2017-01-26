#This program takes in a file created by
# My majors by term, academic org CECON and CECONOMICS
import sys
sys.path.append('/Users/cmcdanie/ECNdept/dept_python/library/')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from term_functions import previous_term, spring_fall_only, term_label_list
from matplotlib.patches import Rectangle


def all_stu_count(file_nm, term_range, plans):
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
    return df_count


def plot_majors_by_level(infile, term_range, outfile):
    dftot = all_stu_count(infile, term_range, ['BAECNBS', 'LAECNBS'])
    dfWPC = all_stu_count(infile, term_range, ['BAECNBS'])
    dfCLAS = all_stu_count(infile, term_range, ['LAECNBS'])
    terms = list(dfWPC.index)
    dfs = [dfWPC, dfCLAS]
    y_pos = np.arange(len(terms))
    levels = list(dfWPC.columns)
    colors = ['xkcd:faded pink', 'xkcd:light gray blue',
              'xkcd:greenish tan', 'xkcd:sandy yellow']
    val = dftot['Total']
    plt.matplotlib.rcParams.update({'font.size': 12})
    fig, ax = plt.subplots(figsize=(8, 6))
    for ind in range(0, len(levels) - 1):
        ax.bar(y_pos, val, color=colors[ind],
               edgecolor='black', align='center', label=levels[ind])
        ax.set_xticks(y_pos)
        ax.set_xticklabels(term_label_list(terms))
        ax.set_yticks(np.arange(0, 1600, 50), minor=True)
        ax.set_ylim([0, 1400])
        ax.bar(y_pos, val - dfs[1][levels[ind]], color=colors[ind],
               edgecolor='black', hatch='///', align='center')
        #ax.yaxis.grid(which='both', color='k', linestyle=':', linewidth=0.5)
        p = Rectangle((0, 0), 1, 1, fc="lightgray", edgecolor='black',
                      hatch='///')
        pp = Rectangle((0, 0), 1, 1, fc="lightgray", edgecolor='black')
        second_legend = plt.legend([p, pp], ["WPC", "CLAS"], loc=1,
                                   framealpha=0.01)
        plt.legend(loc=2, framealpha=0.1)
        plt.gca().add_artist(second_legend)
        val = val - dftot[levels[ind]]
        plt.savefig(outfile)
    plt.show()


#def plot_majors_by_level_side(infile, term_range, outfile):



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
