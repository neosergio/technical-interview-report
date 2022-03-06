# technical-interview-report
A report generator tool from technical interview spreadsheets templates.

## About
This is a simple command-line tool to generate and print a report in two formats (JSON/text) from a CSV file with technical interview notes.

## Requirements
- Python 3.10+
- Typer
- Poetry

## Running from source code
Clone repository, install the dependencies using Poetry and execute

```bash
$ python generate_report.py sample_interview_template.csv
```

## Usage
You can change the sample_interview_template.csv with any other CSV file identical format to use this tool. 
It is not a requirement to put a CSV file inside any specific folder, due the parameter is a file path, so you can use this tool like this:

```bash
$ python generate_report.py ~/Downloads/candidate_interview.csv
``` 

Also, you can use format parameter, to define JSON output or plain text output, if you don't specify the output format, the plain text should be executed by default:

```bash
$ python generate_report.py ~/Downloads/candidate_interview.csv --json
```

If you need any help regarding the command tool usage, you can review the documentation with --help parameter:

```bash
$ python generate_report.py --help
```

## Limitations
This tool only works with CSV files with sample interview template format.

## Copyright

2022 Sergio Infante

## License

GNU GPL, Version 3.0