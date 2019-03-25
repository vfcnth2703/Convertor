from var_dump import var_dump
from pprint import pprint


class Converter:
    def __init__(self, file_name, FileReader):
        self.file_name = file_name
        self.FileReader = FileReader

    def load_file(self):
        return FileReader.read(self, self.file_name)

    def save_file(self, FileWriter):
        FileWriter.write(self.file_name)


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
    file_rider = FileReader()
    converter = Converter(file, file_rider)
    pprint(converter.load_file())


if __name__ == '__main__':
    main()
