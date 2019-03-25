# from typing import List

import pyperclip

export_header_line = "[ADRESS_ID],[TORG_POINT_ID],[ID],[CLASSIF_ID],[SER_NUM],[IS_HOLOGRAM_PASTED ],[IS_HOLOGRAM_FOUND],[TALON_NBR],[EXECUTOR_ID],[USER_ID ],[CLOSE_DATE],[IS_READY ],[CLOSE_STATUS_ID]"
import_header_line: str = "[talon_nomer],[task_head_id],[prof_priority_id],[firm_firm_id],[firm_name],[TorgPoint_ID],[torg_point_name],[address_id],[address],[user_id],[user_name ],[Data_Vaydachi],[Execution_Date],[Execution_To_Date],[Execution_Exactly_Date],[classif_id],[equipment_type],[clear_ser_num],[torg_point_memo],[task_memo],[firm_manager_id],[torg_point_firm_id],[is_kkm],[serial_nbr],[hologramm_so_nbr ],[gosreesrt_nbr],[firm_manger_name]"

export_header = "%EXPORT_PROF_ASCN_SYSTEM%"
import_header = "%PORTABLE_PROF_ASCN_SYSTEM%"


def read_file(file_name):
    with open(file_name, 'r') as f:
        return list(f.readlines())


def read_sublime_view():
    pass


def insert_hider_line(header_line, data):
    data.insert(0, header_line)
    return data


def prepare_import_file(file_body):
    tmp_list = []
    idx = 0
    for line in file_body:
        if line.startswith('%DATA%'):
            break
        idx += 1

    file_body = file_body[idx:]
    for line in file_body:
        line = line.replace('%DATA%', '')
        tmp_list.append(line)
    return tmp_list


def refine_file(data):
    tmp_data = list(map(lambda x: x.strip().split(';'), data))
    refined_data = []
    for item in tmp_data:
        line = ','.join(map(lambda x: "'" + x + "'", item))
        refined_data.append(line)
    return refined_data


def make_sql_vals(header_line, data):
    # сделать строку sql вида :
    # select * from (
    # values
    # ('1-84/14428', '200711')
    # as A([field_name1], [field_name1])
    sql = 'Select * from (\n'
    sql += 'values\n'
    sql += ',\n'.join(map(lambda x: '(' + x + ')', data[1:]))
    sql += ')\n'
    sql += 'as A (' + header_line + ')'
    return sql


def make_sql(data):
    # сделать строку sql вида :
    # with a ([field_name1], [field_name2]) as (
    # select field_value1, field_value2
    # union all
    # select field_value1, field_value2)
    sql = 'with a (' + data[0] + ') as (\n'
    sql += 'union all\n'.join(map(lambda x: 'Select ' + x + '\n', data[1:]))
    sql += ')\n'
    sql += 'Select * from a'
    return sql


def main():
    # TODO сделать плагин для SublimeText
    # file_name = 'roma_data.csv'
    file_name = 'D:\\_TMP\\Боголюбов АН.CSV'

    # file_name = 'export.csv'
    # file_name = 'import.csv'
    file_body = read_file(file_name)
    if len(file_body) > 10000:
        print('Слишком большой файл')
        exit()
    if file_body[0].strip() == import_header:
        data = prepare_import_file(file_body)
        data = refine_file(data)
        data = insert_hider_line(import_header_line, data)
        pyperclip.copy(make_sql_vals(import_header_line, data))
    else:
        data = refine_file(file_body[1:])
        data = insert_hider_line(export_header_line, data)
        pyperclip.copy(make_sql_vals(export_header_line, data))


if __name__ == '__main__':
    main()
