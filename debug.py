
from click.testing import CliRunner

from sqlmesh.cli.main import cli


runner=CliRunner()
tmp_path='test311'
result = runner.invoke(
    cli, ["--log-file-dir", tmp_path, "--paths", tmp_path, "plan", "--auto-apply"]
)
print(result.exit_code)