
class calculations:

    def yearly_required_fields(self, data):
        req_data = {}
        req_data['max_temp'] = data['max_temp']
        req_data['max_temp_date'] = data['date']
        req_data['min_temp'] = data['min_temp']
        req_data['min_temp_date'] = data['date']
        req_data['max_humidity'] = data['max_humid']
        req_data['max_humidity_date'] = data['date']

        return req_data

    def yearly_weather_calculation(self, weather_data, date):
        default = 0
        req_data = {}
        for data in weather_data:
            if data['date'].year == date.year:
                default += 1
                if default == 1:
                    req_data = self.yearly_required_fields(data)
                else:
                    if req_data['max_temp'] < data['max_temp']:
                        req_data['max_temp'] = data['max_temp']
                        req_data['max_temp_date'] = data['date']

                    if req_data['min_temp'] > data['min_temp']:
                        req_data['min_temp'] = data['min_temp']
                        req_data['min_temp_date'] = data['date']

                    if req_data['max_humidity'] < data['max_humid']:
                        req_data['max_humidity'] = data['max_humid']
                        req_data['max_humidity_date'] = data['date']

        return req_data

    def monthly_weather_calculation(self, weather_data, date):
        req_data = {}
        total_records = 0
        sum_max_temp = 0
        sum_min_temp = 0
        sum_mean_humidity = 0
        for data in weather_data:
            if data['date'].year == date.year and data['date'].month == date.month:
                total_records += 1
                sum_max_temp += data['max_temp']
                sum_min_temp += data['min_temp']
                sum_mean_humidity += data['mean_humid']
        req_data['avg_max'] = int(sum_max_temp/total_records)
        req_data['avg_min'] = int(sum_min_temp/total_records)
        req_data['avg_humidity'] = int(sum_mean_humidity/total_records)

        return req_data

    def bar_charts_calculation(self, weather_data, date):
        bar_chart_records = []
        for data in weather_data:
            if data['date'].year == date.year and data['date'].month == date.month:
                bar_chart_records.append(data)

        return bar_chart_records






