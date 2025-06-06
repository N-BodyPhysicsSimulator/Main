from __future__ import print_function

import nbp
import pytest

from nbp import Cli

def test_required_arguments(capsys):
    argv = "python3 nbp_cli.py".split(" ")

    with pytest.raises(SystemExit):
        Cli(argv).start_application()

    out, err = capsys.readouterr()
    assert "the following arguments are required" in err
    assert "--inputprovider/-i" in err
    assert "--delta-time/-dt" in err
    assert "--outputwriter/-o" in err

def test_forbid_max_ticks_with_max_time(capsys):
    argv = "python3 nbp_cli.py -i json -o json -dt 1 --max-ticks 1 --max-time 1".split(" ")

    with pytest.raises(SystemExit):
        Cli(argv).start_application()

    out, err = capsys.readouterr()
    assert "--max-time/-T" in err
    assert "not allowed with argument" in err
    assert "--max-ticks/-t" in err
