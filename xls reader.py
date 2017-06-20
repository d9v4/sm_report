import xlrd

i = 3
rb = xlrd.open_workbook('e:\\text\\17.xlsx')
sheet = rb.sheet_by_index(3)

#print(sheet.row_values(3)[5])
while True:
	if sheet.row_values(i)[5]:
		i=i+1
	else:
		print(i, sheet.row_values(i-1)[5])
		break
	print(sheet.row_values(i)[5])
	
input()
	
#from xlrd import open_workbook

#wb = open_workbook('d:\\gnatiuk\\work_xls\\17.xlsx')
#for s in wb.sheets(5):
#	print 'Sheet:',s.name
#	for row in range(s.nrows):
#		values = []
#		for col in range(s.ncols):
#			values.append(s.cell(row,col).value)
#	print ','.join(values)
#print