from __future__ import annotations

import pytest

from raman_bacteria_prototype import cli


@pytest.mark.unit
def test_environment_cli_success(monkeypatch, capsys) -> None:
    monkeypatch.setattr(cli, "run_environment_checks", lambda: (0, {"status": "PASS"}))
    assert cli.check_environment_main([]) == 0
    assert "PASS" in capsys.readouterr().out


@pytest.mark.unit
def test_checks_cli_success(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(
        cli, "run_checks", lambda **kwargs: (0, {"overall_status": "PASS"})
    )
    assert cli.run_checks_main(["--output", str(tmp_path / "out.json")]) == 0
    assert "PASS" in capsys.readouterr().out


@pytest.mark.unit
def test_environment_cli_rejects_unexpected_arguments(
    monkeypatch,
    capsys,
) -> None:
    def fail_if_called():
        pytest.fail("run_environment_checks must not run when arguments are invalid")

    monkeypatch.setattr(cli, "run_environment_checks", fail_if_called)

    assert cli.check_environment_main(["unexpected"]) == 2

    captured = capsys.readouterr()

    assert captured.out == ""
    assert "Usage: raman-check-environment" in captured.err


@pytest.mark.unit
def test_checks_cli_rejects_bad_arguments(capsys) -> None:
    assert cli.run_checks_main(["unexpected"]) == 2
    assert "Usage" in capsys.readouterr().err


@pytest.mark.unit
def test_checks_cli_propagates_failure(monkeypatch) -> None:
    monkeypatch.setattr(
        cli, "run_checks", lambda **kwargs: (1, {"overall_status": "FAIL"})
    )
    assert cli.run_checks_main([]) == 1
