import pandas as pd

class dataanalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            return pd.read_csv(self.file_path)
        except FileNotFoundError:
            print('file not found')
            return pd.dataFrame()

    def computing(self):
        if not self.data.empty:
