import xlsxwriter


def export_check(text):
    data = text.split('\n')
    for i in range(len(data)):
        data[i] = data[i].split('\t')
        data[i][1] = float(data[i][1])
        data[i][2] = int(data[i][2])
        data[i] = tuple(data[i])
    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()

    for row, (item, price, count) in enumerate(data):
        # for i in range(len(data)):
        # for row, (item, price, count) in enumerate(data[i]):
        worksheet.write(row, 0, item)
        worksheet.write(row, 1, price)
        worksheet.write(row, 2, count)
        worksheet.write(row, 3, count * price)

    row += 1
    worksheet.write(row, 0, 'Итого')
    worksheet.write(row, 3, f'=SUM(D1:D{len(data)}')
    workbook.close()
