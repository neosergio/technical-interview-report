from typer.testing import CliRunner

from generate_report import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["sample_interview_template.csv"])
    assert result.exit_code == 0
    assert 'Result' in result.output
    assert 'English level' in result.output
    assert 'Python' in result.output

    help_result = runner.invoke(app, ['--help'])
    assert 'Show this message and exit.' in help_result.output
    assert help_result.exit_code == 0

    result_json = runner.invoke(app, ["sample_interview_template.csv", "--json"])
    assert result_json.exit_code == 0
    assert 'Result' in result_json.output
