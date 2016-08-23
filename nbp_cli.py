if __name__ != "__main__":
    print("File should be executed")
else:
    from nbp import cli

    args = cli.get_parser().parse_args()
    cli.start(args);
        
