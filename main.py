# coding=utf-8
from var_dump import var_dump
from pprint import pprint
import reader
import os.path


class Converter:
    def __init__(self, file_name, file_reader, file_writer):
        self.file_name = file_name
        self.file_reader = file_reader
        self.file_writer = file_writer

    def load_file(self):
        return self.file_reader.read(self.file_name)

    def save_file(self):
        self.file_writer.write(self.file_name, self.lines)


class FileReader:
    def __init__(self, file_checker):
        self.file_checker = file_checker

    def read(self, file_name):
        self.file_checker.check(file_name)
        with open(file_name, 'r') as f:
            return list(f.readlines())


class FileWriter:
    def save(self, file_name, lines):
        with open(file_name, 'w') as f:
            f.writelines(self, lines)


class FileChecker:
    def check(self, file_name):
        if not os.path.exists(file_name):
            raise IOError("File not found.")


def main():
    file = 'import_small.csv'
    file_checker = FileChecker()
    file_writer = FileWriter()
    file_reader = FileReader(file_checker)
    converter = Converter(file, file_reader, file_writer)
    var_dump(converter.load_file())


if __name__ == '__main__':
    main()
