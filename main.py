from var_dump import var_dump
from pprint import pprint


class Converter:
    def __init__(self, file_name, FileReader):
        self.file_name = file_name
        self.file_reader = FileReader
        pprint(self.file_reader.__class__)

    def load_file(self):
        # return self.file_reader.read(self, self.file_name)
        return FileReader.read(self, self.file_name)

    def save_file(self):
        FileWriter.write(self, self.file_name, self.lines)


class FileReader:
    def read(self, file_name):
        with open(file_name, 'r') as f:
            return list(f.readlines())


class FileWriter:
    def save(self, file_name, lines):
        with open(file_name, 'w') as f:
            f.writelines(self, lines)


def main():
    file = 'import_small.csv'
    file_reader = FileReader()
    # print(file_reader.__class__)
    converter = Converter(file, file_reader)
    pprint(converter.load_file())


if __name__ == '__main__':
    main()
