#This functions assist in identifying and converting PeopleSoft term codes
#this function determines if a term is
#spring, summer or fall

term_descript = {1: 'Spring', 4: 'Summer', 7: 'Fall'}


def find_semester(strm):
    term_descript = {1: 'Spring', 4: 'Summer', 7: 'Fall'}
    term_val = str(strm)[3]
    term_int = int(term_val)
    semester = term_descript[term_int]
    return semester


def year_convert(strm):
    term_str = str(strm)
    year = term_str[0] + '0' + term_str[1:3]
    return year


def term_label(strm):
    sem = find_semester(strm)
    year = year_convert(strm)
    term = sem + ' ' + year
    return term

def term_label_list(strms):
    semesters = []
    for strm in strms:
        term = term_label(strm)
        semesters.append(term)
    return semesters

def previous_term(strm):
    #returns previous fall or spring term
    term_str = str(strm)
    pre_term = 0
    if term_str[3] == '7':
        pre_term = strm - 6
    if term_str[3] == '1':
        pre_term = strm - 4
    return pre_term


def spring_fall_only(strms):
    #returns only summer and fall from a
    #list of terms
    terms = []
    for strm in strms:
        term_str = str(strm)
        if term_str[3] == '4':
            terms = terms
        else:
            terms.append(int(term_str))
    return terms
