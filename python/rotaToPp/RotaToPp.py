#!/bin/python

import xlrd
import datetime
import pprint
from prettytable import PrettyTable
import prettytable
import sys

WIDEST_COL = 10

def SplitForWidestCol(str, widest_col):
    strOut = ''
    c = -1
    for ch in str:
        c = c + 1
        if c > widest_col and ch==' ':
            c = -1
            strOut += '\n'
        else:
            strOut += ch
    return strOut

def PrintWorksheet(xlsName, sheetIx):
    REPLACEMENTS = [ ('_ ', '_'), (' _', '_'),
                     ('_Guitar', '<G>'), ('_Drums', '<D>'), ('_Flute', '<F>'),
                     ('_Bass', '<B>'), (' Guitar', '_<G>'),
                     (' Guitar', '<G>'), (' Drums', '<D>'), (' Flute', '<F>'),
                     (' Bass', '<B>'), (' Guitar', '_<G>'),
                     ]
    with xlrd.open_workbook(xlsName) as wb:
        pt = None
        sh = wb.sheet_by_index(sheetIx)  # or wb.sheet_by_name('name_of_the_sheet_here')
        row = -1
        for r in range(sh.nrows):
            row = row + 1
            rv = sh.row_values(r)
            rv = rv[0:8]
            # Dates in excel = 1899/12/30 + x (days)
            rv_0_as_float = -1
            try:
                rv_0_as_float = float(rv[0])
            except:
                pass
            if rv_0_as_float>0 :
                dt = datetime.datetime(1899, 12, 30) + datetime.timedelta(days=rv_0_as_float)
                rv[0] = dt.date()
                
            # Remove redundant spaces
            for i in range(0, len(rv)):
                s = str(rv[i])
                s = s.rstrip(' ').lstrip(' ')
                for repl in REPLACEMENTS :
                    s = s.replace(repl[0], repl[1])
                while True:
                    sNew = s.replace('  ', ' ')
                    if sNew==s:
                        break
                    s = sNew
                rv[i] = SplitForWidestCol(s, WIDEST_COL)
            # c.writerow(rv)

            if row==0:
                rvCopy = rv
                for i in range(0, len(rvCopy)):
                    if rvCopy[i]=='':
                        rvCopy[i] = 'r{}'.format(i+1)
                pt = PrettyTable(rvCopy)
                pt.padding_width = 1
                pt.hrules = prettytable.ALL
            else:
                pt.add_row(rv)
        if pt:
            print pt
            # print pt.get_html_string()
        
if __name__ == '__main__':
    PrintWorksheet(sys.argv[1], int(sys.argv[2]))