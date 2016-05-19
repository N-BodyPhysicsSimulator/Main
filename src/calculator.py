import pickle
import base64
import argparse

class Calculator:
    def __init__(self, bodies, tick):
        self.bodies = bodies
        self.tick = tick

    def calculate(self):
        return bodies

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticks")
    parser.add_argument("change-in-time")
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()

    ticks = int(args.ticks)

    with open(args.input, 'r') as f:
        bodies = pickle.loads(base64.b64decode(f.readline()))
        f.close()

    calc = Calculator(bodies, ticks)

    with open(args.output, 'a') as f:
        for x in range(0, ticks):
            f.write(
                base64.b64encode(
                    pickle.dumps(
                        calc.calculate()
                    )
                ).decode('utf-8') + "\n"
            )

        f.close()
