import openpyxl


# 예제 안되넹 ;;;


wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
for i in range (1,11):
    sheet['A'+str(i)].value = i

referenceObject = openpyxl.charts.Reference(sheet, (1,1), (10,1))
seriesObject = openpyxl.charts.Series(referenceObject, title='First series')
chartObject = openpyxl.charts.BarChart()
chartObject.append(seriesObject)

chartObject.drawing.top = 50
chartObject.drawing.left = 100
chartObject.drawing.width = 300
chartObject.drawing.height = 200

sheet.add_chart(chartObject)
wb.save('sampleChart.xlsx')