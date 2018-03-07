import xlrd
from itertools import takewhile
import xlrd

def column_len(sheet, index):
    col_values = sheet.col_values(index)
    col_len = len(col_values)
    for _ in takewhile(lambda x: not x, reversed(col_values)):
        col_len -= 1
    return col_len

# clox 代表 A-CO, A = 0, AA = 26, BA = 52, CA = 78
#第一張(氣象)表到 BL，第二章(災害)表到 AR，第三張(地形)表到 CO
wb = xlrd.open_workbook('氣象詞彙與編碼表_v4.3.xlsx')

sheet = wb.sheet_by_index(0)  #表示讀第幾張表，初始為0

# col 代表 A - Z(column)，index 代表 0 - n(row)
for col in range(0,63): #check sheet 1
    col_len = column_len(sheet, col)
    for index in range ( 0 , col_len):
        if( sheet.cell(rowx = index, colx = col).value=="" ):
            continue
        print ( sheet.cell(rowx = index, colx = col).value)
