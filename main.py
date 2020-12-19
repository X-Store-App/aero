import argparse
import getConfig


def __main__():
    # CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("task", nargs="?")
    parser.parse_args()
    args = parser.parse_args()
    if args.task is None:
        args.task = 'default'
    print(args)


if __name__ == "__main__":
    __main__()
