import os
import csv
from datetime import datetime


class file_parser:

    def validation(self, value):
        if value.strip():
            return int(value)
        else:
            return None

    def is_valid(self, data):
        if data['Max TemperatureC'].strip() and \
                data['Min TemperatureC'].strip() and \
                data['Max Humidity'].strip() and \
                data[' Mean Humidity'].strip():
            return True
        else:
            return False

    def required_weather_data(self, row_data):
        req_field = {}
        if 'PKST' in row_data:
            req_field['date'] = datetime.strptime(row_data['PKST'], '%Y-%m-%d')
        else:
            req_field['date'] = datetime.strptime(row_data['PKT'], '%Y-%m-%d')
        req_field['max_temp'] = self.validation(row_data['Max TemperatureC'])
        req_field['min_temp'] = self.validation(row_data['Min TemperatureC'])
        req_field['max_humid'] = self.validation(row_data['Max Humidity'])
        req_field['mean_humid'] = self.validation(row_data[' Mean Humidity'])

        return req_field

    def read_files_data(self, path):
        weather_data = []
        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                with open(os.path.join(path, filename)) as weather_file:
                    data_reader = csv.DictReader(weather_file)
                    for row in data_reader:
                        if self.is_valid(row):
                            weather_data.append(self.required_weather_data(row))
        return weather_data
