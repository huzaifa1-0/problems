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
            return pd.DataFrame()

    def computing(self):
        if not self.data.empty:
            average_temprature = self.data['temprature'].mean()
            average_humidity = self.data['humidity'].mean()
            return average_temprature, average_humidity
        return None, None

    def getmaxtemperature(self):
        if not self.data.empty:
            max_temperature = self.data['temprature'].max()
            return self.data[self.data['temprature'] == max_temperature]
        return pd.DataFrame()