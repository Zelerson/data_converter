import pandas as pd


class Converter:
    def __init__(self, file_path, changes):
        self.file_path = file_path
        self.df = self.read_file()
        self.changes = [x.split(',') for x in changes]

    def read_file(self):
        extension = self.file_path.split('.')[-1].lower()
        read_functions = {
            'csv': pd.read_csv,
            'json': pd.read_json,
            'pkl': pd.read_pickle,
            'txt': pd.read_csv
        }

        if extension in read_functions:
            return read_functions[extension](self.file_path)
        else:
            raise FileNotFoundError

    def implement_changes(self):
        for x in self.changes:
            self.df.iloc[int(x[1]), int(x[0])] = x[2]


class CSVConverter(Converter):
    def convert(self, out_file_path):
        self.implement_changes()
        self.df.to_csv(out_file_path, index=False)


class JSONConverter(Converter):
    def convert(self, out_file_path):
        self.implement_changes()
        self.df.to_json(out_file_path)


class PKLConverter(Converter):
    def convert(self, out_file_path):
        self.implement_changes()
        self.df.to_pickle(out_file_path)


class TXTConverter(Converter):
    def convert(self, out_file_path):
        self.implement_changes()
        self.df.to_csv(out_file_path, index=False, header=False)