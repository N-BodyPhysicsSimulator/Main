# N-Body Physics Simulator (and Visualisator)
[![codecov](https://codecov.io/gh/N-BodyPhysicsSimulator/main/branch/master/graph/badge.svg)](https://codecov.io/gh/N-BodyPhysicsSimulator/main)
[![Build Status](https://travis-ci.org/N-BodyPhysicsSimulator/Main.svg?branch=master)](https://travis-ci.org/N-BodyPhysicsSimulator/Main)
## How to contribute

1. Fork the project.
2. Write tests (TDD if possible [[1 NL]](https://nl.wikipedia.org/wiki/Test-driven_development) [[1 EN]](https://en.wikipedia.org/wiki/Test-driven_development)) and write code.
3. Commit [[1]](http://chris.beams.io/posts/git-commit/) [[2]](https://github.com/erlang/otp/wiki/writing-good-commit-messages) [[3]](https://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message) (**READ THOSE THREE LINKS**, *please*) and push it to your forked repository. 
4. Do a pull request. [[1]](https://yangsu.github.io/pull-request-tutorial/) [[2]](https://help.github.com/articles/using-pull-requests/) [[3]](https://help.github.com/articles/creating-a-pull-request/)
5. You will receive a code review soon.
6. If quality of code is high enough and Code Coverage is 100% [[1]](https://en.wikipedia.org/wiki/Code_coverage)  [[2]](http://stackoverflow.com/questions/195008/what-is-code-coverage-and-how-do-you-measure-it), code will be merged. Otherwise: *go to step 7*.
7. After we wrote a code review, you could improve your code according to our suggestions. Please, improve your code.
8. *Go to step 4*.

## How to run
### Linux
Not implemented yet.

## Goals

### General
- [ ] 100% code coverage
- [ ] <del>Reading and</del> writing results to a <del>.CSV-file</del> Excel-file (Excel will be used because of the possibility of multiple sheets/tabs. A different program will be created to export Pickle-files to Excel files.)
- [ ] Reading start-values of bodies from JSON or CSV
- [ ] Reading and writing data from a file ([Pickle](https://docs.python.org/3/library/pickle.html) with [Base64](https://docs.python.org/3/library/base64.html))

### Conversions
- [x] Import and export from/to Pickle with Base64

### Simulator
- [ ] Optimizing code for CPU (use of async-code, multiple threads?)
- [ ] Optimizing code for GPU. GPU's are really good in doing many simple functions. (We could use ArrayFire, OpenCL or CUDA)
- [ ] The possibility to theoretically calculate infinite bodies
- [ ] Changing the change in time (Δt) based on the distance of bodies to eachother
- [ ] Collision detection
- [ ] Space ship: a body with the possibility to change speed depending on commands

### Visualisator
- [ ] Showing the data of the simulator on xy-, yz- and xz-diagrams (2D)
- [ ] Changeable virtual time
- [ ] Determining the middle of the display
- [ ] Showing the data of the simulator in three dimensions (xyz, 3D)
