# N-Body Physics Simulator (and Visualisator)

## How to contribute

1. Fork the project.
2. Write tests (TDD if possible) and write code, commit and push it to your forked repository.
3. Do a pull request.
4. You will receive a code review soon.
5. If quality of code is high enough and test coverage is 100%, code will be merged. Otherwise: *go to step 6*.
6. After we wrote a code review, you could improve your code according to our suggestions. Please, improve your code.
7. *Go to step 3*.

## How to run
### Linux
Not implemented yet.

## Goals
### General
- [ ] 100% test coverage
- [ ] Reading data from a .CSV-file
- [ ] Writing data to a .CSV-file
### Simulator
- [ ] Optimizing code for CPU (use of async-code, multiple threads?)
- [ ] Optimizing code for GPU. GPU's are really good in doing many simple functions. (We could use ArrayFire, OpenCL or CUDA)
- [ ] The possibility to theoretically calculate infinite bodies
- [ ] Changing the change in time (Δt) based on the distance of bodies to eachother
- [ ] Collision detection
- [ ] Space ship: a body with the possibility to change speed depending on commands
### Visualisator
- [ ] Showing the data of the simulator on xy-, yz- and xz-diagrams
- [ ] Changeable virtual time
- [ ] Determining the middle of the display