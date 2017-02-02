# N-Body Physics Simulator (and Visualisator
[![codecov](https://codecov.io/gh/N-BodyPhysicsSimulator/main/branch/master/graph/badge.svg)](https://codecov.io/gh/N-BodyPhysicsSimulator/main)
[![Build Status](https://travis-ci.org/N-BodyPhysicsSimulator/Main.svg?branch=master)](https://travis-ci.org/N-BodyPhysicsSimulator/Main)
## Installation by `pip`

`python3 -mpip install git+git://github.com/N-BodyPhysicsSimulator/Main.git`

## To run

`python3 -m nbp`

## How to contribute

1. Fork the project.
2. Write tests (TDD if possible [[1 NL]](https://nl.wikipedia.org/wiki/Test-driven_development) [[1 EN]](https://en.wikipedia.org/wiki/Test-driven_development)) and write code.
3. Commit [[1]](http://chris.beams.io/posts/git-commit/) [[2]](https://github.com/erlang/otp/wiki/writing-good-commit-messages) [[3]](https://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message) (**READ THOSE THREE LINKS**, *please*) and push it to your forked repository. 
4. Do a pull request. [[1]](https://yangsu.github.io/pull-request-tutorial/) [[2]](https://help.github.com/articles/using-pull-requests/) [[3]](https://help.github.com/articles/creating-a-pull-request/)
5. You will receive a code review soon.
6. If quality of code is high enough and Code Coverage is higher than before [[1]](https://en.wikipedia.org/wiki/Code_coverage)  [[2]](http://stackoverflow.com/questions/195008/what-is-code-coverage-and-how-do-you-measure-it), code will be merged. Otherwise: *go to step 7*.
7. After we wrote a code review, you could improve your code according to our suggestions. Please, improve your code.
8. *Go to step 4*.

## How to run from source

For running the simulator, Python `3.5.x` or higher is required.

Not tested on `Mac OS X`/`macOS` or `Microsoft Windows`.

### Linux / Mac OS X

#### Installation from source

1. Run `make install-requirements-app`
2. Run tests and make sure there aren't any failing tests.

#### Run tests

1. Install [bats](https://github.com/sstephenson/bats)
2. Run `make install-requirements-dev`
3. Run `make test`

#### Run application

- There are a few Input Providers, such as `csv` or `json` which you can use to import BodyStates (note: the `csv` Input Provider only imports one state. This is a required argument.
- There are as well Output Writers, to do something with the input. Like the `ws`, `http` and `csv` Output Writer. Required option.
- Delta Time is a required option as well. This is the change of time between two states.

For example: run `python3 -m nbp`

```
usage: nbp [-h] --inputprovider ip --outputwriter outputwriter
                  [outputwriter ...] --delta-time seconds
                  [--modifier [modifiers [modifiers ...]]]
                  [--max-ticks ticks | --max-time seconds]
nbp: error: the following arguments are required: --inputprovider/-i, --outputwriter/-o, --delta-time/-dt
```

- `max-ticks` is used to exit the simulator after a specific amount of ticks
- `max-time` is used to exit the simulator after a specific amount of time (see `delta-time`)
- `modifier` is used to modify data from the Input Provider before passing it to the Output Writers. You could use `calculation` to calculate new data.

You could run `python3 -m nbp --inputprovider json -o ws -dt 10`

```
[...]
nbp: error: the following arguments are required: --input-file, --ws-port
```

The `json` Input Provider requires parameter `--input-file` with a path to the JSON file and the `ws` Output Writer requires `--ws-port` with a port for the WebSocket server to 1listen on.

Let's run `python3 -m nbp --inputprovider json -o ws -dt 10 --input-file /home/<user>/input.json --ws-port 8080`

The simulator will now load the states from the JSON-file, but it won't calculate anything at all. We can use `--modifier` to make it calculate data.

Run command `python3 -m nbp --inputprovider json -o ws -dt 10 --input-file /home/<user>/input.json --ws-port 8080 --modifier calculation --max-ticks 10000`

The simulator will now import the states from the JSON-file, and it output all states from the JSON-file to the OutputWriters. On the last state, the CalculationModifier will start to calculate. Simulator will quit after 10000 states because of the `--max-ticks` option.

You can use multiple OutputWriters at once: `python3 -m nbp --inputprovider json --outputwriter json csv ws -dt 10 --input-file /home/<user>/input.json --json-output-file /home/<user>/output.json --csv-output-path /home/<user>/csv-output --ws-port 8080`

## Goals

### General
- [ ] 100% code coverage
- [x] Reading and writing results to a .CSV-file <del>Excel-file (Excel will be used because of the possibility of multiple sheets/tabs. A different program will be created to export Pickle-files to Excel files.)</del>
- [x] Reading start-values of bodies from JSON <del>or</del> and CSV
- [x] Reading and writing data from a file (JSON)

### Conversions
- [x] Import and export from/to Pickle with Base64

### Simulator
- [x] Optimizing code for CPU (use of async-code, multiple threads?)
- [ ] Optimizing code for GPU. GPU's are really good in doing many simple functions. (We could use ArrayFire, OpenCL or CUDA)
- [x] The possibility to theoretically calculate infinite bodies
- [x] Changing the delta time (change in time) based on the distance of bodies to eachother
- [ ] Spaceship: a body with the possibility to change speed depending on commands

### Visualisator
- [ ] Showing the data of the simulator on xy-, yz- and xz-diagrams (2D)
- [ ] Changeable virtual time
- [ ] Determining the middle of the display
- [ ] Showing the data of the simulator in three dimensions (xyz, 3D)
