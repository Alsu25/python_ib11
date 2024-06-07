import sys
import xlsxwriter


def sp(s):
    nam, sm = s.split()
    sm = int(sm)
    return nam, sm


data = list(map(str.strip, sys.stdin))
data1 = list(map(sp, data))

workbook = xlsxwriter.Workbook('res.xlsx')
worksheet = workbook.add_worksheet()
for row, (item, price) in enumerate(data1):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, price)

chart = workbook.add_chart({'type': 'pie'})
chart.add_series({'values': '=Sheet1!B1:B5', 'categories': '=Sheet1!A1:A5'})
worksheet.insert_chart('C3', chart)
workbook.close()