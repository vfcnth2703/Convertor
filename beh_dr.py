asterisk_cnt = 23


def calc_len(key, value):
    return len(key) + len(str(value)) + 5


def fill_line(char, mult):
    return char * (asterisk_cnt - mult)


def save_file(file_name, source):
    with open(file_name, 'w', encoding='UTF-8') as tf:
        for item in source:
            print(item, file=tf)


def read_file(file_name):
    a = []
    with open(file_name, 'r', encoding='UTF-8') as f:
        data = f.readlines()
    for item in data:
        a.append(tuple(item.split()))
    return(dict(a))


def parse_dict(data):
    char = '.'
    total = 0
    out = []
    header = 'Деньги на ДР'
    header = header.center(23, '.').upper()
    out.append('*' * asterisk_cnt)
    out.append(f'{header}')
    out.append('*' * asterisk_cnt)
    for key, value in sorted(data.items()):
        total += int(value)
        out.append(f'{key}{fill_line(char,calc_len(key,value))}{value} руб.')
    out.append('*' * asterisk_cnt)
    out.append(f'Всего сдало {len(data)} человек.')
    out.append(f'Итого: {total} руб.')
    out.append('*' * asterisk_cnt)
    return out


def main():
    file_name = 'money.txt'
    source = parse_dict(read_file(file_name))
    save_file('check.txt', source)


if __name__ == '__main__':
    main()
