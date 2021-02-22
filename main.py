import argparse
import os
from datetime import datetime

from file_parser import file_parser
from calculations import calculations
from reports import reports


def is_dir(path):
    if os.path.isdir(path):
        return path
    else:
        print("Invalid directory path")


def validate_year_date(date):
    try:
        return datetime.strptime(date, '%Y')
    except ValueError:
        print(f'{date} is not valid')


def validate_month_date(date):
    try:
        return datetime.strptime(date, '%Y/%m')
    except ValueError:
        print(f'{date} is not valid')


def parse_args():
    parser = argparse.ArgumentParser(description="Process Command Line Arguments")
    parser.add_argument("path", type=is_dir)
    parser.add_argument("-e", "--yearly_date", type=validate_year_date)
    parser.add_argument("-a", "--monthly_date", type=validate_month_date)
    parser.add_argument("-c", "--bar_chart", type=validate_month_date)
    return parser.parse_args()


if __name__ == '__main__':

    args = parse_args()
    if args.path:
        file_reader = file_parser()
        weather_data = file_reader.read_files_data(args.path)
        weather_calculation = calculations()

        if args.yearly_date:
            calculated_year_data = weather_calculation.yearly_weather_calculation(weather_data, args.yearly_date)
            reports.generate_yearly_report(calculated_year_data)

        if args.monthly_date:
            calculated_monthly_data = weather_calculation.monthly_weather_calculation(weather_data, args.monthly_date)
            reports.generate_monthly_report(calculated_monthly_data)

        if args.bar_chart:
            calculated_bar_charts_data = weather_calculation.bar_charts_calculation(weather_data, args.bar_chart)
            reports.generate_bar_charts_reports(calculated_bar_charts_data, args.bar_chart)
            print('\nBonus Task\n')
            reports.bonus_task_reports(calculated_bar_charts_data, args.bar_chart)

