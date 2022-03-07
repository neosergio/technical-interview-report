import csv
import json as json_lib

import pyperclip
import typer

import constants


app = typer.Typer()


@app.command()
def main(input_file: str, json: bool = False):
    """
    Generate a report from a CSV file.

    If --json is passed, the report will be in JSON format.
    """
    final_report = {}
    with open(input_file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            row_type = row[constants.TYPE]
            row_topic = row[constants.TOPIC]
            row_subtopic = row[constants.SUBTOPIC]
            row_value = row[constants.EVALUATION]
            if row_type == constants.SECTION_ROW:
                final_report[row_topic] = {
                    "1": [],
                    "2": [],
                    "3": [],
                    "4": [],
                    "5": [],
                    "Comments": [],
                }
            elif row_type in (constants.REPORT_ROW, constants.ADDITIONAL_REPORT_ROW):
                if row_value:
                    if row_type == constants.REPORT_ROW:
                        if row_subtopic:
                            row_topic = row_subtopic
                        final_report[list(final_report)[-1]][row_value[0]].append(
                            row_topic
                        )
                    elif row_type == constants.ADDITIONAL_REPORT_ROW:
                        final_report[list(final_report)[-1]]["Comments"].append(
                            f"{row_topic}: {row_value}"
                        )

    printing_result = ""
    if json:
        json_result = json_lib.dumps(final_report, indent=4)
        printing_result += json_result
    else:
        for key in final_report:
            printing_result += "\n"
            printing_result += f"{key}\n"
            printing_result += "========================\n"
            for subkey, value in final_report[key].items():
                if value:
                    if subkey in constants.LEVELS:
                        printing_result += f"{constants.LEVELS[subkey]}: \n"
                    printing_result += f'{", ".join(value)} \n'

    typer.echo(printing_result)
    pyperclip.copy(printing_result)


if __name__ == "__main__":
    app()
