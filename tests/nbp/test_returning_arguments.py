from __future__ import print_function

import nbp
import pytest

from nbp import Cli

def test_test(capsys):
    with pytest.raises(SystemExit):
        Cli().start_application()

    # [ "$status" -eq 2 ]
    # [[ "$output" =~ "the following arguments are required" ]]
    # [[ "$output" =~ "--inputprovider/-i" ]]
    # [[ "$output" =~ "--outputwriter/-o" ]]
    # [[ "$output" =~ "--delta-time/-dt" ]]
    out, err = capsys.readouterr()
    assert "the following arguments are required" in err
    print(out, err)
