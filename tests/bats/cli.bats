#!/usr/bin/env bats

@test "required arguments" {
  run python3.5 nbp_cli.py

  [ "$status" -eq 2 ]
  [[ "$output" =~ "the following arguments are required" ]]
  [[ "$output" =~ "--inputprovider/-i" ]]
  [[ "$output" =~ "--outputwriter/-o" ]]
  [[ "$output" =~ "--delta-time/-dt" ]]
}

@test "forbid using --max-ticks and --max-time together" {
  run python3.5 nbp_cli.py -i json -o json -dt 1 --max-ticks 1 --max-time 1

  [ "$status" -eq 2 ]
  [[ "$output" =~ "--max-time/-T" ]]
  [[ "$output" =~ "not allowed with argument" ]]
  [[ "$output" =~ "--max-ticks/-t" ]]
}

