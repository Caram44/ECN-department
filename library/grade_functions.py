import pandas as pd
import matplotlib.pyplot as plt
tbl = pd.read_csv('../csv_files/class_grades_2107_2141.csv',parse_dates = True)

#turn grades into numbers


def gpa_calc(df):
	from numpy import sum
	#this takes a two column data frame and returns a single GPA value
	noGPA = ['-','Y','LC','Z','X']
	df = df[~df['Crse Grade Off'].isin(noGPA)]
	if len(df) == 0:
		return 0
	else:
		grdpt = {'A+':4.33,'A': 4.0,'A-':3.67, 'B+':3.33,'B':3.0,'B-':2.67,'C+':2.33,'C':2.0,'D':1.0,'E':0,'XE':0}
		for l in grdpt:
			df['Crse Grade Off'][df['Crse Grade Off'] == l] = grdpt[l]
			pts = df['Crse Grade Off']*df['Unt Taken']
		return np.sum(pts)/np.sum(df['Unt Taken'])

def letter_to_GPA(df):
	from numpy import sum
	#this takes a two column data frame and returns a single GPA value
	noGPA = ['-','Y','LC','Z','X']
	df = df[~df['Crse Grade Off'].isin(noGPA)]
	if len(df) == 0:
		return 0
	else:
		grdpt = {'A+':4.33,'A': 4.0,'A-':3.67, 'B+':3.33,'B':3.0,'B-':2.67,'C+':2.33,'C':2.0,'D':1.0,'E':0,'XE':0}
		for l in grdpt:
			df['Crse Grade Off'][df['Crse Grade Off'] == l] = grdpt[l]
		return df



#Strm                  13794  non-null values
#Term                  13794  non-null values
#Subject               13794  non-null values
#Catalog Nbr           13794  non-null values
#Crse Id               13794  non-null values
#Crse Offer Nbr        13794  non-null values
#Class Nbr             13794  non-null values
#Class Title           13794  non-null values
#Topic Title           248  non-null values
#Session Code          13794  non-null values
#Class Section         13794  non-null values
#Class Career          13794  non-null values
#Class Type            13794  non-null values
#Component             13794  non-null values
#Building Code         13536  non-null values
#Room                  13536  non-null values
#Primary Instructor    13536  non-null values
#Capacity              13794  non-null values
#Emplid                13794  non-null values
#Posting Id            13794  non-null values
#Person Nm             13794  non-null values
#Stdnt Enrl Status     13794  non-null values
#Enrl Status Reason    13794  non-null values
#Grade Basis           13794  non-null values
#Unt Taken             13794  non-null values
#Crse Grade Off        13794  non-null values
#Program and Plan      13794  non-null values
#Academic Level        13794  non-null values
#Asu Asurite Id        13794  non-null values
#Asu Email Addr        13794  non-null values
#Ferpa Flg             13794  non-null values
#Trf Gpa               13794  non-null values
#Cum Gpa               13794  non-null values
#Admit Type            13117  non-null values
#Tot Cumulative        13794  non-null values
#Tot Taken Gpa         13794  non-null values
#Cur Gpa               13794  non-null values
#Unt Taken Prgrss      13794  non-null values
#
