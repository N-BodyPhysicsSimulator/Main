@test "delta-time greater than 0" {
  run python3.5 nbp_cli.py -i json -o json -dt 0

  [ "$status" -eq 2 ]
  [[ "$output" =~ "--delta-time/-dt" ]]
  [[ "$output" =~ "Value should be greater than 0" ]]
}

@test "max-ticks greater than 0" {
  run python3.5 nbp_cli.py -i json -o json -dt 1 --max-ticks 0

  [ "$status" -eq 2 ]
  [[ "$output" =~ "--max-ticks/-t" ]]
  [[ "$output" =~ "Value should be greater than 0" ]]
}

@test "max-time greater than 0" {
  run python3.5 nbp_cli.py -i json -o json -dt 1 --max-time 0

  [ "$status" -eq 2 ]
  [[ "$output" =~ "--max-time/-T" ]]
  [[ "$output" =~ "Value should be greater than 0" ]]
}

@test "delta-time not negative" {
  run python3.5 nbp_cli.py -i json -o json -dt -1

  [ "$status" -eq 2 ]
  [[ "$output" =~ "--delta-time/-dt" ]]
  [[ "$output" =~ "Value should be greater than 0" ]]
}

@test "max-ticks not negative" {
  run python3.5 nbp_cli.py -i json -o json -dt 1 --max-ticks -1

  [ "$status" -eq 2 ]
  [[ "$output" =~ "--max-ticks/-t" ]]
  [[ "$output" =~ "Value should be greater than 0" ]]
}

@test "max-time not negative" {
  run python3.5 nbp_cli.py -i json -o json -dt 1 --max-time -1

  [ "$status" -eq 2 ]
  [[ "$output" =~ "--max-time/-T" ]]
  [[ "$output" =~ "Value should be greater than 0" ]]
}

@test "delta-time positive" {
  run python3.5 nbp_cli.py -i json -o json -dt 1

  [[ ! "$output" =~ "--delta-time/-dt" ]]
  [[ ! "$output" =~ "Value should be greater than 0" ]]
}

@test "max-ticks positive" {
  run python3.5 nbp_cli.py -i json -o json -dt 1 --max-ticks 1

  [[ ! "$output" =~ "--max-ticks/-t" ]]
  [[ ! "$output" =~ "Value should be greater than 0" ]]
}

@test "max-time positive" {
  run python3.5 nbp_cli.py -i json -o json -dt 1 --max-time 1

  [[ ! "$output" =~ "--max-time/-T" ]]
  [[ ! "$output" =~ "Value should be greater than 0" ]]
}