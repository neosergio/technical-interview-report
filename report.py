import argparse
import csv
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
            elif row_type == constants.REPORT_ROW or \
                    row_type == constants.ADDITIONAL_REPORT_ROW:
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
