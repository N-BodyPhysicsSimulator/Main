from __future__ import print_function

import nbp
import pytest

from nbp import Cli


def greater_than_zero(capsys, command, parameter):
    argv = command.split(" ")
    with pytest.raises(SystemExit):
        Cli(argv).start_application()

    out, err = capsys.readouterr()
    assert parameter in err
    assert "Value should be greater than 0" in err

def greater_than_zero_should_pass(capsys, command, parameter):
    argv = command.split(" ")
    with pytest.raises(SystemExit):
        Cli(argv).start_application()

    out, err = capsys.readouterr()
    assert parameter not in err
    assert "Value should be greater than 0" not in err

def test_delta_time_greater_than_zero(capsys):
    greater_than_zero(
        capsys,
        "python3 nbp_cli.py -i json -o json -dt 0",
        "--delta-time/-dt"
    )

def test_max_ticks_greater_than_zero(capsys):
    greater_than_zero(
        capsys,
        "python3 nbp_cli.py -i json -o json -dt 1 --max-ticks 0",
        "--max-ticks/-t"
    )

def test_max_time_greater_than_zero(capsys):
    greater_than_zero(
        capsys,
        "python3 nbp_cli.py -i json -o json -dt 1 --max-time 0",
        "--max-time/-T"
    )

def test_delta_time_not_negative(capsys):
    greater_than_zero(
        capsys,
        "python3 nbp_cli.py -i json -o json -dt -1",
        "--delta-time/-dt"
    )

def test_max_ticks_not_negative(capsys):
    greater_than_zero(
        capsys,
        "python3 nbp_cli.py -i json -o json -dt 1 --max-ticks -1",
        "--max-ticks/-t"
    )

def test_max_time_not_negative(capsys):
    greater_than_zero(
        capsys,
        "python3 nbp_cli.py -i json -o json -dt 1 --max-time -1",
        "--max-time/-T"
    )

def test_delta_time_positive(capsys):
    greater_than_zero_should_pass(
        capsys,
        "python3 nbp_cli.py -i json -o json -dt 1",
        "--delta-time/-dt"
    )

def test_max_ticks_positive(capsys):
    greater_than_zero_should_pass(
        capsys,
        "python3 nbp_cli.py -i json -o json -dt 1 --max-ticks 1",
        "--max-ticks/-t"
    )

def test_max_time_positive(capsys):
    greater_than_zero_should_pass(
        capsys,
        "python3 nbp_cli.py -i json -o json -dt 1 --max-time 1",
        "--max-time/-T"
    )
