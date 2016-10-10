if __name__ != "__main__":
    print("File should be executed")
else:
    from nbp import Cli
    from sys import argv

    Cli(argv[1:]).start_application()
