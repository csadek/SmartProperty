import xlrd


class ReadExcel:
        """ This class to read data from excel sheets """
        def get_sheets(file_path, sheetname):
                # create an empty list to store rows
                rows = []
                # open the specified Excel spreadsheet as workbook
                book = xlrd.open_workbook(file_path,encoding_override='utf8')
                # get the first sheet
                # iterate through the sheet and get data from rows in list
                sheet1 = book.sheet_by_name(sheetname[0])
                sheet2 = book.sheet_by_name(sheetname[1])
                for row_idx in range(1, sheet2.nrows):
                    rows.append(list(sheet1.row_values(1, 0, sheet1.ncols)))
                for row2 in range(1, sheet2.nrows):
                    for cell in sheet2.row_values(row2, 0, sheet2.ncols):
                                rows[row2-1].append(cell)
                return rows
        """ This class to read data from excel sheets """
        def get_sheet(file_path, sheetname):
                # create an empty list to store rows
                rows = []
                # open the specified Excel spreadsheet as workbook
                book = xlrd.open_workbook(file_path,encoding_override='utf8')
                # get the first sheet
                sheet = book.sheet_by_name(sheetname)
                # iterate through the sheet and get data from rows in list
                for row_idx in range(1, sheet.nrows):
                    rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
                return rows