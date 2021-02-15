import argparse
import csv
import json

import constants


def generate_report(filepath):
    report = dict()
    with open(filepath, 'r') as file:
        csv_file = csv.reader(file, delimiter=',')
        for row in csv_file:
            row_type = row[0]
            row_topic = row[1]
            row_subtopic = row[2]
            row_value = row[3]
            if row_type == constants.SECTION_ROW:
                report[row_topic] = {"1": list(),
                                     "2": list(),
                                     "3": list(),
                                     "4": list(),
                                     "5": list(),
                                     "Comments": list()}
            elif row_type in (constants.REPORT_ROW,
                              constants.ADDITIONAL_REPORT_ROW):
                if row_value:
                    if row_type == constants.REPORT_ROW:
                        if row_subtopic:
                            row_topic = row_subtopic
                        report[list(report.keys())[-1]][row_value[0]]\
                            .append(row_topic)
                    elif row_type == constants.ADDITIONAL_REPORT_ROW:
                        report[list(report.keys())[-1]]["Comments"]\
                            .append(f'{row_topic}: {row_value}')
    return report


def print_report(report, output_format='text'):
    if output_format == 'json':
        json_result = json.dumps(report, indent=4)
        print(json_result)
    elif output_format == 'text':
        levels = {'1': 'Cannot Perform',
                  '2': 'Can perform with supervision',
                  '3': 'Can perform with limited supervision',
                  '4': 'Can perform without supervision',
                  '5': 'Can teach others'}
        for key in report:
            print("\n")
            print(key)
            print("==========")
            for sub_key, value in report[key].items():
                if value:
                    if sub_key in levels:
                        print(levels[sub_key] + ": ")
                    print(", ".join(value))


parser = argparse.ArgumentParser(description='Generate a report.',
                                 epilog='Happy Coding! :)')
parser.add_argument('csv_file_path',
                    metavar='CSV filepath',
                    type=str,
                    help='input csv file path')
parser.add_argument('-f', '--format', default='text',
                    help='output format (text/json)')
args = vars(parser.parse_args())

report = generate_report(filepath=args.get('csv_file_path'))
print_report(report=report, output_format=args.get('format').lower())
