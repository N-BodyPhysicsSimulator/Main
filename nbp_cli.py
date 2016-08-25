if __name__ != "__main__":
    print("File should be executed")
else:
    from nbp import Cli

    Cli(
        Cli.get_parser().parse_args()
    ).start_application()
