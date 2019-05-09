from clipboard import copy
from pprint import pprint as pp
from var_dump import var_dump as vv
# a = ['%PORTABLE_PROF_ASCN_SYSTEM%', '%DATE%2018-11-13', '%USER%Аспидов РП', '%USER%Новиков ИГ', '%USER%Рещиков АВ', '%USER%Трофимов ВВ', '%USER%Кузин КГ', '%USER%Безяев СН', '%USER%Максягин АЮ', '%USER%Семенютин ИВ', '%USER%Пономарёв СВ', '%USER%Кузнецов АМ', '%USER%Устинский ДВ', '%USER%Боголюбов АН', '%USER%Казорин АА', '%USER%Бочаров ДА', '%USER%Мурашов АА', '%USER%Голомазов АВ', '%USER%Закотский АС', '%USER%Караханов АР', '%USER%Казаков ИЮ', '%USER%Тимаков ДМ', '%USER%Рыжков РА', '%USER%_Кудрявцев АБ', '%USER%Егоркин НД', '%USER%Курнасенков АВ', '%USER%Скакун ВН', '%DATA%1-84/14399', '%DATA%1-84/14428', '%DATA%1-84/14375', '%DATA%1-84/14375', '%DATA%1-84/14375', '%DATA%1-84/14375', '%DATA%1-84/14375', '%DATA%1-84/14375', '%DATA%1-84/14375']
# for_search = '%USER%'
# for item in a:
#     if item.startswith(for_search):
#  index = a.index(item)
#  break
# print(a[index])


# a = 'Итоговая статистика по выработке инженеров'
# b = 'Процент Просроченных и Успешных заявок'
# c = 'Кол-во заявок * удаленный коэффициент * сложность работ'
# d = 'Финальный раcчет'
# print(help(clipbord.copy))
# print(a.center(80, '-'))
# copy(a.center(80, '-'))
# copy(b.center(80, '-'))
# copy(c.center(80, '-'))
# copy(d.center(80, '-'))
# copy(80 * '-')
# copy('#statistics'.upper())


a = ['ОКЕЙ 6ч. 12x7', 'ОКЕЙ 5ч. 12x7', 'ОКЕЙ 5ч. 12x7', 'ОКЕЙ 4ч. 24x7', 'ОКЕЙ 8ч. 8x5', 'ОКЕЙ 5ч. 12x7', 'ОКЕЙ 4ч. 8x5', 'ОКЕЙ 5ч. 8x5', 'ОКЕЙ 5ч. 24x7', 'ОКЕЙ 6ч. 8x5', 'ОКЕЙ 5ч. 24x7', 'ОКЕЙ 8ч. 8x5', 'ОКЕЙ 4ч. 12x7', 'ОКЕЙ 5ч. 12x7', 'ОКЕЙ 5ч. 12x7', 'ОКЕЙ 5ч. 24x7', 'ОКЕЙ 5ч. 24x7', 'ОКЕЙ 5ч. 24x7', 'ОКЕЙ 4ч. 24x7', 'ОКЕЙ 9ч. 8x4', 'ОКЕЙ 5ч. 8x5', 'ОКЕЙ 5ч. 12x7', 'ОКЕЙ 5ч. 8x5', 'ОКЕЙ 5ч. 12x7', 'ОКЕЙ 8ч. 8x5', 'ОКЕЙ 5ч. 12x7']
a.sort()
b = set(a)
d = list(b)
d.sort()
id_list = [x for x in range(-37, (-37 - 10), -1)]
zz = dict(zip(id_list, d))
for key, value in zz.items():
    # print(f'{key},{value}')
    print(f'insert into DOG_ReactionTimeTypes (ID, Caption, WorkFrom, WorkTo,ReactionHours, Info, WorkDayFrom, WorkDayTo, ReactionTimeType_Kind ) values ({key},\'{value}\',null,null,null,\'\',1,7,2);')
# print(len(id_list))


ПОРТ СКС: ремонт на кассовой линейке
ПОРТ СКС: ремонт не на кассовой линейке ≥ 10 шт.
ПОРТ СКС: ремонт не на кассовой линейке ≤ 9 шт.
