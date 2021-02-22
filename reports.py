class reports:

    def generate_yearly_report(data):
        print(
            f'Highest: {data["max_temp"]}C on {data["max_temp_date"].strftime("%B")} {data["max_temp_date"].day}\n'
            f'Lowest: {data["min_temp"]}C on {data["min_temp_date"].strftime("%B")} {data["min_temp_date"].day}\n'
            f'Humidity: {data["max_humidity"]}% on '
            f'{data["max_humidity_date"].strftime("%B")} {data["max_humidity_date"].day}\n'
        )

    def generate_monthly_report(data):
        print(
            f'Highest Average: {data["avg_max"]}C \n'
            f'Lowest Average: {data["avg_min"]}C \n'
            f'Average Mean Humidity: {data["avg_humidity"]}%'
        )

    def generate_bar_charts_reports(data, date):
        red = '\033[31m'
        blue = '\033[34m'
        color_end = '\033[00m'
        print(f'\n{date.strftime("%B")} {date.year}\n')
        for row in data:
            max_temp = '+' * row['max_temp']
            min_temp = '+' * row['min_temp']
            print(
                f'{row["date"].day} {red+max_temp+color_end} {row["max_temp"]}C\n'
                f'{row["date"].day} {blue + min_temp + color_end} {row["min_temp"]}C\n'
            )

    def bonus_task_reports(data, date):
        red = '\033[31m'
        blue = '\033[34m'
        color_end = '\033[00m'
        print(f'{date.strftime("%B")} {date.year}\n')
        for row in data:
            max_temp = '+' * row['max_temp']
            min_temp = '+' * row['min_temp']
            print(
                f'{row["date"].day} {blue + min_temp + color_end}'
                f'{red + max_temp + color_end} {row["min_temp"]}C - {row["max_temp"]}C \n'
            )
