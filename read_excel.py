import xlrd


def add_space(val):
    return ' ' * val


file_name = 'mon.xlsx'
dir_name = 'D://Python_projects//tests//'
out_file = 'out.sql'
lst = []
s = ' '
tmp_table = 'tmp.lo_monetka_not_working'
del_table = f'if OBJECT_ID(\'{tmp_table}\') is NOT NULL\ndrop table {tmp_table};\n\n'
alter_table = f"""ALTER TABLE {tmp_table}
	    ADD CONSTRAINT [lo_monetka_not_working_pk] PRIMARY KEY ([ID])
	  GO"""
rd = xlrd.open_workbook(file_name)
sheet = rd.sheet_by_index(0)
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    lst.append(row)

with open(out_file, 'w') as f:
    f.write(del_table)
    f.write(f'WITH R ([ID],[SHOPID],[NAME],[NOT_WORKING],[ADDRESS_ID])\n AS (\n')
    for item in enumerate(lst[1:], start=1):
        f.write(f'{add_space(4)}select {item[0]},\'{item[1][0]}\',\'{item[1][1]}\',\'{item[1][2]}\', Null\n')
        if item[1] != lst[-1]:
            f.write(f'{add_space(6)}union all\n')
    f.write(')\n')
    f.write(f'{add_space(4)}Select * into {tmp_table} from R\n\n')
    f.write(f'{add_space(4)}{alter_table}')
