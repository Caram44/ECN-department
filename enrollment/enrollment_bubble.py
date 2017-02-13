import sys
sys.path.append('/Users/cmcdanie/ECNdept/dept_python/library/')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from term_functions import previous_term, spring_fall_only, term_label_list

tbl = pd.read_csv(file_nm, parse_dates=True, engine='python')
tbl = tbl.drop_duplicates()
cols = ['Senior', 'Junior', 'Sophomore', 'Freshman', 'Total']
terms = tbl['Strm'].unique()
