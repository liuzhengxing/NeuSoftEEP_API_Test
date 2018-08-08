# _*_ coding: utf-8 _*_

import xlrd

from xlutils.copy import copy


def excel_write(fdir, sheetname, i, j, value):
    fileobj = xlrd.open_workbook(fdir)
    sheet = fileobj.sheet_by_name(sheetname)
    sheet.put_cell(i, j, 1, value, 0)
    wb = copy(fileobj)
    wb.save(fdir)


def excel_read(fdir, sheetname, i, j):
    fileobj = xlrd.open_workbook(fdir)
    sheet = fileobj.sheet_by_name(sheetname)
    value = sheet.cell(i, j).value
    return value


def excel_readline(fdir, sheetname, row):
    fileobj = xlrd.open_workbook(fdir)
    sheet = fileobj.sheet_by_name(sheetname)
    val = sheet.row_values(row)
    return val


def excel_find(fdir, sheetname, key):
    fileobj = xlrd.open_workbook(fdir)
    sheet = fileobj.sheet_by_name(sheetname)
    row_count = sheet.nrows
    col_count = sheet.ncols
    gid = ''
    for element in range(row_count):
        if key.lower() in (str(sheet.row_values(element))).lower():
            gid = sheet.row_values(element)[1]
    return gid


if __name__ == '__main__':
    print(excel_read(2, 1))
    print(excel_find('EquipInspectPartGid'))
    # excel_write(11, 0, 'efwfawfa')
    # excel_write(11, 1, 'gfslk4r2klvsjfklqj4l4j4j234fsa')
