EMPLOYEES = [["Surname", "FirstName", "Age", "Salary"],
             ["Smith", "Mary", 25, 2000],
             ["Black", "Lucy", 40, 3000],
             ["Verdi", "Nico", 36, 4500],
             ["Smith", "Mark", 40, 3900]]

R2 = [["Department", "Head"],
      ["production", "Mori"],
      ["sales", "Brown"]]

GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             ["Surname", "O'Malley", 39],
             [9824, "Darkes", 38]]

R3 = [[1, 2, 3]]


def filter_employees(row):
    """
    Check if employee represented by row
    is AT LEAST 30 years old and makes
    MORE THAN 3500.
    :param row: A List in the format:
        [{Surname}, {FirstName}, {Age}, {Salary}]
    :return: True if the row satisfies the condition.
    """
    return row[-2] >= 300 and row[-1] > 3500

# !/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists. """


#####################
# HELPER FUNCTIONS ##
#####################

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """
    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass


def selection(t1, f):
    """
    Perform select operation on table t that satisfy condition f. Return the result of function f applied on table t

    :param t1: list of lists
    :param f: a function that affects the rows of t1
    :return: result, a list of lists

    """
    i = 1
    result = []
    pass
    result.append(t1[0])
    # iterates through table
    while i < len(t1):
        if f(t1[i]):
            result.append(t1[i])
        i += 1
    # if table only has schema column
    if len(result) == 1:
        result = None
    return result


def projection(t, r):
    """
    Takes in a table and and an attribute list containing schemas. Returns the parts of the table that match the schema
    :param t: a list of lists
    :param r: a list containing the header columns that should be returned
    :return: result, a list of lists
    """
    # i tracks which row within the table is being compared. 
    i = 0
    # j tracks which row within the table is being compared.
    j = 0
    # k tracks the spot for the attribute list. 
    k = 0
    
    result = [[]]
    match_list = []
    
    if len(t[0]) < len(r):
        raise UnknownAttributeException

    try:
        while k < len(r):
            while j < len(t[i]):
                if t[i][j] == r[k]:
                    result[i].append(t[i][j])
                    match_list.append(j)
                j += 1
            j = 0
            k += 1
        i = 1
        while i < len(t):
            result.append([])
            for numeral in match_list:
                result[len(result)-1].append(t[i][numeral])
            i += 1

    except AssertionError:
        for item in r:
            for header in t:
                if r[item] not in t[header]:
                    raise UnknownAttributeException

    return result

print projection(EMPLOYEES, ["Surname"])


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.

    :param t1: a table as a list of lists
    :param t2: a table as a lists of lists
    :return: result, a lists of lists with the cross-product of t1 and t2

    """
    i = 1
    j = 1

    # merge table schemas
    result = [t1[0] + t2[0]]
    # iterates through table1
    while i < len(t1):
        # iterates through table2
        while j < len(t2):
            result.append(t1[i]+t2[j])
            j += 1
        j = 1
        i += 1
        # if tables only have schema column
    if len(result) == 1:
        result = None

    return result
