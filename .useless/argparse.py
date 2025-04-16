import argparse

devMode = False

arg_devmode = argparse.ArgumentParser(
        prog="ActName",
        description="howitwork")
arg_devmode.add_argument("--dev", action="store_true", help="Enable dev mode without typing d!")

arg_check = arg_devmode.parse_args()
devMode = arg_check.dev

print(str(devMode))
