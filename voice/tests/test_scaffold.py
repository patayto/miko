"""Milestone 1 placeholder: the package imports and the CLI wires up.

Real tests arrive with each milestone (parsing fixtures in milestone 2, etc.).
"""

from typer.testing import CliRunner

from voiceclone import config
from voiceclone.cli import app

runner = CliRunner()


def test_cli_help_lists_commands():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    for command in ("prep", "stats", "rag", "serve-smoke", "route", "eval"):
        assert command in result.output


def test_stub_commands_exit_nonzero():
    result = runner.invoke(app, ["prep"])
    assert result.exit_code == 1
    assert "milestone 2" in result.output


def test_config_paths_point_inside_repo():
    assert config.RAW_ROOT.name == "raw"
    assert config.PROJECT_ROOT.name == "voice"
    assert set(config.SOURCES) == {"obsidian", "icloud", "aichats"}
